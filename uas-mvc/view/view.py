class View:
    # untuk menampilkan daftar buku di perpus
    def tampilkan_buku(self, buku):
        print("Daftar Buku di Perpustakaan:")
        print(buku)

    def tampilkan_pesan(self, pesan): 
        print(pesan)

    # untuk menambahkan buku baru
    def menambahkan_buku_baru(self):
        judul = input("Masukkan Judul Buku: ")
        penulis = input("Masukkan Penulis Buku: ")
        return judul, penulis

    # untuk mencari buku
    def mencari_judul_buku(self):
        judul = input("Masukkan Judul Buku: ")
        return judul

    # untuk mengedit buku yang sudah ada
    def mengedit_detail_buku(self):
        judul_baru = input("Masukkan Judul Baru: ")
        penulis_baru = input("Masukkan Penulis Baru: ")
        return judul_baru, penulis_baru

    def login_sistem(self):
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        return username, password
