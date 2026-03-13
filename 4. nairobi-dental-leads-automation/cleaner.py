
import pandas as pd

def final_polish_cleaning(file_name):
    # 1. Load data
    df = pd.read_excel(file_name)
    
    # 2. Fungsi untuk menghapus simbol aneh (non-ASCII)
    # Simbol  termasuk karakter unik yang akan dibersihkan oleh regex ini
    def remove_junk(text):
        if pd.isna(text) or text == 'N/A':
            return 'N/A'
        # Menghapus karakter non-ASCII (seperti simbol icon lokasi)
        return str(text).encode("ascii", "ignore").decode("ascii").strip()

    # 3. Terapkan pembersihan ke kolom Address dan Phone Number
    print("[*] Membersihkan simbol icon dari kolom Address...")
    df['Address'] = df['Address'].apply(remove_junk)
    
    print("[*] Membersihkan simbol icon dari kolom Phone Number...")
    df['Phone Number'] = df['Phone Number'].apply(remove_junk)

    # 4. Tambahan: Pastikan nomor telepon tidak mengandung spasi berlebih atau karakter aneh
    # Terutama jika simbol tersebut nempel di depan nomor telepon
    df['Phone Number'] = df['Phone Number'].str.replace(r'[^\d+ -]', '', regex=True)

    # 5. Simpan ke file baru yang benar-benar bersih
    output_name = "Nairobi_Dental_800_SUPER_CLEAN.xlsx"
    df.to_excel(output_name, index=False)
    
    print(f"\n[+] SELESAI! Simbol  telah dihapus.")
    print(f"[+] File bersih tersimpan di: {output_name}")

if __name__ == "__main__":
    # Ganti dengan nama file terakhirmu
    final_polish_cleaning("Nairobi_Dental_800_Final.xlsx")



    
    

import pandas as pd
import os
import re

def final_polish(filename):
    # 1. Cek keberadaan file
    if not os.path.exists(filename):
        # Tambahkan ekstensi jika lupa
        if not filename.endswith('.xlsx'):
            filename += '.xlsx'
        
        if not os.path.exists(filename):
            print(f"[!] File '{filename}' tetap tidak ditemukan. Cek folder kamu!")
            return

    print(f"[*] Memproses file: {filename}")
    
    # 2. Load data
    df = pd.read_excel(filename)
    
    # 3. Fungsi Master Cleaner (Menghapus  dan karakter sampah)
    def clean_junk(text):
        if pd.isna(text) or text == 'N/A':
            return 'N/A'
        # Menghapus simbol non-ASCII () dan merapikan spasi
        cleaned = str(text).encode("ascii", "ignore").decode("ascii").strip()
        # Menghapus double spasi jika ada
        cleaned = re.sub(' +', ' ', cleaned)
        return cleaned

    # 4. Terapkan ke semua kolom yang rawan simbol (Address, Phone, Clinic Name)
    target_columns = ['Clinic Name', 'Phone Number', 'Address']
    for col in target_columns:
        if col in df.columns:
            print(f"[*] Membersihkan kolom: {col}")
            df[col] = df[col].apply(clean_junk)
            
            # Khusus nama klinik dan alamat, buat jadi Huruf Kapital di awal kata (Proper Case)
            if col in ['Clinic Name', 'Address']:
                df[col] = df[col].str.title()

    # 5. Hilangkan duplikat terakhir (berdasarkan Phone Number)
    df.drop_duplicates(subset=['Phone Number'], keep='first', inplace=True)

    # 6. Simpan ke file yang benar-benar siap dikirim ke klien
    output_name = "Nairobi_Dental_800_READY_TO_SELL.xlsx"
    df.to_excel(output_name, index=False)
    
    print("-" * 35)
    print(f"[+] SELESAI! Data sudah 100% bersih.")
    print(f"[+] Total leads: {len(df)}")
    print(f"[+] Simbol icon lokasi () telah dibuang.")
    print(f"[+] File siap jual: {output_name}")

if __name__ == "__main__":
    # Jalankan pembersihan pada file target
    final_polish("Nairobi_Dental_800_SUPER_CLEAN")