jarak_pergi = 100
jarak_pulang= 100
konsumsi = 40
bensin = 1.5
harga_bensin = 10000

total_jarak = jarak_pergi + jarak_pulang
total_bensin = total_jarak / konsumsi
total_bensin_dibeli = total_bensin - bensin
total_biaya = total_bensin_dibeli * harga_bensin

print("jarak perjalanan=", total_jarak, "km")
print("bensin=", total_bensin, "liter")
print("bensin yang harus dibeli=", total_bensin_dibeli, "liter")
print("total biaya:", int(total_biaya))
