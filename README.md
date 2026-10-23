
# PERTEMUAN 10 — STRING PYTHON

## Identitas Mahasiswa

- Nama: [Rahma Elina Yasmin]
- NIM: [2225250016]
- Kelas: [3F]
- Mata Kuliah: Algoritma dan Pemrograman
- Materi: String Python

---

## 1. Tujuan Pembelajaran

Tujuan dari praktikum Pertemuan 10 adalah untuk memahami dan menerapkan penggunaan string dalam bahasa pemrograman Python. Melalui latihan dan tugas yang dikerjakan, mahasiswa diharapkan mampu:

1. Memahami pengertian string dan penggunaannya dalam Python.
2. Menampilkan panjang string menggunakan fungsi `len()`.
3. Mengakses karakter string menggunakan indeks dan mengambil bagian string menggunakan slicing.
4. Menggunakan metode string seperti `upper()`, `lower()`, `title()`, dan `strip()`.
5. Membersihkan dan menormalisasi teks agar lebih konsisten.
6. Memisahkan teks menggunakan `split()` dan menggabungkan teks menggunakan `join()`.
7. Mencari kata dalam string menggunakan operator `in`, metode `count()`, dan metode `find()`.
8. Membuat program sederhana untuk menormalisasi nama mahasiswa dan kode kelas.
9. Menjalankan, menguji, dan mengelola program Python menggunakan VS Code dan GitHub.

---

## 2. Deskripsi Praktikum

Pada pertemuan ini, praktikum berfokus pada pengolahan data teks atau string menggunakan Python. String merupakan tipe data yang digunakan untuk menyimpan teks, seperti nama mahasiswa, kalimat, dan kode kelas.

Materi yang dipelajari meliputi pengaksesan karakter, pemotongan string, penggunaan metode bawaan string, pembersihan spasi, pemisahan kata, penggabungan teks, dan pencarian kata.

Selain itu, mahasiswa mengerjakan tugas membuat program normalisasi data mahasiswa. Program tersebut digunakan untuk merapikan nama, menyeragamkan penulisan kode kelas, menghitung jumlah kata dalam nama, dan menghasilkan inisial nama.

---

## 3. Daftar Latihan

### Latihan 1 — Dasar String

**Nama file:** `latihan/01_dasar_string.py`

Program ini digunakan untuk menampilkan teks, menghitung panjang string, mengubah teks menjadi huruf kapital, dan mengubah teks menjadi huruf kecil.

**Konsep yang digunakan:**
- Variabel string
- Fungsi `len()`
- Metode `upper()`
- Metode `lower()`

**Contoh hasil keluaran:**

```text
Algoritma
9
ALGORITMA
algoritma
```

### Latihan 2 — Indeks dan Slicing

**Nama file:** `latihan/02_indeks_slicing.py`

Program ini digunakan untuk mengakses karakter tertentu dalam string dan mengambil sebagian teks menggunakan teknik slicing.

**Konsep yang digunakan:**
- Indeks positif
- Indeks negatif
- Slicing
- Pembalikan string menggunakan `[::-1]`

### Latihan 3 — Metode String

**Nama file:** `latihan/03_method_string.py`

Program ini digunakan untuk membersihkan spasi pada awal dan akhir teks serta mengubah format penulisan menjadi huruf kapital di awal setiap kata atau seluruhnya.

**Konsep yang digunakan:**
- `strip()`
- `title()`
- `upper()`

### Latihan 4 — Membersihkan Teks

**Nama file:** `latihan/04_bersihkan_teks.py`

Program ini digunakan untuk merapikan teks yang memiliki spasi berlebihan. Teks dibersihkan agar tidak memiliki spasi di awal atau akhir dan agar jarak antarkata menjadi satu spasi.

**Konsep yang digunakan:**
- `strip()`
- `split()`
- `join()`
- `capitalize()`

### Latihan 5 — Split dan Join

**Nama file:** `latihan/05_split_join.py`

Program ini digunakan untuk memisahkan sebuah kalimat menjadi beberapa kata dan menggabungkan kembali kata-kata tersebut menggunakan tanda hubung.

**Konsep yang digunakan:**
- `split()`
- `join()`

### Latihan 6 — Pencarian Kata

**Nama file:** `latihan/06_pencarian_kata.py`

Program ini digunakan untuk memeriksa keberadaan kata dalam teks, menghitung jumlah kemunculan kata, dan menemukan posisi kemunculan pertama kata.

**Konsep yang digunakan:**
- Operator `in`
- Metode `count()`
- Metode `find()`
- Metode `lower()`

---

## 4. Tugas Praktikum

### Normalisasi Data Mahasiswa

**Nama file:** `tugas/normalisasi_data_mahasiswa.py`

Tugas praktikum ini adalah membuat program untuk mengolah dan menormalisasi data mahasiswa menggunakan fungsi-fungsi string pada Python.

Program menerima input berupa nama mahasiswa dan kode kelas. Selanjutnya, program melakukan pengolahan data agar format nama dan kode kelas menjadi lebih konsisten.

**Fitur program:**

1. Membersihkan spasi berlebihan pada nama mahasiswa.
2. Mengubah nama menjadi format huruf kapital di awal setiap kata.
3. Mengubah kode kelas menjadi huruf kapital.
4. Mengganti pemisah antarkata pada kode kelas menjadi tanda hubung.
5. Menghitung jumlah kata dalam nama mahasiswa.
6. Membuat inisial berdasarkan huruf pertama setiap kata dalam nama.

**Fungsi yang digunakan:**

- `normalisasi_nama(nama)` untuk membersihkan dan merapikan nama mahasiswa.
- `buat_inisial(nama)` untuk menghasilkan inisial nama.
- `normalisasi_kode(kode)` untuk menyeragamkan format kode kelas.

### Contoh Input

```text
Nama: aan hendrayana
Kode kelas: pmat a 2026
```

### Contoh Output

```text
Nama bersih : Aan Hendrayana
Kode kelas : PMAT-A-2026
Jumlah kata : 2
Inisial     : AH
```

---

## 5. Algoritma Program Tugas

Langkah-langkah algoritma program normalisasi data mahasiswa adalah sebagai berikut.

1. Memulai program.
2. Meminta pengguna memasukkan nama mahasiswa.
3. Meminta pengguna memasukkan kode kelas.
4. Membersihkan spasi pada nama dan mengubah formatnya menggunakan `title()`.
5. Membersihkan spasi pada kode kelas dan mengubah semua huruf menjadi kapital.
6. Memisahkan kode kelas berdasarkan spasi, kemudian menggabungkan bagian-bagiannya menggunakan tanda hubung.
7. Memisahkan nama mahasiswa menjadi kata-kata untuk menghitung jumlah katanya.
8. Mengambil huruf pertama dari setiap kata untuk membentuk inisial nama.
9. Menampilkan nama yang sudah dinormalisasi, kode kelas, jumlah kata, dan inisial nama.
10. Mengakhiri program.

---

## 6. Cara Menjalankan Program

Program dijalankan melalui terminal pada Visual Studio Code.

### Langkah 1 — Membuka Folder Proyek

Buka Visual Studio Code, kemudian pilih folder proyek Pertemuan 10 yang berisi file README, folder `latihan`, dan folder `tugas`.

### Langkah 2 — Membuka Terminal

Pilih menu **Terminal**, kemudian klik **New Terminal**.

### Langkah 3 — Menjalankan Program Latihan

Jalankan program dengan mengetikkan perintah berikut pada terminal:

**Latihan 1:**

```bash
python latihan/01_dasar_string.py
```

**Latihan 2:**

```bash
python latihan/02_indeks_slicing.py
```

**Latihan 3:**

```bash
python latihan/03_method_string.py
```

**Latihan 4:**

```bash
python latihan/04_bersihkan_teks.py
```

**Latihan 5:**

```bash
python latihan/05_split_join.py
```

**Latihan 6:**

```bash
python latihan/06_pencarian_kata.py
```

### Langkah 4 — Menjalankan Program Tugas

Untuk menjalankan program normalisasi data mahasiswa, gunakan perintah:

```bash
python tugas/normalisasi_data_mahasiswa.py
```

Jika perintah `python` tidak dapat digunakan pada perangkat, coba gunakan `python3` sebagai penggantinya.

### Langkah 5 — Memasukkan Data

Setelah program tugas dijalankan, masukkan nama mahasiswa dan kode kelas sesuai permintaan program. Periksa apakah hasil normalisasi nama, kode kelas, jumlah kata, dan inisial sudah sesuai.

---

## 7. Hasil Pengujian Program

Pengujian dilakukan dengan memberikan beberapa variasi input untuk memastikan program dapat menormalisasi nama dan kode kelas dengan benar.

| No. | Input Nama | Input Kode Kelas | Nama Bersih | Kode Kelas Bersih | Jumlah Kata | Inisial | Status |
|---|---|---|---|---|---:|---|---|
| 1 | `aan hendrayana` | `pmat a 2026` | Aan Hendrayana | PMAT-A-2026 | 2 | AH | Sesuai |
| 2 | `fATHIYYAH mUTHMAINNAH` | `kelas b` | Fathiyyah Muthmainnah | KELAS-B | 2 | FM | Sesuai |
| 3 | `BUDI` | `pmtk 01` | Budi | PMTK-01 | 1 | B | Sesuai |
| 4 | `siti nur aisyah` | `kelas c` | Siti Nur Aisyah | KELAS-C | 3 | SNA | Sesuai |

**Catatan:** Kolom hasil aktual dan status perlu diperiksa kembali berdasarkan hasil eksekusi program di komputer.

---

## 8. Kesimpulan

Berdasarkan praktikum Pertemuan 10, dapat disimpulkan bahwa string merupakan tipe data yang penting dalam pengolahan teks menggunakan Python. Berbagai metode string dapat digunakan untuk membersihkan teks, mengubah format huruf, mengambil bagian teks, memisahkan kata, menggabungkan teks, dan mencari kata tertentu.

Melalui tugas normalisasi data mahasiswa, penggunaan fungsi string dapat diterapkan pada permasalahan sederhana yang berkaitan dengan pengolahan data. Program membantu menghasilkan nama dan kode kelas yang lebih konsisten sehingga data lebih mudah dibaca dan diolah.

---

## 9. Refleksi

Melalui praktikum ini, saya mempelajari cara menggunakan berbagai metode string dalam Python. Saya memahami bahwa `strip()` digunakan untuk menghapus spasi di awal dan akhir teks, `split()` digunakan untuk memisahkan teks menjadi beberapa bagian, sedangkan `join()` digunakan untuk menggabungkan beberapa bagian teks menjadi satu string.

Saya juga mempelajari bahwa string bersifat immutable, yaitu karakter pada string tidak dapat diubah secara langsung. Jika ingin mengubah teks, saya perlu menghasilkan string baru menggunakan metode yang sesuai.

Kesulitan yang dapat muncul adalah membedakan fungsi setiap metode string dan memastikan format input sudah sesuai. Untuk mengatasinya, saya perlu memahami cara kerja setiap metode, mencoba beberapa variasi input, dan memeriksa hasil program melalui terminal VS Code.

Dengan praktikum ini, saya menjadi lebih memahami penerapan string untuk menyelesaikan masalah pengolahan teks sederhana menggunakan Python.
