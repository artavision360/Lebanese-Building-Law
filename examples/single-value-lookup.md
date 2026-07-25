# Example — single-value lookups
# lebanese-building-law skill · demonstrates retrieval routing, citation, verification & zoning labels

> These examples demonstrate **workflow behavior only**. Every legal value is drawn from the existing
> verified references with its Article/page/figure and its `OCR — VERIFY` status intact. No value was
> invented. They show three cases: a GENERAL code value, a ZONE-SPECIFIC parameter, and a NOT-FOUND case.

---

## Example 1 — GENERAL Building-Code value (answerable)

**User:** "What's the maximum parking-ramp slope for a 1,200 m² plot?"

**Routing:** parking/ramps → Art 15 → Tier 1 `QUICK_MATRIX` row "Ramp max slope". Plot > 800 m².

**Answer:**

> **Requirement**
> Maximum garage-ramp slope for a property larger than 800 m².
>
> **Value**
> ≤ 20 % — `OCR — VERIFY`
>
> **Source**
> Article 15 · ثانياً-3-1 · p.62 · Fig 94
>
> **Verification Status**
> `OCR — VERIFY` (Building-Code value; confirm against the official Gazette of Law 646/2004)
>
> **Zoning Status**
> `GENERAL REQUIREMENT` — set by the Building Code, not plot-specific.
>
> *(≤800 m² plots use ≤ 22 %, Art 15 · p.65 · Fig 103. Ramp width, turn radii, and clearances are in the
> same Article — escalate to the Master/Ledger if the full ramp geometry is needed.)*

---

## Example 2 — ZONE-SPECIFIC parameter (must NOT be answered with a number)

**User:** "What's the maximum FAR / building height I can use on this Beirut plot?"

**Routing:** FAR / height → these are **zone-specific**, not fixed by the Code → `PLANNING_ZONING_WORKFLOW`.

**Answer:**

> **Requirement**
> Maximum FAR (عامل الاستثمار العام) and maximum building height for the specific plot.
>
> **Value**
> Not set by the Building Code. The decree defines *how* exploitation is computed and *what* is excluded
> (Article 12) and the gabarit/height *method* (Articles 7 & 11) — but the **numeric FAR and height limit
> come from the plot's municipal Planning sheet**, which has not been provided.
>
> **Source**
> Method: Article 12 (exploitation) · Article 7 (gabarit) · Article 11 (height datum) — `OCR — VERIFY`.
> The plot's FAR/height value: municipal Planning/Zoning sheet.
>
> **Verification Status**
> Method `OCR — VERIFY`. Plot value: not in sources.
>
> **Zoning Status**
> `LOCAL ZONING VERIFICATION REQUIRED` — provide the plot's Planning/Zoning sheet (or its zone
> classification) and I can apply the Code's exploitation/height *method* to it. I will not assume a
> value from the zone type or from typical practice.

---

## Example 3 — NOT FOUND (absent from sources)

**User:** "What's the minimum distance between a swimming pool and the property boundary?"

**Routing:** searched Art 2 (site), Art 9 (courtyards/setback-view), Art 13 (structures in setback) — no
pool-to-boundary rule is present in the references.

**Answer:**

> **Requirement**
> Minimum setback of a swimming pool from the property boundary.
>
> **Value**
> `NOT FOUND IN CURRENT VERIFIED SOURCES`
>
> **Source**
> Not present in Articles 1–20 or Figures 1–115 of the current references.
>
> **Verification Status / Zoning Status**
> Cannot be answered from the verified sources. This may be governed by the plot's municipal
> regulations (`LOCAL ZONING VERIFICATION REQUIRED`) or by a provision not captured in the OCR. I will
> not invent a value. Recommend checking the plot's zoning sheet and the official Gazette.
