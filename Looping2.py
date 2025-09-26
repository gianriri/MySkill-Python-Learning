# Looping while

ulangi = input("Are You Ready? ")
print("Start")
counter = 0

while ulangi:
    jawab = input("Apakah anda mau mengulang? (yes/no): ")
    counter += 1
    if jawab == "no":
        ulangi = False
    print("Pengulangan ke-" + str(counter))