class User:
    def __init__(self, username):
        self.username = username
        self.role = "user"

    def show_menu(self): #untuk menampilkan menu pilihan user
        return """
        1. Tampilkan Buku
        2. Pinjam Buku
        3. Kembalikan Buku
        4. Keluar
        """

class Admin(User):
    def __init__(self, username):
        super().__init__(username)
        self.role = "admin"

    def show_menu(self): #untuk menampilkan menu pilihan admin 
        return """
        1. Tambah Buku
        2. Tampilkan Buku
        3. Edit Buku
        4. Hapus Buku
        5. Pinjam Buku
        6. Kembalikan Buku
        7. Keluar
        """
