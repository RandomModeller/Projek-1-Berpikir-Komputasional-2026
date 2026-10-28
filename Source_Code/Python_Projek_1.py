import random

jumlah_mahasiswa = 26
tanggal_hari_ini = [26, 10, 2026]

daftar_mahasiswa = []

for i in range(jumlah_mahasiswa):
    daftar_mahasiswa.append([])

    daftar_mahasiswa[i].append(chr(65 + i)) # Menentukan inisial random

    tahun = random.randint(2003, 2015)
    bulan = random.randint(1, 12)
    tanggal = 0

    if bulan == 2:                      # hanya ada 28 hari dalam 1 bulan ketika Februari
        tanggal = random.randint(1, 28)
    elif bulan in (4, 6, 9, 11):        # hanya ada 30 hari dalam 1 bulan ketika April, Juni, September, dan Oktober
        tanggal = random.randint(1, 30)
    else:                               # hanya ada 31 hari dalam 1 bulan yang lain
        tanggal = random.randint(1, 31)

    daftar_mahasiswa[i].append([tanggal, bulan, tahun]) # Menentukan tanggal lahir random

    daftar_mahasiswa[i].append(("laki-laki", "perempuan")[random.randint(0, 1)]) # Menentukan jenis kelamin random

    daftar_mahasiswa[i].append(random.randint(150, 180)) # Menentukan tinggi badan random

    print(f"Inisial: {daftar_mahasiswa[i][0]}\nTanggal lahir: {"-".join(map(str, daftar_mahasiswa[i][1]))}\nJenis kelamin: {daftar_mahasiswa[i][2]}\nTinggi badan: {daftar_mahasiswa[i][3]} cm")

grup_umur = [[], [], []]
grup_jenis_kelamin = [[], []]
grup_tinggi = [[], [], []]

grup_akhir = [[] for x in range(18)]

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

for mahasiswa in daftar_mahasiswa:
    tanggal_lahir_desimal = mahasiswa[1][2] + mahasiswa[1][1] / 12 + mahasiswa[1][0] / 31
    tanggal_hari_ini_desimal = tanggal_hari_ini[2] + tanggal_hari_ini[1] / 12 + tanggal_hari_ini[0] / 31

    umur_desimal = tanggal_hari_ini_desimal - tanggal_lahir_desimal

    indeks_subgrup = 0

    if umur_desimal < 16:
        grup_umur[0].append(mahasiswa[0])
        indeks_subgrup += 0
    elif umur_desimal > 19:
        grup_umur[2].append(mahasiswa[0])
        indeks_subgrup += 6
    else:
        grup_umur[1].append(mahasiswa[0])
        indeks_subgrup += 3

    if mahasiswa[3] < 160:
        grup_tinggi[0].append(mahasiswa[0])
        indeks_subgrup += 0
    elif mahasiswa[3] > 170:
        grup_tinggi[2].append(mahasiswa[0])
        indeks_subgrup += 2
    else:
        grup_tinggi[1].append(mahasiswa[0])
        indeks_subgrup += 1

    if mahasiswa[2] == "laki-laki":
        grup_jenis_kelamin[0].append(mahasiswa[0])
        indeks_subgrup *= 1
    else:
        grup_jenis_kelamin[1].append(mahasiswa[0])
        indeks_subgrup *= 2

    grup_akhir[indeks_subgrup].append(mahasiswa[0])

print(grup_umur)
print(grup_jenis_kelamin)
print(grup_tinggi)
print(grup_akhir)

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
            grup_B.append(grup[i][0])
        elif jumlah_mahasiswa_grup_A == i:
            grup_A.append(grup[i][0])
            jumlah_mahasiswa_grup_A -= 1
        else:
            if random.randint(0, 1) == 0:
                grup_A.append(grup[i][0])
                jumlah_mahasiswa_grup_A -= 1
            else:
                grup_B.append(grup[i][0])

print(grup_A)
print(grup_B)
