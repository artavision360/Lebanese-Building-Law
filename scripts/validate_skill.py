#!/usr/bin/env python3
"""
lebanese-building-law - skill integrity & structure validator (READ ONLY).

Verifies the skill is well-formed and that the LOCKED legal source files have not
been altered. This tool NEVER writes to, repairs, or normalizes any legal content;
it only reads and reports. Exit code 0 = all checks pass, 1 = at least one failure.

Checks
  1  SKILL.md frontmatter: name present, <= 64 chars
  2  SKILL.md frontmatter: description present, <= 1024 chars
  3  SKILL.md body budget: < 500 lines
  4  Every references/*.md path mentioned in SKILL.md resolves on disk
  5  Locked source files match scripts/reference-integrity.sha256 (tamper detection)
  6  Expected derived components exist (QUICK_MATRIX, COMPLIANCE_CHECKLIST, examples/)

ASCII-only output (Windows cp1252 consoles).
"""

import hashlib
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = SKILL_ROOT / "scripts" / "reference-integrity.sha256"

results = []  # (ok: bool, label: str, detail: str)


def check(ok, label, detail=""):
    results.append((bool(ok), label, detail))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def main() -> int:
    skill_md = SKILL_ROOT / "SKILL.md"
    if not skill_md.exists():
        check(False, "SKILL.md exists", str(skill_md))
        return report()

    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    fm = m.group(1) if m else ""

    # 1 name
    nm = re.search(r"^name:\s*(.+)$", fm, re.M)
    name = nm.group(1).strip() if nm else ""
    check(bool(name) and len(name) <= 64, "name present and <= 64",
          f"len={len(name)} value={name!r}")

    # 2 description
    dm = re.search(r'description:\s*"(.*)"', fm, re.S)
    desc = dm.group(1) if dm else ""
    check(bool(desc) and len(desc) <= 1024, "description present and <= 1024",
          f"len={len(desc)}")

    # 3 line budget
    lines = text.count("\n") + 1
    check(lines < 500, "SKILL.md < 500 lines", f"lines={lines}")

    # 4 referenced files resolve
    refs = sorted(set(re.findall(r"references/[A-Za-z0-9_./-]+\.md", text)))
    missing = [r for r in refs if not (SKILL_ROOT / r).exists()]
    check(not missing, "referenced files resolve",
          "missing: " + ", ".join(missing) if missing else f"{len(refs)} refs OK")

    # 5 locked-source integrity
    if not MANIFEST.exists():
        check(False, "integrity manifest present", str(MANIFEST))
    else:
        tampered, checked = [], 0
        for line in MANIFEST.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            expected, rel = parts[0], parts[-1]
            target = SKILL_ROOT / rel
            if not target.exists():
                tampered.append(f"{rel} MISSING")
                continue
            checked += 1
            if sha256(target) != expected:
                tampered.append(f"{rel} HASH MISMATCH")
        check(not tampered, "locked source files intact (no tampering)",
              "; ".join(tampered) if tampered else f"{checked} file(s) verified")

    # 6 derived components present
    expected_derived = [
        "references/QUICK_MATRIX.md",
        "references/PLANNING_ZONING_WORKFLOW.md",
        "references/PROJECT_ZONING_INTAKE.md",
        "references/COMPLIANCE_CHECKLIST.md",
        "examples/single-value-lookup.md",
        "examples/project-compliance-review.md",
    ]
    absent = [d for d in expected_derived if not (SKILL_ROOT / d).exists()]
    check(not absent, "derived components present",
          "absent: " + ", ".join(absent) if absent else f"{len(expected_derived)} present")

    return report()


def report() -> int:
    passed = sum(1 for ok, _, _ in results if ok)
    print("lebanese-building-law :: validate_skill.py (read-only)\n")
    for ok, label, detail in results:
        tag = "[PASS]" if ok else "[FAIL]"
        line = f"  {tag} {label}"
        if detail:
            line += f"  ({detail})"
        print(line)
    fails = len(results) - passed
    print(f"\n  {passed} passed, {fails} failed")
    print("  RESULT: " + ("PASS" if fails == 0 else "FAIL"))
    print("  NOTE: this validator never modifies legal content; it only reads and reports.")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
