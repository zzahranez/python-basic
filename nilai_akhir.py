import os
def cls():
    cmd = 'cls'
    os.system(cmd)

def bobot(nilai, persen):
    bobot = persen / 100
    nilai_col = nilai * bobot
    return nilai_col

print("\n\n==== MENENTUKAN NILAI AKHIR MHS ====")
nilai_kehadiran = float(input("Masukkan nilai kehadiran : "))
bbot_hadir = bobot(nilai_kehadiran, 20)
print(bbot_hadir)
nilai_tugas = float(input("Masukkan nilai tugas : "))
bbot_tgs = bobot(nilai_tugas, 20)
nilai_uts = float(input("Masukkan nliai UTS : "))
bbt_uts = bobot(nilai_uts, 25)
nilai_uas = float(input("Masukkan nilai UAS : "))
bbt_uas = bobot(nilai_uas, 35)
nilai_akhir = bbot_hadir + bbot_tgs + bbt_uts + bbt_uas
print(f"\nNilai Akhir : {nilai_akhir}")

if nilai_akhir == 0 and nilai_akhir <= 44:
    print("Bobot : E")
elif nilai_akhir >= 45 and nilai_akhir <= 55:
    print("Bobot : D")
elif nilai_akhir >= 56 and nilai_akhir <= 65:
    print("Bobot : C")
elif nilai_akhir >= 66 and nilai_akhir <= 75:
    print("Bobot : B-")
elif nilai_akhir >= 76 and  nilai_akhir <= 80:
    print("Bobot : B")
elif nilai_akhir >= 81 and nilai_akhir <= 85:
    print("Bobot : B+")
elif nilai_akhir >= 86 and nilai_akhir <= 90:
    print("Bobot : A-")
elif nilai_akhir >= 91 and nilai_akhir <= 100:
    print("Bobot : A")