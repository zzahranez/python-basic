import os

#Database
database_buku = [
    {'id':1, 'judul':'belajar python', 'pengarang':'cacadwi'},
    {'id':2, 'judul':'how to get caca heart', 'pengarang':'zahran'}
]

def LihatData():
    print("     ==DAFTAR BUKU==")
    if len(database_buku) == 0:
        print('Tidak tersedia buku')
    else:
        for buku in database_buku:
            print(f"ID: {buku['id']} -  Judul: {buku['judul']} - Pengarang: {buku['pengarang']}")

def TambahBuku():
    print("     ==Tambah Buku")
    id_buku = len(database_buku) + 1
    judul_buku = input("Masukkan judul buku : ")
    pengarang_buku = input("Masukkan Pengarang buku : ")
    database_buku.append({'id': id_buku, 'judul': judul_buku, 'pengarang': pengarang_buku})
    print(f"Data berhasil ditambahkan\nid_buku : {id_buku} - judul_buku : {judul_buku}, pengarang : {pengarang_buku}")

def DeleteBuku():
    LihatData()
    print("\n\n     ==DELETE DATA")
    id_delete = int(input(" Masukkan id yang ingin di hapus : "))
    buku = None
    for b in database_buku:
            if b['id'] == id_delete:
                buku = b
                break
    if buku:
        print(f"\nBuku yang dipilih: ID {buku['id']} - Judul: {buku['judul']} - Pengarang: {buku['pengarang']}")
        konfirmasi = input("\nApakah Anda yakin ingin menghapus data ini? (y/n): ").lower()
        if konfirmasi == 'y':
            database_buku.remove(buku)
            print(f"Buku dengan ID {id_delete} berhasil dihapus!")
        else:
            print("Penghapusdan dibatalkan")
    else:
        print('Terjadi keslahan')
 
def UpdateBuku():
    LihatData()
    print("===  UPDATE DATA ===")
    id_update = int(input("Masukkan id yang akan diupdate : "))
    buku = None
    for b in database_buku:
        if b['id'] == id_update:
            buku = b
            break
    if buku:
        print(f"Id yang dipilih Id : {buku['id']} -  Judul : {buku['judul']} - Pengarang : {buku['pengarang']}")
        konfirmasi = input("Apakah anda yakin ingin mengupdate data ini ? ").lower()
        if konfirmasi == 'y':
            buku['judul'] = input(f"Masukkan judul baru (Sekarang : {buku['judul']}) : ")
            buku['pengarang'] = input(f"Masukkan pengarang baru (Sekarang : {buku['pengarang']}) : ")
            print(f'Data berhasil diperbarui judul: {buku["judul"]} -  Pengarang: {buku["pengarang"]}')
        else :
            print("Terjadi kesalahan")
    else :
        print("Data tidak ditemukan")
            
def cls():
    cmd = 'cls'
    os.system(cmd)
    
while True:
    print("\n     == DATABASE PERPUSTAKAAN ==")
    print("\n     1. Lihat Data  : ")
    print("     2. Tambah Data : ")
    print("     3. Update Data : ")
    print("     4. Delete Data : ")

    opsiTerminal = int(input("\n      Masukkan Pilihan Anda : "))
    cls()

    if opsiTerminal == 1:
        LihatData()
    elif opsiTerminal == 2:
        TambahBuku()
    elif opsiTerminal == 3:
        UpdateBuku()
    elif opsiTerminal == 4:
        DeleteBuku()
    else:
        print("==Pilihan tidak ditemukan==")
    
    opsiLanjut = input("\n\n    Apakah anda ingin kembali kemenu y/n : ")
    if opsiLanjut == 'n' or opsiLanjut == 'N':
        break
    else :
        cls()

