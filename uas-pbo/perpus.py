import json 

class Perpus:
    def __init__(self):
        self.buku_list = self.muat_buku()  # untuk menyimpan list buku 

    def simpan_buku(self):
        with open("buku.json", "w") as f:
            json.dump(self.buku_list, f)

    def muat_buku(self):
        try:
            with open("buku.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []  # jika file tidak ada, mulai dengan list kosong

    def tambah_buku(self, judul, penulis):
        self.buku_list.append({"judul": judul, "penulis": penulis, "status": "tersedia"})
        self.simpan_buku()  # untuk menyimpan buku setelah ditambahkan
        
    def tampil_buku(self):
        return self.buku_list

    def ubah_buku(self, judul, judul_baru, penulis_baru):
        for buku in self.buku_list:
            if buku["judul"] == judul:
                buku["judul"] = judul_baru
                buku["penulis"] = penulis_baru
                self.simpan_buku()  # untuk menyimpan perubahan data buku setelah di edit 
                return f"Buku '{judul}' berhasil diubah menjadi '{judul_baru}'."
        return "Buku tidak ditemukan."

    def hapus_buku(self, judul):
        for buku in self.buku_list:
            if buku["judul"] == judul:
                self.buku_list.remove(buku)
                self.simpan_buku()  # untuk menyimpan perubahan data buku setelah di hapus
                return f"Buku '{judul}' berhasil dihapus."
        return "Buku tidak ditemukan."

    def pinjam_buku(self, judul):
        for buku in self.buku_list:
            if buku["judul"] == judul and buku["status"] == "tersedia":
                buku["status"] = "dipinjam"
                self.simpan_buku()  # untuk menyimpan data buku setelah buku dipinjam 
                return f"Buku '{judul}' berhasil dipinjam."
        return f"Buku '{judul}' tidak tersedia untuk dipinjam."

    def buku_kembali(self, judul):
        for buku in self.buku_list:
            if buku["judul"] == judul and buku["status"] == "dipinjam":
                buku["status"] = "tersedia"
                self.simpan_buku()  # untuk menyimpan data buku setelah buku dikembalikan
                return f"Buku '{judul}' berhasil dikembalikan."
        return f"Buku '{judul}' tidak ditemukan atau tidak sedang dipinjam."
