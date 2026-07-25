# PLANNING · ZONING · PRE-DESIGN COMPLIANCE WORKFLOW
# التنظيم المدني · أنظمة المناطق · التحقّق التخطيطي قبل التصميم
# lebanese-building-law skill · planning-validation layer

> **Source & status of this file.** This workflow is adapted from the **ARTAVISION360 "AI Planning,
> Zoning & Building Regulations" module (v1.1)** — a **secondary, workflow source**, not the OCR of the
> Building Code. It is integrated here for its *procedure and its GENERAL-vs-ZONE-SPECIFIC discipline*,
> **not** as a new authority for numeric code values.
>
> - **All numeric Building-Law values remain owned by the primary references** (`QUICK_MATRIX.md`,
>   Master, Ledger) and keep their `OCR — VERIFY` status. This file does **not** restate or override them.
> - **Plot/zone-specific values (BCR, FAR, height, floors, setbacks, zoning class, land use, road width,
>   plot area) are NOT fixed by the Building Code.** They come from the plot's municipal **Planning /
>   Zoning sheet**. When they are not supplied, return **`LOCAL ZONING VERIFICATION REQUIRED`**.
> - Nothing here fabricates a zoning classification, a BCR, a FAR, or a setback. Missing → request or flag.

---

## 1 · The core distinction — GENERAL vs ZONE/PLOT-SPECIFIC

This is the most important rule in the whole skill. **The Application Decree (Law 646/2004) sets the
*rules of the game*; the plot's zoning sheet sets the plot's *specific numbers*.** Never present a
zone/plot-specific parameter as if the Building Code fixed it.

| Parameter | Classification | Where the value comes from | Default status when unsupplied |
|---|---|---|---|
| Zone classification (التصنيف) | **ZONE-SPECIFIC** | Municipal Zoning sheet | `LOCAL ZONING VERIFICATION REQUIRED` |
| Permitted land use (استعمال الأرض) | **ZONE-SPECIFIC** | Zoning sheet | `LOCAL ZONING VERIFICATION REQUIRED` |
| BCR — surface exploitation (معدل الاستثمار السطحي) | **ZONE-SPECIFIC** | Planning sheet | `LOCAL ZONING VERIFICATION REQUIRED` |
| FAR — general exploitation (عامل الاستثمار العام) | **ZONE-SPECIFIC** | Planning sheet | `LOCAL ZONING VERIFICATION REQUIRED` |
| Maximum building height (ارتفاع البناء) | **ZONE-SPECIFIC** | Planning sheet | `LOCAL ZONING VERIFICATION REQUIRED` |
| Maximum number of floors (عدد الطوابق) | **ZONE-SPECIFIC** | Planning sheet | `LOCAL ZONING VERIFICATION REQUIRED` |
| Setback distances F/R/sides (الارتدادات · التراجعات) | **ZONE-SPECIFIC** | Planning sheet | `LOCAL ZONING VERIFICATION REQUIRED` |
| Plot area (مساحة العقار) | **PLOT-SPECIFIC** | Survey drawing | `NEEDS INFO` |
| Road width (عرض الطريق) | **PLOT-SPECIFIC input** | Survey / planning | `NEEDS INFO` |
| How exploitation is computed & what's excluded | **GENERAL** | Building Code → Art 12 | `OCR — VERIFY` |
| Gabarit geometry (2.5× / 5× road width · 2/5 slope) | **GENERAL** | Building Code → Art 7 | `OCR — VERIFY` |
| Projection limits (balcony 1.05 m · cornice 1/8 · 0.60 m) | **GENERAL** | Building Code → Art 8 | `OCR — VERIFY` |
| View / light / ventilation (4.5 m · 30 m² · 4.5×5.5 · منور) | **GENERAL** | Building Code → Art 9 | `OCR — VERIFY` |
| Min/max clear heights (2.80 / 2.20 / 2.00 · max 5.75) | **GENERAL** | Building Code → Art 17 | `OCR — VERIFY` |
| Parking ratios & geometry (1/100 max 5 · stalls · ramps) | **GENERAL** | Building Code → Art 15 | `OCR — VERIFY` |
| Retaining walls · excavation · backfill · grading | **GENERAL** | Building Code → Art 2 | `OCR — VERIFY` |
| Basement backfilled/exposed rules | **GENERAL** | Building Code → Art 12 | `OCR — VERIFY` |

> Some parameters interact: **road width** is a plot input that feeds **code-fixed formulas** (gabarit
> 2.5×, balcony 9 m threshold, cornice 1/8). Supply the road width from the survey; apply the formula
> from the primary references (`OCR — VERIFY`).

---

## 2 · Planning parameter checklist (15)

Collect / confirm each before a full compliance review. Priority mirrors the ARTAVISION360 module.

| # | Parameter (EN) | العربية | Class | Priority |
|---|---|---|---|---|
| 1 | Plot Area | مساحة العقار | plot-specific | CRITICAL |
| 2 | Zone Classification | تصنيف المنطقة | zone-specific | CRITICAL |
| 3 | Land Use | استعمال الأرض | zone-specific | CRITICAL |
| 4 | BCR (surface exploitation) | معدل الاستثمار السطحي | zone-specific | CRITICAL |
| 5 | FAR (general exploitation) | عامل الاستثمار العام | zone-specific | CRITICAL |
| 6 | Maximum Building Height | الارتفاع الأقصى للمبنى | zone-specific | CRITICAL |
| 7 | Maximum Number of Floors | عدد الطوابق الأقصى | zone-specific | CRITICAL |
| 8 | Front Setback | التراجع الأمامي | zone-specific | CRITICAL |
| 9 | Rear Setback | التراجع الخلفي | zone-specific | CRITICAL |
| 10 | Side Setbacks (L/R) | التراجعات الجانبية | zone-specific | CRITICAL |
| 11 | Road Width | عرض الطريق | plot input | CRITICAL |
| 12 | Parking Requirement | متطلبات المواقف | Code method (Art 15) + count | HIGH |
| 13 | Special Municipality Conditions | الشروط الخاصة بالبلدية | municipal | HIGH |
| 14 | Natural Ground Level / Topography | مستوى الأرض الطبيعية / الطوبوغرافيا | survey | HIGH |
| 15 | Approved Planning (Takhteet) | التخطيط المصدّق | municipal | MEDIUM |

---

## 3 · Document priority hierarchy (conflict resolution)

When two documents disagree on the *same* parameter, **flag the conflict, never silently pick**, then
adopt the higher-priority value **and** state that it still needs verification.

1. **Municipality Planning Sheet** (مرفة التخطيط البلدي) — highest; zone-specific rules
2. **Official Zoning Sheet** (مرفة التنظيم) — zoning classification & permitted uses
3. **Official Building Code** (قانون البناء) — national baseline (this skill's primary references)
4. **Survey Drawing** (رسم المساحة) — legal plot dimensions & boundaries
5. **Site Analysis Report** — professional site data
6. **Architectural Strategy Document** — intent; informs, never overrides regulation
7. **User manual inputs** — lowest; only when no document has it; must be confirmed

**Conflict protocol:** detect → report (name both documents + values + priorities) → apply higher-
priority value → mark the parameter with a conflict flag in the validation table → require verification.
Never average or blend conflicting values. Never assume "no conflict" because values look similar.

---

## 4 · Zero-assumption policy (hard)

The skill **must never**:
- Assume a BCR/FAR/height/floors/setback from zone *type* alone → return `LOCAL ZONING VERIFICATION REQUIRED`.
- Estimate setbacks from photos, or invent a municipal condition.
- Apply another country's/city's rules without explicit confirmation.
- Fill missing data with "typical" or "average" values, or round a known value to guess an unknown one.
- Use general/training knowledge to substitute for a missing regulatory document.
- Proceed to design/verdict while a CRITICAL parameter is unknown.

The skill **must always**: request missing data; report conflicts before resolving; stop when
uncertainty can't be resolved; use only supplied documents + the verified references; label unclear-
source values `⚠️ SOURCE VERIFICATION REQUIRED`; distinguish confirmed vs unconfirmed data.

---

## 5 · Planning validation table (structure)

Produce this once inputs are gathered. Status legend: `[OK]` confirmed · `[MISS]` missing ·
`[CONFLICT]` conflicting · `~` approximate · `LZV` local-zoning-verification-required.

| Parameter | Value | Source (doc / Article·page) | Class | Status | Notes |
|---|---|---|---|---|---|
| Plot Area | … | Survey | plot | … | |
| Zone / Land Use | … | Zoning sheet | zone | … | LZV if unsupplied |
| BCR / FAR | … | Planning sheet | zone | … | LZV if unsupplied |
| Max Height / Floors | … | Planning sheet | zone | … | LZV if unsupplied |
| Setbacks F/R/L/R | … | Planning sheet | zone | … | LZV if unsupplied |
| Road Width | … | Survey | plot | … | feeds gabarit (Art 7) |
| Parking count | … | Art 15 method + program | Code+program | … | ratio `OCR — VERIFY` |
| Ground level / topo | … | Topo survey | survey | … | Art 2/11 datum |
| Municipality conditions | … | Municipal report | municipal | … | |

---

## 6 · Buildable-envelope method (formulas, not values)

The decree gives the *method*; the *inputs* (BCR, FAR, setbacks, height, plot area) are zone/plot-
specific. Compute only when those inputs are supplied and verified.

```
Net buildable footprint   = Plot area − (front + rear + side setback areas)     [setbacks: LZV]
Max ground-floor coverage = BCR × (per the plot's zoning basis)                 [BCR: LZV]
Max total built area      = FAR × plot area                                     [FAR: LZV]
Max height / floors       = from the plot's planning sheet                      [LZV]
```

**Basement note (GENERAL, Art 12):** a fully-buried basement (roof ≤ 1 m above ground, per Art 12 /
`QUICK_MATRIX` row) used as parking/storage/mechanical is **excluded** from FAR/BCR; other uses count
up to a 50 % cap. This exclusion *method* is code-fixed (`OCR — VERIFY`); the FAR it is measured
against is zone-specific (`LOCAL ZONING VERIFICATION REQUIRED`).

---

## 7 · Pre-design compliance gate

Do **not** issue a design-stage "clear to proceed" for a project until each is resolved:

```
[ ] Plot area confirmed (survey)
[ ] Zone classification + land use confirmed  ........  else LOCAL ZONING VERIFICATION REQUIRED
[ ] BCR + FAR confirmed (planning sheet)  .............  else LOCAL ZONING VERIFICATION REQUIRED
[ ] Max height + max floors confirmed  ................  else LOCAL ZONING VERIFICATION REQUIRED
[ ] All setbacks confirmed (F/R/L/R)  .................  else LOCAL ZONING VERIFICATION REQUIRED
[ ] Road width confirmed (survey)
[ ] Parking requirement computed (Art 15 method)
[ ] Municipality special conditions reviewed
[ ] Building-Code cross-check done against primary references
[ ] No unresolved conflicts (per §3)
```

If any zone-specific item is unconfirmed, the correct output is **not** a fabricated value — it is
`LOCAL ZONING VERIFICATION REQUIRED`, with a clear statement of what document would resolve it
(the plot's municipal planning/zoning sheet).

---

## 8 · Status tokens used across the skill

- `VERIFIED` — only where a reference explicitly marks a *structural* fact verified.
- `OCR — VERIFY` — default for every Building-Code numeric value (corrupted-OCR source).
- `⚠️ SOURCE VERIFICATION REQUIRED` — reference itself flags uncertainty, or a documented discrepancy.
- `LOCAL ZONING VERIFICATION REQUIRED` — parameter is zone/plot-specific and not supplied; the value
  is set by the plot's municipal planning/zoning sheet, not by the Building Code.
- `PROJECT ZONING (as provided)` — a zone value **read from the plot's supplied planning/zoning
  document** (see `PROJECT_ZONING_INTAKE.md`); project-scoped and session-only, confirm with the
  municipality, and **never** written into these references or reused across projects.
- `NOT FOUND IN CURRENT VERIFIED SOURCES` — the value/regulation is absent from the references; do not invent it.

> **Reading a supplied planning/zoning document:** when the user provides an ارتفاع وتخطيط / urban-
> planning sheet, follow `PROJECT_ZONING_INTAKE.md` — recognize it, pick the applicable Zone, extract
> that zone's row as `PROJECT ZONING (as provided)`, then combine with the GENERAL Building Law for the
> project check. Those values stay project-scoped; they never become universal rules.

---

## 9 · Anti-fabrication reminder (this file included)

Nothing here introduces a BCR, FAR, height, floor count, setback, zoning class, or land use as a
fact. Those are always the plot's — obtained from its municipal sheet or returned as
`LOCAL ZONING VERIFICATION REQUIRED`. Code *method and limits* stay owned by the primary references,
`OCR — VERIFY`, reconciled against the Gazette. This skill is a design-stage screen and retrieval aid —
**never** an authoritative legal or zoning certification.
