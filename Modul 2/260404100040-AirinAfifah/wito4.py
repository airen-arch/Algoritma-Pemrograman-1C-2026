pin = int(input("pin 3 digit:"))
jam = int(input("jam kedatangan (0-23):"))

digit_1 = pin // 100
digit_2 = (pin // 10) % 10
digit_3 = pin % 10

if pin % 5 == 0:
    if jam < 12:
        status = "garasi pagi terbuka"
    else:
        status = "garasi malam terbuka, lampu dinyalakan"
elif pin % 2 == 0:
    if digit_1 + digit_3 == digit_2:
        status = "garasi VIP terbuka khusus bos"
    else:
        status = "kode genap ditolak, alarm berbunyi!"
else:
    status = "akses ditolak"

print("digit pertama =", digit_1)
print("digit kedua =", digit_2)
print("digit ketiga =", digit_3)
print("status akses =", status)
print("mode malam merekam" if jam > 18 else "mode siang standby")