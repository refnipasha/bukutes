from datetime import datetime
from prettytable import PrettyTable 

# Daftar buku
buku = [
    {'judul': 'The Great Gatsby', 'penulis': 'F. Scott Fitzgerald', 'tahun': 1925, 'genre': 'Fiksi'},
    {'judul': 'To Kill a Mockingbird', 'penulis': 'Harper Lee', 'tahun': 1960, 'genre': 'Fiksi'},
    {'judul': '1984', 'penulis': 'George Orwell', 'tahun': 1949, 'genre': 'Fiksi Ilmiah'},
    {'judul': 'The Hunger Games', 'penulis': 'Suzanne Collins', 'tahun': 2008, 'genre': 'Fiksi Ilmiah'},
    {'judul': 'Pride and Prejudice', 'penulis': 'Jane Austen', 'tahun': 1813, 'genre': 'Romansa'}
]

# Tugas 1: Mengembalikan buku yang diterbitkan dalam 10 tahun terakhir
def ambil_buku(buku):
    tahun_sekarang = datetime.now().year
    return [b for b in buku if b['tahun'] >= (tahun_sekarang - 10)]

# Tugas 2: Fungsi pencarian
def cari_buku(buku, keyword):
    hasil = []
    for b in buku:
        if (keyword.lower() in b['judul'].lower()) or (keyword.lower() in b['genre'].lower()):
            hasil.append(b)
    return hasil

# Tampilkan buku menggunakan PrettyTable
def tampilkan_buku(buku):
    table = PrettyTable()
    table.field_names = ["Judul", "Penulis", "Tahun", "Genre"]
    
    for b in buku:
        table.add_row([b['judul'], b['penulis'], b['tahun'], b['genre']])
    
    print(table)

# Menampilkan semua buku
print("Buku yang Tersedia:")
tampilkan_buku(buku)

# Menampilkan buku terbaru
print("\nBuku Terbaru:")
tampilkan_buku(ambil_buku(buku))

# Input dari pengguna untuk pencarian
keyword = input("\nMasukkan kata kunci buku yang ingin dicari: ")
tampilkan_buku(cari_buku(buku, keyword))
