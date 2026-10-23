# Latihan 4: Membersihkan Teks

teks = " belajar    python  untuk           pendidikan       "

# Menghapus spasi di awal dan akhir
teks = teks.strip()

# Memisahkan teks berdasarkan spasi
# lalu menggabungkannya kembali dengan satu spasi
teks = " ".join(teks.split())

# Mengubah huruf pertama menjadi kapital
teks = teks.capitalize()

print("Teks setelah dibersihkan:", teks)