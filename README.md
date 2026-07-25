# Lebanese Building Law — Claude Code Skill

A professional Claude Code Skill for Lebanese Building Law, architectural compliance checking, and project-specific Urban Planning & Zoning workflows.

## Overview

This Skill provides a structured regulatory knowledge system for architects working with the Lebanese Building Law.

It combines:

- Lebanese Building Law knowledge
- Architectural compliance checking
- Building-Code parameter lookup
- Article and source-page traceability
- Urban Planning / Zoning workflow
- Project-specific ارتفاع وتخطيط analysis
- BCR / معدل الاستثمار السطحي
- FAR / عامل الاستثمار العام
- Maximum building height
- Maximum number of floors
- Setbacks / تراجعات
- Parking and garage requirements
- Basements
- Building envelope and gabarit
- Architectural regulatory checks
- Source verification and anti-hallucination safeguards

## How It Works

The Skill separates two regulatory layers:

### 1. General Lebanese Building Law

Permanent regulatory knowledge derived from the Lebanese Building Law reference set.

### 2. Project-Specific Planning & Zoning

Planning and zoning values are NOT treated as universal regulations.

For each project, the user can provide the applicable:

- ارتفاع وتخطيط document
- Urban Planning / Zoning sheet
- Zone classification
- Municipal planning document

The Skill extracts the applicable project-specific parameters and combines them with the general Building Law.

```text
GENERAL LEBANESE BUILDING LAW
              +
PROJECT-SPECIFIC PLANNING / ZONING
              ↓
ARCHITECTURAL COMPLIANCE REVIEW
