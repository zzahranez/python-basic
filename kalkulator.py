import os

def cls():
    cmd = 'cls'
    os.system(cmd)
    
while True:

    print("\n\n===== KALKULATOR =====")
    print("1. Tambah ")
    print("2. Kurang ")
    print("3. Kali ")
    print("4. Bagi ")
    terminalInput = int(input("Masukkan operator anda : "))

    cls()

    print("\n\n==== SILAHKAN MEMASUKKAN BILANGAN ====")
    num1 = float(input("\n||      Masukkan angka pertama : "))
    num2 = float(input("\n||      Masukkan angka kedua   : "))

    if terminalInput ==  1 :
        print("\n     === PENJUMLAHAN ===")
        hasil = num1 + num2
        print('     Hasil Penjumlahan : ', hasil, '\n\n')
    elif terminalInput == 2:
        print("\n       === PENGURANGAN ===")
        hasil = num1 - num2
        print("     Hasil pengurangan ialah : ", hasil, '\n\n')
    elif terminalInput == 3:
        print("\n       === PERKALIAN ===")
        hasil = num1 * num2
        print("     Hasil perkalian adalah : ", hasil, '\n\n')
    elif terminalInput == 4 :
        print("\n       === PEMBAGIAN ===")
        hasil = num1 / num2
        print('     Hasil pembagian adalah : ',hasil, '\n')
    else :
        print("        === OPERATOR TIDAK DITEMUKAN === :)")
        
    opsiUlang = input("\n     Apakah anda ingin mengulang y/n ? ")

    if opsiUlang == 'n' or opsiUlang == 'N':
        print("\n\n  TERIMAKASIH TELAH MENGGUNAKAN PROGRAM")
        break
    cls()