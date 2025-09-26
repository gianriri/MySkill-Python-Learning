nilai = int(input('Masukkan Nilai: '))
grade = ""

if nilai > 90:
    grade = "A"
elif nilai > 80:
    grade = "B"
elif nilai > 70:
    grade = "C"
else: 
    grade = "D"

print("Grade Anda adalah", grade)