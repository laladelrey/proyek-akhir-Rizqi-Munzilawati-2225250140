# Program Utama (Main Program) dengan Pengujian (Test Case & Assert)
import os
from src.data_io import baca_data_nilai, simpan_laporan
from src.utilitas import validasi_nilai
from src.analisis import hitung_statistik, tentukan_status, hitung_rata_rata, BATAS_KKM

def jalankan_pengujian():
    """Menjalankan pengujian otomatis (Test Case) sesuai instruksi Pertemuan 15."""
    print("[LOG] Menjalankan pengujian test case...")
    
    # TC01: Normal
    assert hitung_rata_rata([70, 80, 90]) == 80.0, "TC01 Gagal"
    # TC02: Batas bawah
    assert validasi_nilai(0) == True, "TC02 Gagal"
    # TC03: Batas atas
    assert validasi_nilai(100) == True, "TC03 Gagal"
    # TC04: Invalid
    assert validasi_nilai(105) == False, "TC04 Gagal"
    
    print("[LOG] Semua pengujian utama LULUS (PASS)!\n")

def main():
    jalankan_pengujian()
    
    print("=" * 50)
    print("   PROGRAM REKAP & ANALISIS NILAI MATEMATIKA   ")
    print("=" * 50)
    
    path_file = os.path.join("data", "nilai_contoh.txt")
    data_mentah = baca_data_nilai(path_file)
    
    if not data_mentah:
        print("Menggunakan data cadangan...")
        data_mentah = ["80", "70", "90", "105", "50"]
        
    print(f"Data Mentah Diterima : {data_mentah}")
    
    # Validasi data
    data_valid = []
    for item in data_mentah:
        if validasi_nilai(item):
            data_valid.append(float(item))
        else:
            print(f"⚠️ Peringatan: Nilai '{item}' diabaikan (tidak valid).")
            
    if not data_valid:
        print("❌ Tidak ada data valid untuk diproses.")
        return

    # Hitung Statistik
    stats = hitung_statistik(data_valid)
    
    # Format Laporan
    laporan = f"""=== LAPORAN STATISTIK KELAS ===
Total Siswa Valid    : {stats['jumlah_siswa']}
Nilai Rata-rata      : {stats['rata_rata']:.2f}
Nilai Terendah       : {stats['minimum']}
Nilai Tertinggi      : {stats['maksimum']}
Jumlah Tuntas (>={BATAS_KKM}) : {stats['jumlah_tuntas']}
Jumlah Belum Tuntas  : {stats['jumlah_belum_tuntas']}
"""
    
    print("\n" + laporan)
    print("Detail Status Siswa:")
    for idx, val in enumerate(data_valid, start=1):
        status = tentukan_status(val)
        print(f"  - Siswa {idx:02d} | Nilai: {val:>5.1f} | Status: {status}")
        
    # Simpan laporan
    os.makedirs("output", exist_ok=True)
    simpan_laporan(os.path.join("output", "laporan.txt"), laporan)
    print("=" * 50)

if __name__ == "__main__":
    main()