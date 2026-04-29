from mahasiswa import Mahasiswa

m1 = Mahasiswa("Chen", "23001")
m2 = Mahasiswa("Budi", "23002")
m3 = Mahasiswa("Siti", "23003")

m1.set_nilai(80, 85, 90)
m2.set_nilai(70, 75, 80)
m3.set_nilai(60, 65, 70)

m1.hitung_nilai_akhir()
m2.hitung_nilai_akhir()
m3.hitung_nilai_akhir()

print("DATA MAHASISWA")
m1.info()
m2.info()
m3.info()