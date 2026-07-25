# Example — project compliance review
# lebanese-building-law skill · demonstrates the checklist workflow, mixed statuses & no-certification close

> **Workflow demonstration only.** The **project inputs below are a hypothetical example**, clearly
> labeled as such — they are NOT legal data. Every **Building-Code value** is drawn from the verified
> references with its Article/page/figure and `OCR — VERIFY` status. Zone-specific parameters that were
> not supplied are returned as `LOCAL ZONING VERIFICATION REQUIRED`, never guessed.

---

## Example project inputs (hypothetical — for demonstration)

| Input | Example value | Note |
|---|---|---|
| Location | Batroun, Lebanon | in scope |
| Use | Single residential villa | |
| Plot area | 900 m² | from (example) survey |
| Road width | 10 m | from (example) survey |
| Zone / BCR / FAR / max height / floors / setbacks | **not provided** | no planning sheet supplied |
| Proposed habitable ceiling height | 2.90 m | design input |
| Proposed garage ramp slope | 18 % | design input |
| Proposed parking stalls | 4 | design input |
| Proposed living-room view depth | 4.0 m | design input |

---

## Compliance screen (design-stage)

| Requirement | Project Value | Legal Reference | Status | Notes |
|---|---|---|---|---|
| Zone classification / land use | not provided | Zoning sheet | `LOCAL ZONING VERIFICATION REQUIRED` | supply municipal sheet |
| BCR / FAR | not provided | Planning sheet | `LOCAL ZONING VERIFICATION REQUIRED` | Code gives method (Art 12); ratio is zonal |
| Max height / floors | not provided | Planning sheet | `LOCAL ZONING VERIFICATION REQUIRED` | Art 7/11 give method only |
| Setbacks (F/R/L/R) | not provided | Planning sheet | `LOCAL ZONING VERIFICATION REQUIRED` | required distances are zonal |
| Habitable clear height | 2.90 m | Art 17 · p74 · Fig 111 (min 2.80 m) `OCR — VERIFY` | **PASS** | 2.90 ≥ 2.80 |
| Garage ramp slope | 18 % | Art 15 · p62 · Fig 94 (≤ 20 %, >800 m²) `OCR — VERIFY` | **PASS** | 18 ≤ 20 |
| Parking count (housing) | 4 stalls | Art 15 · p58 (1/100 m², max 5) `OCR — VERIFY` | **NEEDS INFO** | needs FAR-counted residential area to compute requirement |
| Living-room view depth | 4.0 m | Art 9 · p27 · Fig 37 (min 4.50 m) `OCR — VERIFY` | **FAIL** | 4.0 < 4.50 — deepen opening / reduce room depth |
| Stall dimensions | not specified | Art 15 · p61 · Fig 93 (5.20×1.80 m) `OCR — VERIFY` | **NEEDS INFO** | provide stall layout |
| Restaurant parking (n/a here) | — | Art 15 · p59 | `SOURCE VERIFICATION REQUIRED` | ratio disputed in sources (1/30 vs 2/30) — not applicable to a villa |

---

## Verdict

```
COMPLIANCE SCREEN RESULT (design-stage)
------------------------------------------------------
PASS:                              2   (clear height, ramp slope)
FAIL:                              1   (view depth 4.0 m < 4.50 m)
NEEDS INFO:                        2   (parking calc, stall layout)
LOCAL ZONING VERIFICATION REQUIRED:4   (zone/use, BCR/FAR, height/floors, setbacks)

Overall: BLOCKED
  1. Resolve the FAIL: living-room opening must achieve ≥ 4.50 m view depth (Art 9, p.27).
  2. Provide the plot's municipal Planning/Zoning sheet to lift the 4 LOCAL ZONING items —
     without it, BCR, FAR, height, floors, and setbacks cannot be evaluated (they are not
     set by the Building Code).
  3. Provide FAR-counted residential area and stall layout to close the NEEDS INFO items.
```

**This is a design-stage screen, not a legal certification.** It does not replace the municipality, a
licensed engineer/architect, the official Gazette, or the plot's zoning sheet. Every Building-Code value
cited above is `OCR — VERIFY` and must be confirmed against the Gazette of Law 646/2004.
