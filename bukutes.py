from prettytable import PrettyTable 

# Daftar buku
buku = [
    {'judul': 'The Great Gatsby', 'penulis': 'F. Scott Fitzgerald', 'tahun': 1925, 'genre': 'Fiksi'},
    {'judul': 'To Kill a Mockingbird', 'penulis': 'Harper Lee', 'tahun': 1960, 'genre': 'Fiksi'},
    {'judul': '1984', 'penulis': 'George Orwell', 'tahun': 1949, 'genre': 'Fiksi Ilmiah'},
    {'judul': 'The Hunger Games', 'penulis': 'Suzanne Collins', 'tahun': 2008, 'genre': 'Fiksi Ilmiah'},
    {'judul': 'Pride and Prejudice', 'penulis': 'Jane Austen', 'tahun': 1813, 'genre': 'Romansa'}
]

# Membuat tabel
tabel = PrettyTable(["Judul", "Penulis", "Tahun", "Genre"])

# Menambahkan data ke tabel
for b in buku:
    tabel.add_row([b['judul'], b['penulis'], b['tahun'], b['genre']])

# Menampilkan tabel
print(tabel)
