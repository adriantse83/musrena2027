from openpyxl import load_workbook
from pathlib import Path

DATA_FILE = Path("../data/daftar_musrena27.xlsx")
TEMPLATE_FILE = Path("template_gampong.html")
OUTPUT_DIR = Path("../hotspot")

print("Template :", TEMPLATE_FILE)
print("Data     :", DATA_FILE)
print("Output   :", OUTPUT_DIR)

print("\nGenerator ini adalah pondasi proyek.")
print("Tahap berikutnya akan ditambahkan:")
print("- Membaca Excel")
print("- Mengelompokkan per gampong")
print("- Menghasilkan satu HTML untuk setiap gampong")
