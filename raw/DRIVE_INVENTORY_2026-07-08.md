# Google Drive Inventory — UAC & TNR

**Date:** 2026-07-08  
**Source:** GAPI Drive search across Commander's shared folders  
**Total files discovered:** 122 (including folders)

---

## Category Summary

| Category | Count | Description |
|----------|-------|-------------|
| **tax-legal** | 12 | IRS docs, EIN, Articles of Incorporation, PA filings, MSA |
| **grant** | 20 | EDEN Network grant sections, Bradford United Way, FVF, Fund-a-Farmer, FruitGuys |
| **education/botany** | 8 | Aquaponics 101-104 slides, course description, lesson plan review |
| **farm-operations** | 8 | Volunteer roster, inventory, goat registrations (PDFs), animal records |
| **marketing** | 6 | Marketing plans, Giving Tuesday docs, flyer, social assets |
| **admin** | 4 | LSP draft, GCP service account JSON, Work Order |
| **media/images** | ~45 | Social photos, EDEN Social Photos, content images, plant ID photos |
| **other** | ~19 | Business plans, templates, zip files, EDEN folder structures |

---

## FILES INGESTED (Text/CSV downloaded to eden-wiki/raw/)

### grants/
| File | Source |
|------|--------|
| PA_Ag_EDEN_Network_sec8910_impl_budget_team.md | Drive |
| PA_Ag_EDEN_Network_sec1_exec_summary.md | Drive |
| PA_Ag_EDEN_Network_sec2_3_challenge_solution.md | Drive |
| PA_Ag_EDEN_Network_sec4_technical.md | Drive |
| PA_Ag_EDEN_Network_sec567_veteran_impact_partner.md | Drive |
| PA_Ag_Innovation_EDEN_Network_COMPLETE.md | Drive |
| PA_Ag_Innovation_EDEN_Network_COMPLETE_v2.md | Drive (duplicate) |
| Bradford_United_Way_2026.md | Drive |
| FVF_Essay_FINAL.md | Drive |
| FVF_Essay_FINAL_v2.md | Drive (duplicate) |
| fund_a_farmer_FINAL.md | Drive |
| fruitguys_REAL_APPLICATION.md | Drive |
| GRANT_WORKFLOW.md | Drive |

### business/
| File | Source |
|------|--------|
| TNR_Business_Plan_20260131.md | Drive |
| TNR_Business_Plan_20260131_v2.md | Drive (duplicate) |
| TNR_Bridge_Plan_v1.csv | Drive (GSheet export) |
| TNR_Bridge_Plan_v2.csv | Drive (GSheet export) |

### marketing/
| File | Source |
|------|--------|
| 11.26.23_UAC_GivingTuesday_1Page.txt | Drive (GDoc export) |
| 11.15.23_UAC_Checklist_GivingTuesdayCampaign.csv | Drive (GSheet export) |

### admin/
| File | Source |
|------|--------|
| 10.30.23_UAC_LSP_Draft.txt | Drive (GDoc export) |
| project-eden-484316-da2d0c20d6c1.json | Drive |

### farm-operations/
| File | Source |
|------|--------|
| UAC_Volunteer_Day_Roster.csv | Drive (GSheet export) |

### inventory/
| File | Source |
|------|--------|
| Inventory_20231021.xlsx | Drive |

---

## BINARY FILES (not ingested — logged only)

### PDFs (tax/legal)
- `Articles of Incorporation.pdf` — Business Docs
- `EIN Docs.pdf` — Business Docs
- `IRS Docs 2.pdf` — Business Docs
- `IRS Form 1023.pdf` — Business Docs
- `IRS determination .pdf` — Business Docs
- `PA Filing.pdf` — Business Docs
- `PA Filings 2.pdf` — Business Docs
- `Notice_from_Secretary_of_State_02-05-2020_at_22-18-55.pdf` — Business Docs
- `Urban Ark Conservation Mktg Plan 2023.pdf` — Business Docs
- `10.30.23_UAC_MSA_SignedbyQOLA.pdf` — UAC - Shared root

### PDFs (grant/agreements)
- `2025 Agreement - Page 1.pdf` — United Way 2025-2026 Grant
- `2025 Agreement - Page 2 .pdf` — United Way 2025-2026 Grant
- `2025 Agreement - Page 2 (SIGNED).pdf` — United Way 2025-2026 Grant
- `ACH Credit Authorization from Agency to UWBC 2025.pdf` — United Way 2025-2026 Grant
- `ACH Credit Authorization from Agency to UWBC 2025 (SIGNED).pdf` — United Way 2025-2026 Grant
- `Needs Assessment book 08212024.pdf` — United Way 2025-2026 Grant
- `Urban Ark Conservation 5.12.2025.docx` — United Way 2025-2026 Grant
- `form_schedule_f_2025_skeleton.pdf` (x3 copies) — TNR tax filings

### PDFs (animals/goat registrations)
- `Mabel.pdf` — Goat Registrations
- `Belle.pdf` — Goat Registrations
- `Tree Blossom.pdf` — Goat Registrations
- `Storm.pdf` — Goat Registrations
- `Zoey.pdf` — Goat Registrations
- `Manaaki.pdf` — Goat Registrations

### PDFs (education)
- `UrbanArkConservation Course Description.pdf` — Aquaponics
- `Lesson Plan Review.pdf` — Aquaponics

### PPTX (education)
- `101 Slideshow.pptx` — Aquaponics
- `UAC Aquaponics 102 .pptx` — Aquaponics
- `UAC Aquaponics 103.pptx` — Aquaponics
- `UAC Aquaponics 104.pptx` — Aquaponics

### DOCX
- `Urban Ark Conservation, Inc., Work Order No. 1, (2024)draftv.1.docx` — UAC - Shared root
- `Mktg Plan 2023.docx` — Business Docs
- `Urban Ark Conservation 5.12.2025.docx` — United Way 2025-2026 Grant

### Images (social media / content)
- ~45 images across: EDEN Social Photos, Content, EDEN_Plant_ID, EDEN_Social Photos
- Includes: animal photos (Tree Blossum, Ozzy, Forrest, Pango, Cora, Oakley, Sahara, etc.), flyers, plant ID photos
- `USED_UAC Flyer.png` — UAC - Shared root

### Archives
- `fwdhomegrownbyheroescertification.zip` — UAC - Shared root
- `United Way of Bradford County 2025-2026 Grant .zip` — United Way 2025-2026 Grant

### Google-native (no text export done)
- `UAC Volunteer Day — Roster & Analytics` — GSheet (exported as CSV instead)
- `11.15.23_UAC_Checklist_GivingTuesdayCampaign` — GSheet (exported as CSV)
- `TNR Bridge Plan - Template` (x2) — GSheets (exported as CSV)

---

## Folder Structure

```
UAC - Shared/
├── Aquaponics/
│   ├── 101 Slideshow.pptx
│   ├── UAC Aquaponics 102.pptx
│   ├── UAC Aquaponics 103.pptx
│   ├── UAC Aquaponics 104.pptx
│   ├── UrbanArkConservation Course Description.pdf
│   └── Lesson Plan Review.pdf
├── Business Docs/
│   ├── 10.30.23_UAC_LSP_Draft (GDoc)
│   ├── Articles of Incorporation.pdf
│   ├── EIN Docs.pdf
│   ├── IRS Docs 2.pdf
│   ├── IRS Form 1023.pdf
│   ├── IRS determination.pdf
│   ├── PA Filing.pdf
│   ├── PA Filings 2.pdf
│   ├── Notice_from_Secretary_of_State.pdf
│   ├── Mktg Plan 2023.docx
│   └── Urban Ark Conservation Mktg Plan 2023.pdf
├── Content/ (9 images)
├── EDEN Social Photos/ (social media images)
├── Goat Registrations/ (6 PDFs)
├── Inventory Docs/ (1 xlsx)
├── Marketing/ → 2023_GivingTuesday/
│   ├── 11.26.23_UAC_GivingTuesday_1Page (GDoc)
│   └── 11.15.23_UAC_Checklist_GivingTuesdayCampaign (GSheet)
├── Sponsors/ (empty)
├── Wishlist/ (empty)
├── USED_UAC Flyer.png
├── 10.30.23_UAC_MSA_SignedbyQOLA.pdf
├── Urban Ark Conservation Work Order.docx
└── fwdhomegrownbyheroescertification.zip

EDEN_Grants/
├── Bradford_United_Way_2026.md
├── FVF_Essay_FINAL.md
├── TNR_Business_Plan_20260131.md
├── PA_Ag_Innovation_EDEN_Network_COMPLETE.md
├── 2026-01-31/ (12 .md grant section files)
├── United Way Grants/ → 2025/ → United Way of Bradford County 2025-2026 Grant/
│   ├── 2025 Agreements (PDFs)
│   ├── ACH Authorizations (PDFs)
│   ├── Needs Assessment book.pdf
│   ├── Urban Ark Conservation 5.12.2025.docx
│   └── United Way ... Grant .zip

EDEN_Plant_ID/ (4 plant ID photos)
EDEN_Livestock/ (empty)
EDEN_Media/ (empty)
EDEN_Reports/ (empty)
EDEN_Outbox/ (empty)
EDEN_Backups/ (empty)
EDEN_Inbox/ (GCP service account JSON)
EDEN_Datasets/ (empty)
EDEN_Goat_Training/ (empty)
EDEN_Documents/ (empty)
```

## Summary

- **Total unique files in Drive:** ~65 files (plus ~45 images, 12 folders)
- **Text files ingested into eden-wiki/raw/:** 24 files (13 markdown, 4 CSV, 2 plain text, 1 JSON, 1 xlsx, plus pre-existing 64 doctrine/operator files)
- **Categories represented:** grants, business, marketing, admin, farm-operations, inventory, tax-legal, education/botany, media/images
- **Binary files logged (not ingested):** ~30 PDFs, 4 PPTX, 3 DOCX, ~45 images, 2 ZIPs
- **Deduplication:** Several files had duplicate copies in Drive (TNR Business Plan x2, EDEN Network COMPLETE x2, FVF Essay x2, TNR Bridge Plan x2, form_schedule_f x3) — only one copy ingested, duplicates noted
