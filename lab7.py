import sys

class DaftarNilai:
    """
    Class untuk mengelola daftar nilai mahasiswa.
    Data disimpan sebagai list of dictionaries: [{'nama': str, 'nilai': int}, ...]
    """
    def __init__(self):
        # List untuk menyimpan data mahasiswa (nama dan nilai)
        self.data = []
        print("Sistem Daftar Nilai berhasil diinisialisasi.")

    def tambah(self, nama, nilai):
        """Menambah data mahasiswa baru."""
        # Validasi sederhana nilai
        try:
            nilai = int(nilai)
            if not (0 <= nilai <= 100):
                print(f"Gagal menambah: Nilai {nilai} tidak valid. Nilai harus antara 0-100.")
                return False
        except ValueError:
            print("Gagal menambah: Nilai harus berupa angka.")
            return False

        # Cek apakah nama sudah ada (case-insensitive)
        if any(item['nama'].lower() == nama.lower() for item in self.data):
            print(f"Peringatan: Mahasiswa dengan nama '{nama}' sudah ada. Silakan gunakan fungsi Ubah.")
            return False

        mahasiswa = {'nama': nama, 'nilai': nilai}
        self.data.append(mahasiswa)
        print(f"Data '{nama}' dengan nilai {nilai} berhasil ditambahkan.")
        return True

    def tampilkan(self):
        """Menampilkan semua data mahasiswa yang tersimpan."""
        if not self.data:
            print("Daftar nilai kosong.")
            return

        print("\n" + "="*40)
        print(f"{'No.':<5}{'Nama':<25}{'Nilai':<10}")
        print("="*40)
        
        # Sortir data berdasarkan nama
        data_sorted = sorted(self.data, key=lambda x: x['nama'])
        
        for i, mhs in enumerate(data_sorted, 1):
            print(f"{i:<5}{mhs['nama']:<25}{mhs['nilai']:<10}")
        print("="*40)
        print(f"Total Mahasiswa: {len(self.data)}")

    def hapus(self, nama):
        """Menghapus data mahasiswa berdasarkan nama."""
        initial_length = len(self.data)
        
        # Membuat list baru tanpa data yang namanya cocok
        self.data = [mhs for mhs in self.data if mhs['nama'].lower() != nama.lower()]
        
        if len(self.data) < initial_length:
            print(f"Data '{nama}' berhasil dihapus.")
            return True
        else:
            print(f"Gagal menghapus: Nama '{nama}' tidak ditemukan.")
            return False

    def ubah(self, nama, nilai_baru):
        """Mengubah nilai mahasiswa berdasarkan nama."""
        
        # Validasi nilai baru
        try:
            nilai_baru = int(nilai_baru)
            if not (0 <= nilai_baru <= 100):
                print(f"Gagal mengubah: Nilai baru {nilai_baru} tidak valid. Nilai harus antara 0-100.")
                return False
        except ValueError:
            print("Gagal mengubah: Nilai baru harus berupa angka.")
            return False

        # Mencari dan mengubah data
        data_ditemukan = False
        for mhs in self.data:
            if mhs['nama'].lower() == nama.lower():
                nilai_lama = mhs['nilai']
                mhs['nilai'] = nilai_baru
                print(f"Data '{mhs['nama']}' berhasil diubah. Nilai lama: {nilai_lama}, Nilai baru: {nilai_baru}.")
                data_ditemukan = True
                break
        
        if not data_ditemukan:
            print(f"Gagal mengubah: Nama '{nama}' tidak ditemukan.")
            return False
        return True

# --- Fungsi untuk Menu Interaktif ---
def jalankan_menu():
    """Menampilkan menu dan memproses input pengguna."""
    manajer_nilai = DaftarNilai()
    
    while True:
        print("\n==============================")
        print("MENU MANAJEMEN NILAI MAHASISWA")
        print("==============================")
        print("1. Tambah Data Mahasiswa")
        print("2. Tampilkan Daftar Nilai")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Keluar")
        print("------------------------------")
        
        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == '1':
            print("\n--- TAMBAH DATA ---")
            nama = input("Masukkan Nama Mahasiswa: ").strip()
            nilai = input("Masukkan Nilai: ").strip()
            if nama:
                manajer_nilai.tambah(nama, nilai)
            else:
                print("Nama tidak boleh kosong.")
        
        elif pilihan == '2':
            print("\n--- TAMPILKAN DATA ---")
            manajer_nilai.tampilkan()
            
        elif pilihan == '3':
            print("\n--- UBAH DATA ---")
            nama = input("Masukkan Nama Mahasiswa yang ingin diubah: ").strip()
            if nama:
                nilai_baru = input(f"Masukkan Nilai Baru untuk {nama}: ").strip()
                manajer_nilai.ubah(nama, nilai_baru)
            else:
                print("Nama tidak boleh kosong.")
            
        elif pilihan == '4':
            print("\n--- HAPUS DATA ---")
            nama = input("Masukkan Nama Mahasiswa yang ingin dihapus: ").strip()
            if nama:
                manajer_nilai.hapus(nama)
            else:
                print("Nama tidak boleh kosong.")

        elif pilihan == '5':
            print("\nTerima kasih. Program diakhiri.")
            sys.exit()
            
        else:
            print("Pilihan tidak valid. Silakan masukkan angka antara 1 sampai 5.")

# Memanggil fungsi menu saat program dijalankan
if __name__ == "__main__":
    jalankan_menu()