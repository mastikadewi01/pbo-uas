from perpus import Perpus
from view import View
from user import Admin, User

class Controller:
    def __init__(self):
        self.perpus = Perpus() # Objek dari kelas Perpus untuk mengakses operasi terkait buku
        self.view = View() # Objek dari kelas View untuk menampilkan antarmuka pengguna
        self.current_user = None # Objek yang mewakili pengguna saat ini (Admin atau User)
        self.users = {
            "admin": {"password": "admin_besti", "role": "admin"},
            "user": {"password": "user_besti", "role": "user"}
        }

    def login(self):
        while True:
            username, password = self.view.login_sistem()
            if username in self.users and self.users[username]["password"] == password:
                if self.users[username]["role"] == "admin":
                    self.current_user = Admin(username)
                else:
                    self.current_user = User(username)
                self.view.tampilkan_pesan(f"=================================================================")
                self.view.tampilkan_pesan(f"Login berhasil. Selamat datang di Perpustakaan Besti, {username}!")

                break
            else:
                self.view.tampilkan_pesan("Login gagal. Username atau password salah.")

    def menu_admin(self): #untuk menampilkan menu admin
        while True:
            print("\nMenu Admin:")
            print(self.current_user.show_menu())
            choice = input("Pilih menu: ")

            if choice == "1":
                judul, penulis = self.view.menambahkan_buku_baru()
                self.perpus.tambah_buku(judul, penulis)
                self.view.tampilkan_pesan(f"Buku '{judul}' berhasil ditambahkan.")
            elif choice == "2":
                buku = self.perpus.tampil_buku()
                self.view.tampilkan_buku(buku)
            elif choice == "3":
                judul = self.view.mencari_judul_buku()
                judul_baru, penulis_baru = self.view.mengedit_detail_buku()
                pesan = self.perpus.ubah_buku(judul, judul_baru, penulis_baru)
                self.view.tampilkan_pesan(pesan)
            elif choice == "4":
                judul = self.view.mencari_judul_buku()
                pesan = self.perpus.hapus_buku(judul)
                self.view.tampilkan_pesan(pesan)
            elif choice == "5":
                judul = self.view.mencari_judul_buku()
                pesan = self.perpus.pinjam_buku(judul)
                self.view.tampilkan_pesan(pesan)
            elif choice == "6":
                judul = self.view.mencari_judul_buku()
                pesan = self.perpus.buku_kembali(judul)
                self.view.tampilkan_pesan(pesan)
            elif choice == "7":
                print("Terima kasih telah menggunakan sistem perpustakaan.")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih kembali.")

    def menu_user(self): #untuk menampilkan menu user 
        while True:
            print("\nMenu User:")
            print(self.current_user.show_menu())
            choice = input("Pilih menu: ")

            if choice == "1":
                buku = self.perpus.tampil_buku()
                self.view.tampilkan_buku(buku)
            elif choice == "2":
                judul = self.view.mencari_judul_buku()
                pesan = self.perpus.pinjam_buku(judul)
                self.view.tampilkan_pesan(pesan)
            elif choice == "3":
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
        if self.current_user.role == "admin":
            self.menu_admin()
        elif self.current_user.role == "user":
            self.menu_user()

