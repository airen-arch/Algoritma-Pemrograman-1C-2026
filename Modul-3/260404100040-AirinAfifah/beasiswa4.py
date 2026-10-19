jumlah_beasiswa_penuh = 0

for i in range(1, 11):
    if jumlah_beasiswa_penuh == 3:
        break
    print("mahasiswa ke-", i)
    nama = input("nama: ")
    ipk = float(input("IPK: "))
    penghasilan = int(input("penghasilan orang tua: "))

    if ipk < 3.00:
        print("tidak memenuhi syarat beasiswa")
        continue

    if penghasilan <= 3000000:
        print("mendapat beasiswa penuh")
        jumlah_beasiswa_penuh += 1
    elif penghasilan <= 5000000:
        print("mendapat beasiswa sebagian")
    else:
        print("tidak mendapat beasiswa")

print("jumlah penerima beasiswa penuh:", jumlah_beasiswa_penuh)