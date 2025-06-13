import os



def cls():
    cmd = "cls"
    os.system(cmd)

def diskon20(total_pembelian):
        diskon = 20 /100
        harga = total_pembelian - (total_pembelian * diskon)
        return harga
    
def diskon35(total_pembelian):
    diskon = 35 / 100
    harga = total_pembelian - (total_pembelian * diskon)
    return harga

while True:
    input_user = float(input("\n\n  Total Pembelian Pelanggan Rp. : "))
    harga_diskon = input_user
    if input_user < 25000:
         print(f"    Total Pembelian : {input_user}")
     
    elif input_user > 25000 and input_user < 45000:
        harga20 = diskon20(harga_diskon)
        besar_diskon = input_user - harga20
        print("\n   === NOTA ===")
        print(f"    Total Pembelian : {input_user}")
        print(" Besaran Diskon : 20%")
        print(f"    Diskon : {besar_diskon}")
        print(f"    Total Setelah diskon : {harga20}")
    elif input_user > 45000 :
        harga35 = diskon35(harga_diskon)
        besar_diskon = input_user - harga35
        print("\n   === NOTA ===")
        print(f"    Total Pembelian : {input_user}")
        print("     Besaran Diskon : 35%")
        print(f"    Diskon : {besar_diskon}")
        print(f"    Total Setelah diskon : {harga35}")
    
    pilihan = input("Apakah anda ingin lanjut y/n : ").lower()
    if pilihan == 'n':
        break
    else:
        cls()