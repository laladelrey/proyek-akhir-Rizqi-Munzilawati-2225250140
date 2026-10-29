# Modul Data I/O (Membaca dan Menulis File)
def baca_data_nilai(path_file):
    """Membaca data dari file teks baris per baris."""
    data_mentah = []
    try:
        with open(path_file, 'r', encoding='utf-8') as f:
            for baris in f:
                bersih = baris.strip()
                if bersih:
                    data_mentah.append(bersih)
        return data_mentah
    except FileNotFoundError:
        print(f"❌ Error: File '{path_file}' tidak ditemukan[cite: 50].")
        return []

def simpan_laporan(path_output, teks):
    """Menyimpan laporan ke dalam file di folder output."""
    try:
        with open(path_output, 'w', encoding='utf-8') as f:
            f.write(teks)
        print(f"✅ Laporan berhasil disimpan ke '{path_output}'")
    except Exception as e:
        print(f"❌ Gagal menyimpan laporan: {e}")