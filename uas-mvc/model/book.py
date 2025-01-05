import sqlite3

class perpus:
    def __init__(self):
        self.conn = sqlite3.connect("perpus.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        # Buat tabel buku jika belum ada
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                status TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def tambah_buku(self, judul, penulis):
        # Tambahkan buku ke database
        self.cursor.execute("""
            INSERT INTO books (title, author, status) 
            VALUES (?, ?, ?)
        """, (judul, penulis, "tersedia"))
        self.conn.commit()

    def tampil_buku(self):
        # Ambil semua buku dari database
        self.cursor.execute("SELECT title, author, status FROM books")
        return self.cursor.fetchall()

    def ubah_buku(self, judul_sebelumnya, judul_baru, penulis_baru):
        # Edit buku berdasarkan judul lama
        self.cursor.execute("""
            UPDATE books
            SET title = ?, author = ?
            WHERE title = ?
        """, (judul_baru, penulis_baru, judul_sebelumnya))
        if self.cursor.rowcount == 0:
            return f"Buku dengan judul '{judul_sebelumnya}' tidak ditemukan."
        self.conn.commit()
        return f"Buku '{judul_sebelumnya}' berhasil diperbarui menjadi '{judul_baru}'."

    def hapus_buku(self, judul):
        # Hapus buku berdasarkan judul
        self.cursor.execute("DELETE FROM books WHERE title = ?", (judul,))
        if self.cursor.rowcount == 0:
            return f"Buku dengan judul '{judul}' tidak ditemukan."
        self.conn.commit()
        return f"Buku '{judul}' berhasil dihapus."

    def pinjam_buku(self, judul):
        # Pinjam buku (ubah status menjadi 'dipinjam')
        self.cursor.execute("""
            SELECT status FROM books WHERE title = ?
        """, (judul,))
        book = self.cursor.fetchone()
        if not book:
            return f"Buku dengan judul '{judul}' tidak ditemukan."
        if book[0] == "dipinjam":
            return f"Buku '{judul}' sedang dipinjam."
        self.cursor.execute("""
            UPDATE books
            SET status = 'dipinjam'
            WHERE title = ?
        """, (judul,))
        self.conn.commit()
        return f"Buku '{judul}' berhasil dipinjam."

    def buku_kembali(self, judul):
        # Mengembalikan buku (ubah status menjadi 'tersedia')
        self.cursor.execute("""
            SELECT status FROM books WHERE title = ?
        """, (judul,))
        book = self.cursor.fetchone()
        if not book:
            return f"Buku dengan judul '{judul}' tidak ditemukan."
        if book[0] == "tersedia":
            return f"Buku '{judul}' sudah tersedia dan tidak perlu dikembalikan."
        self.cursor.execute("""
            UPDATE books
            SET status = 'tersedia'
            WHERE title = ?
        """, (judul,))
        self.conn.commit()
        return f"Buku '{judul}' berhasil dikembalikan dan sekarang tersedia."

    def __del__(self):
            self.conn.close()
