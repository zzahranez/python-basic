# Latihan dictonary
import datetime
import os

mahasiswa_template = {
    'nama' : 'Jack',
    'nim' : "000000",
    'sks_lulus' : 0,
    'lahir' : datetime.datetime(1111,1,1)
}


os.system("cls")


print(f"{'SELAMAT DATANG':^20}")
print("-"*20)

mahasiswa = dict.fromkeys(mahasiswa_template.keys())
mahasiswa['nama'] = input("Nama Mahasiswa : ")
mahasiswa['nim'] = input("NIM Mahasiswa : ")
mahasiswa['sks_lulus'] = int(input('SKS Lulus : '))
TAHUN_LAHIR = int(input("Masukan tahun lahir : "))
BULAN_LAHIR = int(input("Masukan bulan lahir (1-12): "))
TANGGAL_LAHIR = int(input("Masukan tanggal Lahir (1-31) : "))
mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

print("\nDATA MAHASISWA BERHASIL DITAMBAHAKAN")
print("-"*30)

print(f"\nNama : {mahasiswa['nama']}")
print(f"Nim : {mahasiswa['nim']}")
print(f"SKS Lulus : {mahasiswa['sks_lulus']} SKS")
print(f"Tanggal lahir : {mahasiswa['lahir']}")
