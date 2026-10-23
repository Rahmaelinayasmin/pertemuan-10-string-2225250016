# Latihan 6: Pencarian Kata

teks = "Python untuk data. Python untuk pendidikan."

# Mengubah seluruh teks menjadi huruf kecil
teks = teks.lower()

kata = "python"

print("Apakah kata ditemukan?", kata in teks)
print("Jumlah kemunculan:", teks.count(kata))
print("Posisi kemunculan pertama:", teks.find(kata))