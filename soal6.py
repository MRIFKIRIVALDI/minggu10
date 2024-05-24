class Perpustakaan:
    def __init__(self):
        self.buku = []
        self.mahasiswa = []
        self.peminjam = []

    def tambah_buku(self, no_isbn, judul, pengarang, halaman, deskripsi, stok, booked):
        buku_baru = {
            'no_isbn': no_isbn,
            'judul': judul,
            'pengarang': pengarang,
            'halaman': halaman,
            'deskripsi': deskripsi,
            'stok': stok,
            'booked': booked
        }
        self.buku.append(buku_baru)

    def tambah_mahasiswa(self, nama, nim, nomerhp, alamat):
        mahasiswa_baru = {
            'nama': nama,
            'nim': nim,
            'nomerhp': nomerhp,
            'alamat': alamat
        }
        self.mahasiswa.append(mahasiswa_baru)

    def pinjam_buku(self, nim, no_isbn, tanggal_pinjam, tanggal_kembali, status):
        peminjaman = {
            'nim': nim,
            'no_isbn': no_isbn,
            'tanggal_pinjam': tanggal_pinjam,
            'tanggal_kembali': tanggal_kembali,
            'status': status
        }
        self.peminjam.append(peminjaman)

    def tampilkan_buku(self):
        for buku in self.buku:
            print("ISBN:", buku['no_isbn'])
            print("Judul:", buku['judul'])
            print("Pengarang:", buku['pengarang'])
            print("Halaman:", buku['halaman'])
            print("Deskripsi:", buku['deskripsi'])
            print("Stok:", buku['stok'])
            print("Booked:", buku['booked'])
            print()

    def tampilkan_mahasiswa(self):
        for mhs in self.mahasiswa:
            print("Nama:", mhs['nama'])
            print("NIM:", mhs['nim'])
            print("Nomor HP:", mhs['nomerhp'])
            print("Alamat:", mhs['alamat'])
            print()

    def tampilkan_peminjaman(self):
        for pinjam in self.peminjam:
            print("NIM:", pinjam['nim'])
            print("ISBN:", pinjam['no_isbn'])
            print("Tanggal Pinjam:", pinjam['tanggal_pinjam'])
            print("Tanggal Kembali:", pinjam['tanggal_kembali'])
            print("Status:", pinjam['status'])
            print()



perpustakaan = Perpustakaan()

# Menambahkan buku
perpustakaan.tambah_buku("978-3-16-148410-0", "Safinatunnaja", "Syeh Salim Bin Samir", 118, "Buku tentang fikih islam", 10, 0)
perpustakaan.tambah_buku("978-3-16-148411-0", "Jurumiyyah", "Syeh Asson Hajj", 56, "Ilmu Nahwu Dasar", 5, 0)

# Menambahkan mahasiswa
perpustakaan.tambah_mahasiswa("Rijal", "20230040155", "08123456789", "Jl. Cendana No. 10")
perpustakaan.tambah_mahasiswa("Yusuf", "20230040124", "08234567890", "Jl. Kenanga No. 5")

# Melakukan peminjaman
perpustakaan.pinjam_buku("20230040155", "978-3-16-148410-0", "2024-05-23", "2024-06-06", "Dipinjam")
perpustakaan.pinjam_buku("20230040124", "978-3-16-148411-0", "2024-05-23", "2024-06-06", "Dipinjam")

# Menampilkan informasi buku, mahasiswa, dan peminjaman
print("Informasi Buku:")
perpustakaan.tampilkan_buku()

print("Informasi Mahasiswa:")
perpustakaan.tampilkan_mahasiswa()

print("Informasi Peminjaman:")
perpustakaan.tampilkan_peminjaman()
