jumlah_mahasiswa = 10
total_nilai = 0

jumlah_A = 0
jumlah_B = 0
jumlah_C = 0
jumlah_D = 0
jumlah_E = 0

nilai_tertinggi = -1
nilai_terendah = 101

for i in range(1, 11):
    print("mahasiswa ke-", i)
    nama = input("nama: ")
    nilai_tugas = float(input("nilai tugas: "))
    nilai_uts = float(input("nilai UTS: "))
    nilai_uas = float(input("nilai UAS: "))

    nilai_akhir = nilai_tugas * 0.30 + nilai_uts * 0.30 + nilai_uas * 0.40

    if nilai_akhir >= 85:
        kategori = "A"
        jumlah_A += 1
    elif nilai_akhir >= 75:
        kategori = "B"
        jumlah_B += 1
    elif nilai_akhir >= 65:
        kategori = "C"
        jumlah_C += 1
    elif nilai_akhir >= 50:
        kategori = "D"
        jumlah_D += 1
    else:
        kategori = "E"
        jumlah_E += 1

    print("nama:", nama)
    print(f"nilai akhir: {nilai_akhir:.2f}")
    print("kategori:", kategori)

    total_nilai += nilai_akhir

    if nilai_akhir > nilai_tertinggi:
        nilai_tertinggi = nilai_akhir
        nama_tertinggi = nama

    if nilai_akhir < nilai_terendah:
        nilai_terendah = nilai_akhir
        nama_terendah = nama

print("jumlah kategori A:", jumlah_A)
print("jumlah kategori B:", jumlah_B)
print("jumlah kategori C:", jumlah_C)
print("jumlah kategori D:", jumlah_D)
print("jumlah kategori E:", jumlah_E)
print("nama:", nama_tertinggi, f"dengan nilai tertinggi: {nilai_tertinggi:.2f}")
print("nama:", nama_terendah, f"dengan nilai terendah: {nilai_terendah:.2f}")
print(f"rata-rata nilai: {total_nilai / jumlah_mahasiswa:.2f}")