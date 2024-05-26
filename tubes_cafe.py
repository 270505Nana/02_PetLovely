# Daftar makanan dan minuman
daftar_makanan = """
|==============================================|
|              Pilih Menu Makanan              |
|==============================================|
| 1. Nasi Goreng                    Rp 25.000  |
| 2. Mie Goreng Jawa                Rp 25.000  |
| 3. Rice Bowl Chicken Teriyaki     Rp 30.000  |
| 4. Rice Bowl Beef Bulgogi         Rp 35.000  |
| 5. Rice Bowl Chicken Katsu Curry  Rp 30.000  |
| 6. Pasta Aglio Olio               Rp 40.000  |
|==============================================|
"""

daftar_minuman = """
|===============================|
|      Pilih Menu Minuman       |
|===============================|
| 1. Hot Chocolate  Rp 30.000   |
| 2. Frappuccino    Rp 40.000   |
| 3. Macchiato      Rp 25.000   |
| 4. Latte          Rp 30.000   |
| 5. Matcha Latte   Rp 24.000   |
|===============================|
"""

# Menampilkan daftar makanan dan minuman
print("|==============================================|")
print("|         Mesin Kasir Cafe Cerita Kopi         |")
print("|==============================================|")
print(daftar_makanan)
print(daftar_minuman)

# Inisialisasi total_makanan sebelum loop
total_makanan = 0

# Inisialisasi total_minum sebelum loop
total_minum = 0

# List untuk menyimpan pesanan makanan dan minuman

pesanan_makanan = []
pesanan_minuman = []

# Loop untuk meminta pesanan makanan
while True:
    menu_makanan = int(input("Pilih Menu (1-6) atau masukkan 0 jika sudah selesai memilih makanan: "))
    if menu_makanan == 0: #piliham_treatment
        break

    jumlah_porsi = int(input("Berapa Porsi: "))

    if 1 <= menu_makanan <= 6: #piliham_treatment
        harga = [25000, 25000, 30000, 35000, 30000, 40000][menu_makanan - 1]
        nama_makanan = ["Nasi Goreng", "Mie Goreng Jawa", "Rice Bowl Chicken Teriyaki", "Rice Bowl Beef Bulgogi", "Rice Bowl Chicken Katsu Curry", "Pasta Aglio Olio"][menu_makanan - 1]
        total_makanan += harga * jumlah_porsi
        pesanan_makanan.append((nama_makanan, jumlah_porsi, harga * jumlah_porsi))
    else:
        print("Pilihan tidak valid.")

# Loop untuk meminta pesanan minuman
while True:
    menu_minuman = int(input("Pilih Menu (1-5) atau masukkan 0 jika sudah selesai memilih minuman: "))
    if menu_minuman == 0:
        break

    jumlah_gelas = int(input("Berapa Gelas: "))

    if 1 <= menu_minuman <= 5:
        harga_minuman = [30000, 40000, 25000, 30000, 24000][menu_minuman - 1]
        nama_minuman = ["Hot Chocolate", "Frappuccino", "Macchiato", "Latte", "Matcha Latte"][menu_minuman - 1]
        total_minum += harga_minuman * jumlah_gelas
        pesanan_minuman.append((nama_minuman, jumlah_gelas, harga_minuman * jumlah_gelas))
    else:
        print("Pilihan tidak valid.")

# Cetak Struk Pembelian
print("\n|=====================================|")
print("|        Struk Pembelian        |")
print("|=======================================|")
print("|           Makanan             |")
print("|=======================================|")
for makanan in pesanan_makanan:
    print(f"|{makanan[0]:<30} {makanan[1]:<10} {makanan[2]:>10}|")
print("|           Minuman             |")
print("|===============================|")
for minuman in pesanan_minuman:
    print(f"|{minuman[0]:<30} {minuman[1]:<10} {minuman[2]:>10}|")
print("|===============================|")
print(f"| Total                      {total_makanan + total_minum:>20} |")
print("|===============================|")