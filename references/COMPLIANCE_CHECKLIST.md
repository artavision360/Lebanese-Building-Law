# PROJECT COMPLIANCE CHECKLIST (reusable template)
# lebanese-building-law skill

> Instantiate this per project. Fill the **Project Value** column from the design; fill **Legal
> Reference** from the primary references; set **Status** from the legend. **Do not delete rows for
> missing data** — mark them `NEEDS INFO` or `LOCAL ZONING VERIFICATION REQUIRED` so gaps stay visible.
>
> **Result states:**
> `PASS` · `FAIL` · `NEEDS INFO` · `SOURCE VERIFICATION REQUIRED` · `LOCAL ZONING VERIFICATION REQUIRED`
>
> Every Building-Code value is `OCR — VERIFY`. Zone/plot-specific parameters (BCR, FAR, height, floors,
> setbacks, zoning, land use) are **not** set by the Code — see `PLANNING_ZONING_WORKFLOW.md`.
> **This checklist is a design-stage screen, not a legal certification.**

---

## 0 · Project & plot identity

| Item | Value | Status |
|---|---|---|
| Project name / type | … | |
| Location (country / municipality) | … | Lebanon? if not → these rules do not apply |
| Plot area (مساحة العقار) | … m² | NEEDS INFO if absent |
| Road width(s) (عرض الطريق) | … m | NEEDS INFO if absent |
| Natural ground / topography | … | NEEDS INFO if absent |

## 1 · Zoning inputs (zone/plot-specific — from municipal Planning/Zoning sheet)

> If the project's ارتفاع وتخطيط / planning/zoning document is provided, fill this section from the
> **applicable Zone** via `PROJECT_ZONING_INTAKE.md` and mark each cell **`PROJECT ZONING (as provided)`**
> (confirm with the municipality). If it is **not** provided, each cell stays
> **`LOCAL ZONING VERIFICATION REQUIRED`**. These values are project-scoped — never a universal rule.

| Requirement | Legal / Doc Reference | Project Value | Status |
|---|---|---|---|
| Zone classification | Municipal zoning sheet | … | LOCAL ZONING VERIFICATION REQUIRED if unsupplied |
| Permitted land use | Zoning sheet | … | LOCAL ZONING VERIFICATION REQUIRED if unsupplied |
| BCR — معدل الاستثمار السطحي | Planning sheet | … | LOCAL ZONING VERIFICATION REQUIRED if unsupplied |
| FAR — عامل الاستثمار العام | Planning sheet | … | LOCAL ZONING VERIFICATION REQUIRED if unsupplied |
| Max building height | Planning sheet | … | LOCAL ZONING VERIFICATION REQUIRED if unsupplied |
| Max number of floors | Planning sheet | … | LOCAL ZONING VERIFICATION REQUIRED if unsupplied |
| Front / rear / side setbacks | Planning sheet | … | LOCAL ZONING VERIFICATION REQUIRED if unsupplied |
| Municipality special conditions | Municipal report | … | NEEDS INFO if unsupplied |

## 2 · Site works (GENERAL — Building Code)

| Requirement | Value (`OCR — VERIFY`) | Ref | Project | Status |
|---|---|---|---|---|
| Retaining wall max height | 3.00 m | Art 2 · p2–3 | … | |
| Support wall (outside / in setback) | 3.50 / 2.00 m | Art 2 · p4 | … | |
| Sanad wall max | 3.50 m | Art 2 · p5 | … | |
| Backfill height (outside / in setback) | 3.50 / 2.00 m | Art 12 · p42 | … | |
| Backfill slope (below road) | 5 % | Art 2 · p7 | … | |
| Land-grading staging threshold | 3,000 m² | Art 2 · p4 | … | |

## 3 · Envelope & height (GENERAL method; height *limit* is zone-specific)

| Requirement | Value (`OCR — VERIFY`) | Ref | Project | Status |
|---|---|---|---|---|
| Gabarit vertical line | 2.5 × road width (min 15 m) | Art 7 · p19 | … | |
| Gabarit inclined line | 2/5 slope | Art 7 · p19 | … | |
| Height datum | 1 m above lowest facade pt | Art 11 · p35 | … | |
| Floor-count trigger | free height > 5.75 m | Art 11 · p36 | … | |
| Max height / floors (the numeric limit) | zone-specific | Planning sheet | … | LOCAL ZONING VERIFICATION REQUIRED |

## 4 · Exploitation / FAR (GENERAL method; the ratio is zone-specific)

| Requirement | Value (`OCR — VERIFY`) | Ref | Project | Status |
|---|---|---|---|---|
| Balcony exclusion (general / per floor) | 20 / 25 % | Art 12 · p38 | … | |
| Buried basement (parking/storage/mech) | excluded from FAR/BCR | Art 12 · p44 | … | |
| Buried basement other uses | ≤ 50 % cap | Art 12 · p44 | … | |
| Stair + elevator excluded area | 20 m² (+6 per extra) | Art 12 · p50–51 | … | |
| Technical floor | clear 1.90 m | Art 12 · p52 | … | |
| The FAR / BCR ratio itself | zone-specific | Planning sheet | … | LOCAL ZONING VERIFICATION REQUIRED |

## 5 · Basements (GENERAL)

| Requirement | Value (`OCR — VERIFY`) | Ref | Project | Status |
|---|---|---|---|---|
| Buried basement roof above ground | ≤ 1 m | Art 12 · p41 · Fig 62 | … | |
| Exposed basement ceiling / clear height | 3.00 / 3.50 m | Art 12 · p45 · Fig 73 | … | |
| Exposed basement backfilled facade | ≥ 60 % | Art 12 · p45–46 · Fig 74 | … | |

## 6 · Parking, ramps, circulation (GENERAL)

| Requirement | Value (`OCR — VERIFY`) | Ref | Project | Status |
|---|---|---|---|---|
| Parking count — housing | 1 / 100 m² (max 5) | Art 15 · p58 | … | |
| Parking count — other uses | per Art 15 table | Art 15 · p59–60 | … | SOURCE VERIFICATION REQUIRED (restaurant ratio disputed) |
| Stall dimensions | 5.20×1.80 / 4.80×1.70 m | Art 15 · p61/64 · Fig 93/102 | … | |
| Ramp max slope | 20 % (>800 m²) / 22 % (≤800) | Art 15 · p62/65 · Fig 94/103 | … | |
| Ramp width | 3.50 / 5.25 m (≤30 / >30 cars) | Art 15 · p62 | … | |
| Ramp turn radii | 4.50 / 8 m inner/outer | Art 15 · p63 · Fig 98 | … | |
| Aisle width | 4 / 5 / 6 m (parallel/45°/90°) | Art 15 · p63–64 · Fig 100 | … | |

## 7 · Stairs, clear heights (GENERAL)

| Requirement | Value (`OCR — VERIFY`) | Ref | Project | Status |
|---|---|---|---|---|
| Main stair min clear width | 1.10 m | Art 12 · p50 | … | |
| Corridor to apartments | 1.40 m | Art 12 · p50 | … | |
| Clear height — habitable | 2.80 m (2.40 sloped avg) | Art 17 · p74 · Fig 111 | … | |
| Clear height — basement/garage/Pilotis/service | 2.20 m | Art 17 · p74 · Fig 112 | … | |
| Clear height — WC / corridor | 2.00 m | Art 17 · p74 | … | |
| Max clear height | 5.75 m | Art 17 · p76 | … | |

## 8 · Light, view, ventilation (GENERAL)

| Requirement | Value (`OCR — VERIFY`) | Ref | Project | Status |
|---|---|---|---|---|
| View distance (habitable room) | ≥ 4.50 m | Art 9 · p27 · Fig 37 | … | |
| Room depth | ≤ 5 × clear height | Art 9 · p27–28 · Fig 38 | … | |
| Legal courtyard | ≥ 30 m², 4.50×5.50 m | Art 9 · p30 · Fig 31 | … | |
| منور (light shaft) min | 1.50 m² / width 0.75 m | Art 9 · p31 · Fig 46 | … | |

## 9 · Projections & roof (GENERAL)

| Requirement | Value (`OCR — VERIFY`) | Ref | Project | Status |
|---|---|---|---|---|
| Balcony projection | 0 (<9 m road) / 1.05 m (≥9 m) | Art 8 · p24 | … | |
| Cornice projection | 1/8 road width → 3.00 m max | Art 8 · p24 · Fig 32 | … | |
| Brise-soleil / decoration | ≤ 0.60 m | Art 8 · p24 | … | |
| Tile roof slope / متكأ | ≥ 25° / متكأ ≤ 1 m | Art 12 · p48 · Fig 80 | … | |
| Roof structures height | 3.00 m (≤15 m) / 4.50 m | Art 12 · p51 | … | |

## 10 · Missing information & verification log

| Item | Why needed | Status |
|---|---|---|
| … | … | NEEDS INFO / LOCAL ZONING VERIFICATION REQUIRED |

---

## Verdict block (design-stage screen — NOT a certification)

```
COMPLIANCE SCREEN RESULT
------------------------------------------------------
Rows PASS:                        [#]
Rows FAIL:                        [#]
Rows NEEDS INFO:                  [#]
Rows SOURCE VERIFICATION REQUIRED:[#]
Rows LOCAL ZONING VERIFICATION REQUIRED:[#]

Overall:  [ ] SCREEN CLEAR (design-stage) — pending Gazette + zoning verification
          [ ] BLOCKED — resolve LOCAL ZONING / NEEDS INFO items first
          [ ] FAIL(S) PRESENT — listed above with Article·page·figure

This is NOT a legal certification and does not replace the municipality,
a licensed engineer/architect, the official Gazette, or the plot's zoning sheet.
Every Building-Code value above is OCR — VERIFY.
```
