# Import modul untuk mendapatkan input pengguna
from getpass import getpass

password = getpass('Enter Password: ')
valid_password = 'password'

if password == valid_password:
    print("Selamat datang bos! ")
else:
    print("Password Salah, coba lagi!")

print("Terimakasih sudah menggunakan aplikasi kami")