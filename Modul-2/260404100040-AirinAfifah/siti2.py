total_belanja = int(input("total belanja:"))

if total_belanja % 100000 == 0:
    total_bayar = 0
elif total_belanja % 50000 == 0:
    diskon = total_belanja * 50 // 100
    total_bayar = total_belanja - diskon
elif total_belanja % 10000 == 0:
    diskon = total_belanja * 20 // 100
    total_bayar = total_belanja - diskon
elif total_belanja >= 200000:
    diskon = total_belanja * 10 // 100
    total_bayar = total_belanja - diskon
else:
    total_bayar = total_belanja

print("total belanja awal =", total_belanja)
print("diskon=", diskon)
print("total harga setelah diskon =", total_bayar)
#print("poin bertambah" if total_bayar > 0 else "tidak ada poin")
if total_bayar > 0:
    print("point bertambah")
else:
    print("tidak ada point")