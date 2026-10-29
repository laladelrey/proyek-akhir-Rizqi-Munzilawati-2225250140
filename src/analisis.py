# Modul Analisis Statistik dan Logika
BATAS_KKM = 60

def hitung_rata_rata(data_nilai):
    """Menghitung rata-rata dari list angka."""
    if not data_nilai:
        return 0.0
    return sum(data_nilai) / len(data_nilai)

def tentukan_status(nilai, kkm=BATAS_KKM):
    """Menentukan status tuntas atau belum tuntas berdasarkan KKM."""
    return "Tuntas" if nilai >= kkm else "Belum Tuntas"

def hitung_statistik(data_nilai):
    """Menghitung ringkasan statistik kelas."""
    if not data_nilai:
        return None
    
    tuntas_list = [n for n in data_nilai if n >= BATAS_KKM]
    
    return {
        "jumlah_siswa": len(data_nilai),
        "rata_rata": hitung_rata_rata(data_nilai),
        "minimum": min(data_nilai),
        "maksimum": max(data_nilai),
        "jumlah_tuntas": len(tuntas_list),
        "jumlah_belum_tuntas": len(data_nilai) - len(tuntas_list)
    }