reguler=40000
vip=75000
vvip=100000
minuman=10000
while True:
    tiket=input("masukkan tiket:")
    uang=int(input("masukkan uang:"))
    if tiket == reguler:
        print("menambah minuman")
        tiket+=1
        tambahan_minuman=minuman+reguler
        continue
    elif tiket == vip:
        print("mendapat minuman gratis")
        tiket+=1

    elif tiket == vvip:
        print("mendapat minuman gratis")
        tiket+=1

    else:
        total_akhir=reguler+vip+vvip
        diskon=total_akhir*0.15
        print("mendapat diskon:", diskon)

    kembalian=uang-diskon
    print("kembalian:", kembalian)

#membuat program jika membeli tiket reguler, vip daan vvip    
