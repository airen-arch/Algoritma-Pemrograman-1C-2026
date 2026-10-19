jumlah_penumpang = 0
total_pendapatan = 0
jarak_terjauh = 0
total_jarak = 0

while True:
    jarak = int(input("masukkan jarak km (0 untuk berhenti):"))

    if jarak == 0:
        break
    if jarak < 0:
        print("jarak tidak valid")
        continue

    jumlah_penumpang += 1
    total_jarak += jarak

    if jarak <= 5:
        tarif = 3000
    elif jarak <= 15:
        tarif = 3000 + (jarak - 5) * 1000
    else:
        tarif = 13000 + (jarak - 15) * 500

    if jumlah_penumpang % 5 == 0:
        tarif = tarif * 50 // 100
        print("diskon 50%")

    total_pendapatan += tarif
    print("tarif penumpang:", tarif)

    if jarak > jarak_terjauh:
        jarak_terjauh = jarak
print("jumlah penumpang:", jumlah_penumpang)
print("total pendapatan:", total_pendapatan)

if jumlah_penumpang > 0:
    rata_rata = total_jarak / jumlah_penumpang
    print("jarak terjauh:", jarak_terjauh, "km")
    print(f"rata-rata jarak: {rata_rata:.0f} km")
else:
    print("jarak terjauh: 0 km")
    print("rata-rata jarak: 0 km")