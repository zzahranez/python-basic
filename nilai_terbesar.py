data = [10, 20, 30, 5, 15]

# Inisialisasi nilai terbesar dengan elemen pertama
nilai_terbesar = data[0]

# Iterasi melalui elemen lainnya
for nilai in data:
    if nilai > nilai_terbesar:
        nilai_terbesar = nilai

print("Nilai terbesar adalah:", nilai_terbesar)
