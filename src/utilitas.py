# Modul Utilitas / Validasi Nilai
def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada pada rentang 0 sampai 100."""
    try:
        val = float(nilai)
        return 0 <= val <= 100
    except (ValueError, TypeError):
        return False