from model.book import perpus
from view.view import View

class Controller:
    def __init__(self):
        self.perpus = perpus()
        self.view = View()
        self.current_user = None
        self.users = {
            "admin": {"password": "admin123", "role": "admin"},
            "user": {"password": "user123", "role": "user"}
        }

    def login(self):
        while True:
            username, password = self.view.login_sistem()
            if username in self.users and self.users[username]["password"] == password:
                self.current_user = {"username": username, "role": self.users[username]["role"]}
                self.view.tampilkan_pesan(f"Login berhasil. Selamat datang, {username}!")
                break
            else:
                self.view.tampilkan_pesan("Login gagal. Username atau password salah.")

    # daftar menu admin
    def menu_admin(self):  
        while True:
            print("\nMenu Admin:")
            print("1. Tambah Buku") 
            print("2. Tampilkan Buku")
            print("3. Edit Buku")
            print("4. Hapus Buku")
            print("5. Pinjam Buku")
            print("6. Kembalikan Buku") 
            print("7. Keluar")
            choice = input("Pilih menu: ")

            if choice == "1": # Logika untuk menambahkan buku
                judul, penulis = self.view.menambahkan_buku_baru()
                self.perpus.tambah_buku(judul, penulis)
                self.view.tampilkan_pesan(f"Buku '{judul}' berhasil ditambahkan.")

            elif choice == "2": # Logika untuk menampilkan buku
                buku = self.perpus.tampil_buku()
                self.view.tampilkan_buku(buku)

            elif choice == "3": # Logika untuk mengedit buku
                judul = self.view.mencari_judul_buku()
                judul_baru, penulis_baru = self.view.mengedit_detail_buku()
                pesan = self.perpus.ubah_buku(judul, judul_baru, penulis_baru)
                self.view.tampilkan_pesan(pesan)

            elif choice == "4": # Logika untuk menghapus buku
                judul = self.view.mencari_judul_buku()
                pesan = self.perpus.hapus_buku(judul)
                self.view.tampilkan_pesan(pesan)

            elif choice == "5": # Logika untuk meminjam buku
                judul = self.view.mencari_judul_buku()
                pesan = self.perpus.pinjam_buku(judul)
                self.view.tampilkan_pesan(pesan)

            elif choice == "6":  # Logika untuk pengembalian buku
                judul = self.view.mencari_judul_buku()
                pesan = self.perpus.buku_kembali(judul)
                self.view.tampilkan_pesan(pesan)

            elif choice == "7": 
                print("Terima kasih telah menggunakan sistem perpustakaan.")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")

    # daftar menu user
    def menu_user(self):
        while True:
            print("\nMenu User:")
            print("1. Tampilkan Buku")
            print("2. Pinjam Buku")
            print("3. Kembalikan Buku")  
            print("4. Keluar")
            choice = input("Pilih menu: ")

            if choice == "1": # Logika untuk menampilkan buku
                buku = self.perpus.tampil_buku()
                self.view.tampilkan_buku(buku)

            elif choice == "2": # Logika untuk meminjam buku
                judul = self.view.mencari_judul_buku()
                pesan = self.perpus.pinjam_buku(judul)
                self.view.tampilkan_pesan(pesan)

            elif choice == "3":  # Logika untuk pengembalian buku
                judul = self.view.mencari_judul_buku()
                pesan = self.perpus.buku_kembali(judul)
                self.view.tampilkan_pesan(pesan)

            elif choice == "4":
                print("Terima kasih telah menggunakan sistem perpustakaan.")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")

    def run(self):
        self.login()
        if self.current_user["role"] == "admin":
            self.menu_admin()
        elif self.current_user["role"] == "user":
            self.menu_user()
