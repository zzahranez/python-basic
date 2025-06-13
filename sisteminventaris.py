import os

#Fitur utama 
#Tambah Barang
#perbarui Stock
#cari Barang berdasarkan code atau nama
#Laporan stok minimum

database_barang = [
    {"id": 1, "nama_barang": "Semen", "stock": 4},
    {"id": 2, "nama_barang": "kulkas", "stock":3}
]

def cls():
    cmd = 'cls'
    os.system(cmd)
    
def LihatBarang():
    print("==DAFTAR BARANG==")
    if len(database_barang) == 0:
        print("Barang Kosong")
    else :
        for brng in database_barang:
            print("|============================================|")
            print(f"| Id : {brng['id']} - Nama Barang : {brng['nama_barang']} -  Stock : {brng['stock']} |")
        
def TambahBarang():
    print('=== TAMBAH BARANG ===')
    id_barang = len(database_barang) + 1
    nama_brng = input('Masukkan nama barang : ')
    stock_brng = int(input("Masukkan stock barang : "))
    database_barang.append({'id': id_barang, 'nama_barang': nama_brng, 'stock': stock_brng})
    print(f"Data Berhasil ditambahakan\nId: {id_barang} Nama barang : {nama_brng} Stock yang tersedia : {stock_brng}")
    
def UpdateBarang():
    LihatBarang()
    print("\n   == UPDATE BARANG ==")
    id_update = int(input("Masukkan id data yang ingin diupdate : "))
    barang = None
    for b in database_barang:
        if b['id'] == id_update:
            barang = b
            break
    if barang :
        print(f'Barang yang ingin diupdate Id: {barang['id']} - Nama Barang : {barang['nama_barang']} -  Stock: {barang['stock']}')
        konfirmasi = input("Apakah anda yakin ingin update stock ini : ").lower()
        if konfirmasi == 'y':
            barang["stock"] = int(input(f"Masukkan Stock (Sekarang {barang['stock']}) : "))
            print(f"Stock Berhasil diupdate\nNama Barang : {barang['nama_barang']}\nStock : {barang['stock']}")
        else :
            print("Terjadi Kesalahan")
    else:
        print("id tidak ditemukan")
        
def CariBarang():
    LihatBarang()
    print("\n\n     === PENCARIAN BARANG YANG TERSEDIA ===")
    nama_barang = input("\n     Masukkan barang yang ingin dicari : ")
    brg = None
    for nb in database_barang:
        if nb['nama_barang'] == nama_barang:
            brg = nb
            break  # Keluar loop hanya jika barang ditemukan
    if brg:
        print(f"\n      Barang ditemukan : {brg['nama_barang']}")
    else:
        print("Barang tidak ditemukan")
        
def LaporanStockMinimum():
    print("===  LAPORAN STOCK MINIMUM ===")
    barang_minimum = []
    for barang in database_barang:
        if barang['stock']  <= 10:
            barang_minimum.append(barang)
    # Langkah 2: Sortir barang berdasarkan stok
    barang_minimum_sorted = []
    while barang_minimum:
        # Temukan barang dengan stok terkecil
        barang_terkecil = barang_minimum[0]
        for barang in barang_minimum:
            if barang['stock'] < barang_terkecil['stock']:
                barang_terkecil = barang
        # Tambahkan barang terkecil ke daftar yang diurutkan
        barang_minimum_sorted.append(barang_terkecil)
        # Hapus barang terkecil dari daftar asli
        barang_minimum.remove(barang_terkecil)
    if barang_minimum_sorted:
        print(f"{'ID':<10}{'Nama Barang':<20}{'Stok':<10}")
        print("-" * 40)
        for barang in barang_minimum_sorted:
            print(f"{barang['id']:<10}{barang['nama_barang']:<20}{barang['stock']:<10}")
    else:
        print("Tidak ada barang dengan stok kurang dari atau sama dengan 10.")
    
            
    
while True:
    print("=== SISTEM MANAJEMEN INVENTARIS ===")
    print("1. Lihat Barang ")
    print("2. Tambah Barang ")
    print("3. Perbarui Stock ")
    print("4. Cari Barang ")
    print("5. Laporan Stock Minimum")
    
    opsiTerminal = int(input("Masukkan opsi yang ingin dipilih : "))
    cls()
    
    if opsiTerminal == 1:
        LihatBarang()
    elif opsiTerminal == 2:
        TambahBarang()
    elif opsiTerminal == 3:
        UpdateBarang()
    elif opsiTerminal == 4:
        CariBarang()
    elif opsiTerminal() == 5:
        LaporanStockMinimum
    else:
        print("opsi Tidak ditemukan")

    lanjutorno = input("\nApakah anda ingin kembali kemenu (?) y/n : ").lower()
    
    if  lanjutorno == 'n' :
        print("Terimakasih telah menggunakan program")
        break
    else:
        cls()