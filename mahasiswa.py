class Mahasiswa:
    def __init__(self, nama, nim):
        # Constructor: dijalankan saat objek dibuat
        self.__nama = nama            # atribut private untuk menyimpan nama
        self.__nim = nim              # atribut private untuk menyimpan NIM
        self.__nilai_tugas = 0        # nilai tugas awal = 0
        self.__nilai_uts = 0          # nilai UTS awal = 0
        self.__nilai_uas = 0          # nilai UAS awal = 0
        self.__nilai_akhir = 0        # nilai akhir awal = 0

    def set_nilai(self, tugas, uts, uas):
        # method untuk mengisi nilai
        self.__nilai_tugas = tugas    # simpan nilai tugas
        self.__nilai_uts = uts        # simpan nilai UTS
        self.__nilai_uas = uas        # simpan nilai UAS

    def hitung_nilai_akhir(self):
        # method untuk menghitung nilai akhir
        self.__nilai_akhir = (
            self.__nilai_tugas * 0.3 +   # bobot tugas 30%
            self.__nilai_uts * 0.3 +     # bobot UTS 30%
            self.__nilai_uas * 0.4       # bobot UAS 40%
        )

    def get_nilai_akhir(self):
        # method untuk mengambil nilai akhir dari luar class
        return self.__nilai_akhir

    def get_grade(self):
        # method untuk menentukan grade berdasarkan nilai akhir
        if self.__nilai_akhir >= 85:
            return "A"
        elif self.__nilai_akhir >= 70:
            return "B"
        elif self.__nilai_akhir >= 60:
            return "C"
        else:
            return "D"
        
    def get_grade_desc(self):
        grade = self.get_grade()

        if grade == "A":
            return "Sangat Baik (85–100)"
        elif grade == "B":
            return "Baik (70–84)"
        elif grade == "C":
            return "Cukup (60–69)"
        else:
            return "Kurang (<60)"

    def is_lulus(self):
        # method untuk mengecek apakah lulus atau tidak
        return self.__nilai_akhir >= 60  # True jika >=60, False jika tidak

    def keterangan_lulus(self):
        if self.is_lulus():
            return "Lulus"
        else:
            return "Tidak Lulus"
    
    def info(self):
        # method untuk menampilkan informasi mahasiswa
        print(self.__nama, self.__nim, self.__nilai_akhir, self.get_grade())