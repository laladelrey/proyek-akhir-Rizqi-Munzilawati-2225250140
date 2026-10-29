# Proposal Proyek Akhir: Program Rekap dan Analisis Nilai Matematika Kelas

## 1. Judul Proyek
Program Rekap dan Analisis Nilai Matematika Kelas[cite: 52]

## 2. Latar Belakang
Guru matematika memerlukan program sederhana yang dapat membaca data nilai, memvalidasi isi, menghitung statistik, menentukan ketuntasan, dan menyimpan laporan secara cepat dan konsisten[cite: 47, 52].

## 3. Pengguna dan Tujuan
* **Pengguna:** Guru Matematika[cite: 47].
* **Tujuan:** Memperoleh rekapitulasi nilai, statistik kelas, dan status ketuntasan secara otomatis[cite: 47].

## 4. Ruang Lingkup & Fitur Wajib
1. Membaca file data nilai[cite: 47, 52].
2. Memvalidasi nilai pada rentang 0 sampai 100[cite: 47, 52].
3. Menghitung rata-rata, minimum, dan maksimum[cite: 47, 52].
4. Menentukan status tuntas / belum tuntas berdasarkan KKM (60)[cite: 47, 52].
5. Menyimpan laporan ke dalam file teks[cite: 47, 52].

## 5. Input, Proses, Output (IPO)
* **Input:** File teks berisi data nilai siswa (`nilai_contoh.txt`)[cite: 48].
* **Proses:** Membaca file, validasi rentang 0-100, menghitung statistik kelas, dan menentukan klasifikasi ketuntasan[cite: 48].
* **Output:** Ringkasan statistik (rata-rata, min, max, jumlah tuntas) dan file laporan teks di folder `output/`[cite: 48, 49].

## 6. Algoritma (Pseudocode)
MULAI
baca data dari file
jika file tidak ditemukan: tampilkan pesan error
untuk setiap baris data:
    validasi format dan nilai (0-100)
    simpan data valid
jika tidak ada data valid: tampilkan pesan
hitung statistik dan tentukan status ketuntasan
tampilkan ringkasan dan simpan laporan ke file
SELESAI[cite: 48]

## 7. Struktur Program dan Modularisasi
* `src/main.py` : Mengatur alur utama program.
* `src/data_io.py`: Membaca dan menyimpan file[cite: 49].
* `src/utilitas.py`: Validasi nilai[cite: 49].
* `src/analisis.py`: Perhitungan statistik dan status[cite: 49].

## 8. Struktur Data
* **List:** Untuk menampung kumpulan nilai numerik.
* **Dictionary:** Untuk menyimpan ringkasan statistik kelas.

## 9. Perancangan Test Case (Minimal 5 Pengujian)
| ID | Kategori | Input / Kondisi | Expected Result |
|---|---|---|---|
| TC01 | Normal | Nilai 70, 80, 90 | Rata-rata dihitung 80.0 |
| TC02 | Batas | Nilai 0 | Diterima sebagai nilai valid |
| TC03 | Batas | Nilai 100 | Diterima sebagai nilai valid |
| TC04 | Invalid | Nilai 105 | Ditolak dengan pesan validasi[cite: 50] |
| TC05 | Invalid | File tidak ada | FileNotFoundError ditangani[cite: 50] |

## 10. Pembagian Tugas & Jadwal (Milestone)
* **PIC / Penanggung Jawab:** Dikerjakan secara mandiri (Individu).
* **Jadwal:** Pertemuan 14 (Proposal & Rancangan) $ightarrow$ Antara P14-P15 (Implementasi Kode) $ightarrow$ Pertemuan 15 (Testing & Dokumentasi)[cite: 51].
