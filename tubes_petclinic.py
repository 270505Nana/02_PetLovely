# Get user input for owner's name, animal's name, and animal's condition


# jenis hewan
jenis_hewan = """
|==============================================|
|              Pilih Jenis Hewan               |
|==============================================|
| 1. Hewan Anjing                              |
| 2. Hewan Kucing                              |
|==============================================|
"""

#  NO 1
# Menampilkan daftar makanan dan minuman
print("|==============================================|")
print("|              Pet Shop Lovely hart !          |")
print(jenis_hewan)


total_treatment_ajg = 0
total_treatment_cat = 0
# array buat nyimpen treatment yang dipilih, misal cus punya 2 hewan maka akan disimpan dimasing" array
anjing =[]
kucing=[]

def grooming_anjing(jenis_hewan):
    print("|=======================================================|")
    print("|        Pilihan grooming untuk anjing                  |")
    print("|=======================================================|")
    print("|1. Grooming kering                      Rp.40.000      |")
    print("|2. Grooming basic                       Rp.50.000      |")
    print("|3. Grooming shampoo Anti kutu           Rp.60.000      |")
    print("|4. Grooming shampoo Anti jamur          Rp.70.000      |")
    print("|5. Grooming shampoo anti kutu & jamur   Rp.80.000      |")
    print("|6. Grooming shampoo whitening           Rp.100.000     |")
    print("|=======================================================|")

def grooming_cat(jenis_hewan):
    print("|=======================================================|")
    print("|             Pilihan grooming untuk kucing             |")
    print("|=======================================================|")
    print("|1. Grooming kering                      Rp.20.000      |")
    print("|2. Grooming basic                       Rp.25.000      |")
    print("|3. Grooming shampoo Anti kutu           Rp.30.000      |")
    print("|4. Grooming shampoo Anti jamur          Rp.30.000      |")
    print("|5. Grooming shampoo anti kutu & jamur   Rp.60.000      |")
    print("|6. Grooming shampoo whitening           Rp.80.000      |")
    print("|=======================================================|")

def print_nota(reservasi):
#   groomings = [""]
#   total_harga = 0
  print("\n--- Nota Reservasi Grooming ---")
  for idx, data in enumerate(reservasi):
    print("Reservasi", idx + 1)
    print("Nama Pemilik:",nama_pemilik)
    print("Nomor Pemilik:", no_pemilik)
    print("Alamat Pemilik:", alamat_pemilik)
    print("Nama Hewan:", nama_hewan)
    print("Kondisi Hewan:", kondisi_hewan)
#     print("Pilihan Grooming:", groomings[int(data["pilihan_grooming"])-1])
#     harga = calculate_price(data["pilihan_grooming"], data["jenis_hewan"])
#     print("Harga:", harga)
#     total_harga += harga
#   print("Total Harga: Rp", total_harga)
  print("---------------------------------")

# Loop untuk menu anjing
while True:
    jenis_hewan = int(input("Masukkan jenis hewan (1-2):"))

    if jenis_hewan == 0:
        
        # diinput setelah costumer selesai input jenis hewan, banyak hewan, dn treatment yang dipilih.
        nama_pemilik = input("Masukkan nama pemilik hewan: ")
        no_pemilik = input("Masukkan no pemilik hewan: ")
        alamat_pemilik = input("Masukkan alamat pemilik hewan: ")
        # for i in range banyak_hewan
            # loop sebanyak hewannya
        nama_hewan = input("Masukkan nama hewan: ")
        kondisi_hewan = input("Masukkan kondisi hewan: ")
        reservasi = [nama_pemilik,no_pemilik, alamat_pemilik,nama_hewan,kondisi_hewan]
        print_nota(reservasi)
        break

    if (jenis_hewan == 1):
        grooming_anjing(jenis_hewan)
        pilihan_treatment=int(input("Masukkan pilihan treatment (1-6):"))
        # masuk ke kalau milih menu 1 harganya berapa dst.
        banyak_hewan = int(input("Berapa ekor anjing:"))

        if 1 <= pilihan_treatment <= 6:
            # menggunakan array untuk daftar harga dan menunya, abis itu kalau dipilih maka arraynya akan -1
            harga = [40000, 50000, 60000, 70000, 80000, 100000][pilihan_treatment - 1]
            menu_treatment = ["Grooming kering", "Grooming basic", "Grooming shampoo Anti kutu"
                            , "Grooming shampoo Anti jamur", "Grooming shampoo Anti kutu & jamur"
                            , "Grooming shampoo whitening"][pilihan_treatment - 1]
            total_treatment_ajg += harga * banyak_hewan
            anjing.append((menu_treatment, banyak_hewan, harga * banyak_hewan)) 
            print(anjing) #testing apakah data yang dimasukkan tersimpan.
            # untuk menghitung total biayanya
        else:
            print("Pilihan tidak valid.")
    
    if (jenis_hewan == 2):
        grooming_cat(jenis_hewan)
        pilihan_treatment=int(input("Masukkan pilihan treatment (1-6):"))
        # masuk ke kalau milih menu 1 harganya berapa dst.
        banyak_hewan = int(input("Berapa ekor kucing:"))

        if 1 <= pilihan_treatment <= 6:
            # menggunakan array untuk daftar harga dan menunya, abis itu kalau dipilih maka arraynya akan -1
            harga = [20000, 25000,30000 ,30000 ,60000, 80000 ][pilihan_treatment - 1]
            menu_treatment = ["Grooming kering", "Grooming basic", "Grooming shampoo Anti kutu"
                            , "Grooming shampoo Anti jamur", "Grooming shampoo Anti kutu & jamur"
                            , "Grooming shampoo whitening"][pilihan_treatment - 1]
            total_treatment_cat += harga * banyak_hewan
            kucing.append((menu_treatment, banyak_hewan, harga * banyak_hewan)) 
            print(kucing) #testing apakah data yang dimasukkan tersimpan.
            # untuk menghitung total biayanya
        else:
            print("Pilihan tidak valid.")
