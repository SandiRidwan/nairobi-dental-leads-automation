# 🏥 Google Maps Lead Scraper: Nairobi Dental Clinics
**High-Precision B2B Extraction & Automated Lead Enrichment**

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Automation-Selenium-red.svg?style=for-the-badge&logo=selenium)
![Market](https://img.shields.io/badge/Market-Nairobi_Kenya-green.svg?style=for-the-badge)
![Data](https://img.shields.io/badge/Clean-UTF--8_Safe-brightgreen.svg?style=for-the-badge)

---

## 📌 Project Overview
This specialized automation tool is engineered to penetrate the healthcare market in **Nairobi, Kenya**. It doesn't just scrape data; it performs a **Deep Grid Search** across 26+ sub-districts (Westlands, Kilimani, Karen, etc.) to bypass Google Maps' visibility limits, ensuring 100% market coverage.

---

## ⚡ The Extraction Engine

### 🛰️ Deep Grid Search Logic
Google Maps typically limits search results to ~200 entries. This bot executes a recursive sub-district scan to ensure no dental clinic is missed, regardless of its ranking.

### 🧹 Advanced Text Sanitization (The Cleaner)
Built-in **Regex-powered engines** to scrub raw data:
* Removes messy UTF-8 artifacts (Location pins 📍, Phone icons 📞).
* Standardizes address formats.
* Validates Kenyan phone numbers (+254).

### 💬 WhatsApp Outreach Integration
Automatically generates **Direct WhatsApp API Links** for every lead, allowing sales teams to initiate contact with one click.

---

## 🛠️ Tech Stack & Architecture

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Automation** | Selenium WebDriver | Browser interaction & data harvesting |
| **Engineering** | Pandas | Data cleaning & Excel orchestration |
| **Sanitization** | Regex (re) | UTF-8 artifact removal & text formatting |
| **Validation** | Deduplication Logic | Phone-based uniqueness verification |

---

## 📂 Project Structure

```text
├── src/
│   ├── scraper.py         # The Harvester: Scans G-Maps Grid
│   └── cleaner.py         # The Polisher: Symbol removal & WA links
├── data/
│   └── nairobi_dentists.xlsx  # Final clean output
├── requirements.txt
└── README.md
