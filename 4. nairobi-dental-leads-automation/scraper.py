import pandas as pd
import time
import random
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class NairobiDentalTitan:
    def __init__(self):
        options = Options()
        # options.add_argument("--headless") 
        options.add_argument("--window-size=1920,1080")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
        
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.all_urls = set()
        self.results = []

    def collect_urls(self, query):
        print(f"[*] Scanning Area: {query}...")
        url = f"https://www.google.com/maps/search/{query.replace(' ', '+')}+Nairobi+Kenya"
        self.driver.get(url)
        
        try:
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "hfpxzc")))
            
            panel = self.driver.find_element(By.XPATH, '//div[@role="feed"]')
            # Scroll tetap 20 kali agar semua klinik di sub-area terambil
            for _ in range(20): 
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', panel)
                time.sleep(1.2)
            
            elements = self.driver.find_elements(By.CLASS_NAME, "hfpxzc")
            for el in elements:
                link = el.get_attribute("href")
                if link: self.all_urls.add(link)
            print(f"[+] Total URLs found so far: {len(self.all_urls)}")
        except Exception:
            print(f"[!] No more new leads in this area.")

    def extract_details(self):
        print(f"[*] Starting deep extraction of {len(self.all_urls)} leads...")
        for index, url in enumerate(list(self.all_urls)):
            try:
                self.driver.get(url)
                time.sleep(6)

                name, phone, website, address = "N/A", "N/A", "N/A", "N/A"

                try:
                    name = self.driver.find_element(By.TAG_NAME, "h1").text
                except: pass

                phone_selectors = [
                    '//button[contains(@aria-label, "Phone")]',
                    '//button[contains(@data-item-id, "phone:tel")]',
                    '//div[contains(@class, "fontBodyMedium")]/div[contains(text(), "+254")]'
                ]
                for selector in phone_selectors:
                    try:
                        el = self.driver.find_element(By.XPATH, selector)
                        val = el.get_attribute("data-value") or el.text
                        if val and any(char.isdigit() for char in val):
                            phone = val
                            break
                    except: continue

                try:
                    website = self.driver.find_element(By.XPATH, '//a[@data-item-id="authority"]').get_attribute("href")
                except: pass

                try:
                    address = self.driver.find_element(By.XPATH, '//button[contains(@data-item-id, "address")]').text
                except: pass

                whatsapp_link = "N/A"
                if phone != "N/A":
                    clean_phone = "".join(filter(str.isdigit, phone))
                    if clean_phone: whatsapp_link = f"https://wa.me/{clean_phone}"

                self.results.append({
                    "Clinic Name": name,
                    "Phone Number": phone,
                    "WhatsApp Link": whatsapp_link,
                    "Website": website,
                    "Address": address
                })
                print(f"[{index+1}/{len(self.all_urls)}] Extracted: {name} | Phone: {phone}")

                if (index + 1) % 10 == 0: self.save_to_excel(temp=True)

            except Exception as e:
                continue

    def save_to_excel(self, temp=False):
        if not self.results: return
        df = pd.DataFrame(self.results)
        df.drop_duplicates(subset=['Clinic Name'], inplace=True)
        # Nama file diupdate agar sesuai target 800
        filename = "Nairobi_Dental_800_Final.xlsx" if not temp else "Nairobi_Backup_800.xlsx"
        df.to_excel(filename, index=False)

if __name__ == "__main__":
    bot = NairobiDentalTitan()
    try:
        # STRATEGI 800 LEADS: Menambah area spesifik dan variasi keyword
        # Kami menyisir sub-distrik Nairobi lebih detail
        sub_areas = [
            "Westlands", "Kilimani", "Karen", "CBD Nairobi", "Parklands", 
            "Eastleigh", "Langata", "South B", "South C", "Upper Hill", 
            "Kasarani", "Githurai", "Runda", "Gigiri", "Donholm", "Embakasi",
            "Lavington", "Kileleshwa", "Madaraka", "Pangani", "Ngara", 
            "Buruburu", "Roysambu", "Kahawa Sukari", "Zimmerman", "Utawala"
        ]
        
        # Variasi kata kunci agar Google Maps mengeluarkan data yang berbeda
        keywords = ["Dental Clinic", "Dentist", "Dental Surgery", "Orthodontist"]

        for area in sub_areas:
            for kw in keywords:
                bot.collect_urls(f"{kw} {area}")
                # Jika sudah mencapai 1000 URL unik, kita stop kumpulkan link dan mulai ekstrak
                # (Biasanya dari 1000 URL, setelah difilter akan jadi 800-an data bersih)
                if len(bot.all_urls) >= 1000:
                    break
            if len(bot.all_urls) >= 1000:
                break
        
        if len(bot.all_urls) > 0:
            bot.extract_details()
            bot.save_to_excel()
            print("\n[FINISH] Berhasil mengumpulkan data. Cek file Nairobi_Dental_800_Final.xlsx")
        else:
            print("[!] Gagal mengumpulkan URL.")
    finally:
        bot.driver.quit()
