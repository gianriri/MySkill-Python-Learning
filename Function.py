# Tanpa Parameter
def nama_fungsi():
    print("Hello World!")

# Memanggil fungsi
nama_fungsi()

# Dengan Parameter
def kali(a, b):
    hasil_kasil = a * b
    print("Hasil kali a x b =", hasil_kasil)

#Memanggil fungsi
kali(3, 4)
kali(4, 5)
kali(2, 2)

# Dengan Return
def bagi(a,b):
    hasil_bagi = a / b
    return hasil_bagi

# Memanggil fungsi
nilai1 = 20
nilai2 = 4
hasil_pembagian = bagi(nilai1, nilai2)

print(hasil_pembagian)