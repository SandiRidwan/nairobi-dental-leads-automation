# Google Maps Lead Scraper: Nairobi Dental Clinics

A high-performance Python automation tool designed to extract and clean B2B leads from Google Maps. 

## Features
- **Deep Grid Search**: Scans 26+ sub-districts to bypass Google Maps search limits.
- **Automated Cleaning**: Professional post-processing to remove UTF-8 artifacts (like location icons) and standardize text formatting.
- **WhatsApp Integration**: Automatically generates direct WhatsApp API links for lead outreach.
- **Deduplication**: Ensures data uniqueness based on phone number verification.

## Tech Stack
- **Python 3.x**
- **Selenium**: Browser automation.
- **Pandas**: Data engineering and Excel export.
- **Regex**: Advanced text cleaning and symbol removal.

## How to Use
1. Install dependencies: `pip install -r requirements.txt`
2. Run the scraper: `python src/scraper.py`
3. Run the cleaner: `python src/cleaner.py`

## Sample Output
The tool generates a structured Excel file including:
- Clinic Name
- Verified Phone Number
- WhatsApp Direct Link
- Physical Address
- Website URL
