print("=== ICE CREAM ===")
vanila = 20000
coklat  = 25000
capuccino = 30000

keranjang = []
while True:
    print("=== PILIHAN MINUMNAN ===")
    print("1. Vanila ")
    print("2. Coklat ")
    print("3. Cappucino ")
    user_opsi = input('Masukkan pilihan :')
    
    if user_opsi == '1':
        keranjang.append(vanila)
    elif user_opsi == '2':
        keranjang.append(coklat)
    elif user_opsi == '3':
        keranjang.append(capuccino)
    else : 
        print("Opsi tidak tersedia ")
        break
        
    pilihan_awal = input("Apakah ingin membeli lagi : y/n")
    if user_opsi == 'n':
         break    

    total = sum(keranjang)
print(total)
    