# Tugas 4: Normalisasi Data Mahasiswa
# Pertemuan 10 - String dan Pengolahan Teks

def normalisasi_nama(nama):
    """Membersihkan spasi dan menyeragamkan format nama."""
    nama = " ".join(nama.strip().split())
    return nama.title()


def buat_inisial(nama):
    """Membuat inisial dari setiap kata dalam nama."""
    nama_bersih = normalisasi_nama(nama)
    kata = nama_bersih.split()

    inisial = "".join(k[0] for k in kata)
    return inisial


def normalisasi_kode(kode):
    """Membersihkan dan mengubah kode kelas menjadi huruf besar."""
    kata = kode.strip().upper().split()
    return "-".join(kata)


# Input data mahasiswa
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Memproses data menggunakan fungsi
nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
inisial = buat_inisial(nama)
jumlah_kata = len(nama_bersih.split())

# Menampilkan hasil
print("\n=== HASIL NORMALISASI DATA MAHASISWA ===")
print("Nama bersih :", nama_bersih)
print("Kode kelas  :", kode_bersih)
print("Jumlah kata :", jumlah_kata)
print("Inisial     :", inisial)