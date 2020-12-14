import pandas as pd,os

class absensi:
    def __init__(self):
        self.masuk = 0
        self.tidak_masuk = 0
        self.data_siswa = {}
        self.nama = []
        self.status = []
    def tambah(self,nama,status):
        self.nama.append(nama)
        if status == 1:
            self.masuk += 1
            self.status.append("Masuk")
        elif status == 2:
            self.tidak_masuk += 1
            self.status.append("Tidak Masuk")
    def hasil(self):
        print("="*50)
        self.data_siswa['Nama Siswa'] = self.nama
        self.data_siswa['Masuk/Tidak'] = self.status
        print(pd.DataFrame(self.data_siswa))
        print("="*50)
        print("Jumlah Siswa/i Masuk :",self.masuk)
        print("Jumlah Siswa/i Tidak Masuk :",self.tidak_masuk)

os.system("cls" if os.name == "nt" else "clear")
print("\tAplikasi Absensi Siswa/i")
aplikasi = absensi()
isi = open(input("\n\nmasukkan file list siswa/i : ")).read().splitlines()
for murid in isi:
    print("~"*50)
    print("Nama :",murid)
    print("1. Masuk | 2. Tidak Masuk")
    stat = int(input("nomor : "))
    if stat == 1:
        status = 1
    elif stat == 2:
        status = 2
    aplikasi.tambah(murid,status)
aplikasi.hasil()
