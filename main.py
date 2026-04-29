# mengimpor class mahasiswa dari file mahasiswa.py
from mahasiswa import Mahasiswa

#<<<<<<< HEAD
m1 = Mahasiswa("Depi", "23001") 
#>>>>>>> 3477ed7 (ini komentar)
m2 = Mahasiswa("Gadis", "23002")
m3 = Mahasiswa("Chintya", "23003")

# mengisi nilai tugas, uts, dan uas mahasiswa
m1.set_nilai(80, 85, 90)
m2.set_nilai(70, 75, 80)
m3.set_nilai(60, 65, 70)

# menghitung nilai akhir mahasiswa 
m1.hitung_nilai_akhir()
m2.hitung_nilai_akhir()
m3.hitung_nilai_akhir()

# menampilkan hasil mahasiswa
print("DATA MAHASISWA")
m1.info()
m2.info()
m3.info()
#===

# tampilkan data + keterangan lulus langsung
print("keterangan lulus")
for mhs in [m1, m2, m3]:
    status = "Lulus" if mhs.is_lulus() else "Tidak Lulus"
    print(mhs._Mahasiswa__nama, mhs.get_nilai_akhir(), status)

