suhu = float(input("suhu reaktor:"))
tekanan = float(input("tekanan gas:"))

if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "bahaya suhu: segera turunkan daya!"
elif suhu > 500:
    if tekanan > 30:
        status = "tekanan tidak stabil"
    else:
        status = "operasi reaktor normal"
else:
    status = "reaktor belum cukup panas"

print("suhu =", suhu, "derajat")
print("tekanan =", tekanan, "bar")
print("status =", status)
print("pompa maksimal" if suhu > 800 else "pompa normal")