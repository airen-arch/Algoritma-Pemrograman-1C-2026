while True:
    n = int(input("tinggi menara (2-15): "))

    if n >= 2 and n <= 15:
        break
    else:
        print("input tidak valid")

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j % 10, end="")
    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j % 10, end="")
    for j in range(i - 1, 0, -1):
        print(j % 10, end="")

    print()