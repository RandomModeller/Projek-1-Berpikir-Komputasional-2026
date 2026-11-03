# Menggunakan modul bawaan Python, random, untuk membagi ke dalam 2 kelompok A dan B secara acak.
import random

# Menghitung jumlah mahasiswa.
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa (2 sampai 676): "))

# Jika jumlah mahasiswa terlalu sedikit untuk dibagi ke 2 kelompok (di bawah 2), atau
# Jika jumlah mahasiswa melebihi kemampuan program saat ini (di atas 676 mahasiswa), maka
# Hentikan program dan tuliskan pesan error
if jumlah_mahasiswa < 2 or jumlah_mahasiswa > 676:
    print("Jumlah mahasiswa di luar kemampuan program!")
    exit()

# Menghitung tanggal hari ini
tanggal_hari_ini_string = input("Masukkan tanggal hari ini dalam format DD-MM-YYYY: ")
tanggal_hari_ini = []
buffer_tanggal = ""

# Mengubah tanggal hari ini dari string menjadi list dengan tipe int
for char in tanggal_hari_ini_string:
    if char == "-":
        tanggal_hari_ini.append(int(buffer_tanggal))
        buffer_tanggal = ""
    else:
        buffer_tanggal += char
else:
    tanggal_hari_ini.append(int(buffer_tanggal))
    buffer_tanggal = ""

# Membuat list kosongan untuk menampung semua biodata mahasiswa
daftar_mahasiswa = []

print(f"Menghasilkan data mahasiswa sebanyak {jumlah_mahasiswa} orang:")

# Menghasilkan data mahasiswa
for i in range(jumlah_mahasiswa):
    daftar_mahasiswa.append([]) # Membuat list kosongan yang akan menampung data berupa inisial nama, tanggal lahir, jenis kelamin, dan tinggi badan

    daftar_mahasiswa[i].append(chr(65 + i // 26) + chr(65 + i % 26))    # Menentukan inisial random

    tahun = random.randint(2003, 2015)  # Menentukan tahun kelahiran
    bulan = random.randint(1, 12)       # Menentukan bulan kelahiran
    tanggal = 0

    if bulan == 2:                      # hanya ada 28 hari dalam 1 bulan ketika Februari
        tanggal = random.randint(1, 28)
    elif bulan in (4, 6, 9, 11):        # hanya ada 30 hari dalam 1 bulan ketika April, Juni, September, dan Oktober
        tanggal = random.randint(1, 30)
    else:                               # hanya ada 31 hari dalam 1 bulan yang lain
        tanggal = random.randint(1, 31)

    daftar_mahasiswa[i].append([tanggal, bulan, tahun])     # Menentukan tanggal lahir random

    daftar_mahasiswa[i].append(("laki-laki", "perempuan")[random.randint(0, 1)])    # Menentukan jenis kelamin random

    daftar_mahasiswa[i].append(random.randint(150, 180))    # Menentukan tinggi badan random

    print(f"Inisial: {daftar_mahasiswa[i][0]}\nTanggal lahir: {"-".join(map(str, daftar_mahasiswa[i][1]))}\nJenis kelamin: {daftar_mahasiswa[i][2]}\nTinggi badan: {daftar_mahasiswa[i][3]} cm\n")

# Membuat grup kosongan untuk tiap kategori umur, jenis kelamin, dan tinggi badan.
grup_umur = [[], [], []]
grup_jenis_kelamin = [[], []]
grup_tinggi = [[], [], []]

# Membuat grup kosongan untuk 18 subgrup yang tersedia:
# 1.  < 16 tahun, laki-laki, < 160 cm
# 2.  < 16 tahun, laki-laki, 160-170 cm
# 3.  < 16 tahun, laki-laki, > 170 cm
# 4.  16-19 tahun, laki-laki, < 160 cm
# 5.  16-19 tahun, laki-laki, 160-170 cm cm
# 6.  16-19 tahun, laki-laki, > 170 cm
# 7.  > 19 tahun, laki-laki, < 160 cm
# 8.  > 19 tahun, laki-laki, 160-170 cm
# 9.  > 19 tahun, laki-laki, > 170 cm
# 10. < 16 tahun, perempuan, < 160 cm
# 11. < 16 tahun, perempuan, 160-170 cm
# 12. < 16 tahun, perempuan, > 170 cm
# 13. 16-19 tahun, perempuan, < 160 cm
# 14. 16-19 tahun, perempuan, 160-170 cm cm
# 15. 16-19 tahun, perempuan, > 170 cm
# 16. > 19 tahun, perempuan, < 160 cm
# 17. > 19 tahun, perempuan, 160-170 cm
# 18. > 19 tahun, perempuan, > 170 cm
grup_akhir = [[] for x in range(18)]

for mahasiswa in daftar_mahasiswa:
    # Ubah tanggal lahir dari format DD-MM-YYYY ke desimal agar mudah dibandingkan.
    tanggal_lahir_desimal = mahasiswa[1][2] + mahasiswa[1][1] / 12 + mahasiswa[1][0] / 31
    tanggal_hari_ini_desimal = tanggal_hari_ini[2] + tanggal_hari_ini[1] / 12 + tanggal_hari_ini[0] / 31

    # Hitung selisih tanggal untuk mendapaykan umur.
    umur_desimal = tanggal_hari_ini_desimal - tanggal_lahir_desimal

    # Inisialisasi variabel untuk menentukan
    indeks_subgrup = 0

    # Menentukan kelompok umur serta subgrup
    if umur_desimal < 16:
        grup_umur[0].append(mahasiswa[0])
        indeks_subgrup += 0
    elif umur_desimal > 19:
        grup_umur[2].append(mahasiswa[0])
        indeks_subgrup += 6
    else:
        grup_umur[1].append(mahasiswa[0])
        indeks_subgrup += 3

    # Menentukan kelompok tinggi badan serta subgrup
    if mahasiswa[3] < 160:
        grup_tinggi[0].append(mahasiswa[0])
        indeks_subgrup += 0
    elif mahasiswa[3] > 170:
        grup_tinggi[2].append(mahasiswa[0])
        indeks_subgrup += 2
    else:
        grup_tinggi[1].append(mahasiswa[0])
        indeks_subgrup += 1

    # Menentukan kelompok tinggi badan serta subgrup
    if mahasiswa[2] == "laki-laki":
        grup_jenis_kelamin[0].append(mahasiswa[0])
        indeks_subgrup *= 1
    else:
        grup_jenis_kelamin[1].append(mahasiswa[0])
        indeks_subgrup *= 2

    grup_akhir[indeks_subgrup].append(mahasiswa[0])

print("Grup mahasiswa di bawah 16 tahun")
print(grup_umur[0])
print("\nGrup mahasiswa 16-19 tahun")
print(grup_umur[1])
print("\nGrup mahasiswa di atas 19 tahun")
print(grup_umur[2])

print("\nGrup mahasiswa laki-laki")
print(grup_jenis_kelamin[0])
print("\nGrup mahasiswa perempuan")
print(grup_jenis_kelamin[1])

print("\nGrup mahasiswa di bawah 160 cm")
print(grup_tinggi[0])
print("\nGrup mahasiswa 160-170 cm")
print(grup_tinggi[1])
print("\nGrup mahasiswa di atas 170 cm")
print(grup_tinggi[2])
print("")

for i in range(18):
    print(f"Subgrup {i + 1}: {grup_akhir[i]}")

grup_A = []
grup_B = []

for grup in grup_akhir:
    jumlah_mahasiswa_subgrup = len(grup)
    jumlah_mahasiswa_grup_A = jumlah_mahasiswa_subgrup // 2

    if len(grup) % 2 == 1:
        jumlah_mahasiswa_grup_A = random.choice((jumlah_mahasiswa_grup_A, jumlah_mahasiswa_grup_A + 1))

    for i in range(jumlah_mahasiswa_subgrup):
        mahasiswa_tersisa = jumlah_mahasiswa_subgrup - i

        if jumlah_mahasiswa_grup_A == 0:
            grup_B.append(grup[i])
        elif jumlah_mahasiswa_grup_A == i:
            grup_A.append(grup[i])
            jumlah_mahasiswa_grup_A -= 1
        else:
            if random.randint(0, 1) == 0:
                grup_A.append(grup[i])
                jumlah_mahasiswa_grup_A -= 1
            else:
                grup_B.append(grup[i])

print("\nMahasiswa grup A:")
print(grup_A)
print("\nMahasiswa grup B:")
print(grup_B)
