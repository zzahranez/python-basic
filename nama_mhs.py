print("=== PROGRAM INPUT NAMA MHS ===")

data_mhs = []

while True:
    input_nama = input("Masukkan nama mahasiswa : ")
    data_mhs.append(input_nama)
    if input_nama == '0':
        break


    

for i in range(len(data_mhs) -1):
    print('Mahasiswa ke ', i , f"{data_mhs[i]}" )

