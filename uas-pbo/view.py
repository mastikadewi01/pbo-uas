class View:
    def login_sistem(self): # untuk meminta input username dan password dari pengguna saat login
        print("Silahkan Login untuk Masuk ke Perpustakaan Besti")
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        return username, password

    def tampilkan_pesan(self, pesan): # untuk menampilkan pesan kepada pengguna
        print(pesan)

    def menambahkan_buku_baru(self): # untuk menambahkan buku baru 
        judul = input("Masukkan judul buku: ")
        penulis = input("Masukkan penulis buku: ")
        return judul, penulis

    def tampilkan_buku(self, buku):  # untuk menampilkan buku yang ada di perpustakaan 
        if buku:
            for idx, b in enumerate(buku, 1):
                print(f"{idx}. {b['judul']} oleh {b['penulis']} - Status: {b['status']}")
        else:
            print("Tidak ada buku yang tersedia.")

    def mencari_judul_buku(self): # untuk mencari buku berdasarkan judul 
        return input("Masukkan judul buku yang dicari: ")

    def mengedit_detail_buku(self): # untuk mengedit data buku di perpustakaan
        judul_baru = input("Masukkan judul buku yang baru: ")
        penulis_baru = input("Masukkan penulis buku yang baru: ")
        return judul_baru, penulis_baru
