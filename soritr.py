
kelas_all = ['10 A', '10 B', '11 A', '11 B', '12 A', '12 B', '10 C']

for i in range(len(kelas_all)):
    print(kelas_all[i])
    
    
kelas_parsed = []

for kelas in kelas_all:
    kelas_tanpa_spasi = kelas.replace(' ', '')
    angka_str = ''
    number_str = ''
    for character in kelas_tanpa_spasi:
        if character.isdigit():
            angka_str += character
        else:
            number_str += character
    angka = int(angka_str) if angka_str else 1
    kelas_parsed.append((angka, number_str.upper(), kelas))

# Sort berdasarkan angka dan huruf
kelas_parsed.sort(key=lambda x: (x[0], x[1]))

# Ambil hasil sorted dalam format asli (kelas string)
kelas_sorted = [item[2] for item in kelas_parsed]

print(kelas_sorted)