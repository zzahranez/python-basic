import os
def cld():
    cmd = 'clc'
    os.system(cmd)

print("=== MASUKAN NILAI RATA-RATA MAHASISWA ===")
nilai = []
pilihan = "y"

while True:
    
    userin = input("Masukkan Nilai Mahasiswa : ")
    if userin.isdigit():
        userin = int(userin)
        nilai.append(userin)
    else:
        if userin == pilihan.lower():
         break

for i in range(len(nilai)):
    print(f"Nilai Mahasiswa", i, f": {nilai[i]}")
    
total = sum(nilai)
rata_rata = total / len(nilai)
print('Rata_rata nilai mahasiswa : ', rata_rata)
    