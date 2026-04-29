class Mahasiswa:
    def __init__(self, nama, nim):
        self.__nama = nama
        self.__nim = nim
        self.__nilai_tugas = 0
        self.__nilai_uts = 0
        self.__nilai_uas = 0
        self.__nilai_akhir = 0

    def set_nilai(self, tugas, uts, uas):
        self.__nilai_tugas = tugas
        self.__nilai_uts = uts
        self.__nilai_uas = uas

    def hitung_nilai_akhir(self):
        self.__nilai_akhir = (
            self.__nilai_tugas * 0.3 +
            self.__nilai_uts * 0.3 +
            self.__nilai_uas * 0.4
        )

    def get_nilai_akhir(self):
        return self.__nilai_akhir

    def get_grade(self):
        if self.__nilai_akhir >= 85:
            return "A"
        elif self.__nilai_akhir >= 70:
            return "B"
        elif self.__nilai_akhir >= 60:
            return "C"
        else:
            return "D"

    def is_lulus(self):
        return self.__nilai_akhir >= 60

    def info(self):
        print(self.__nama, self.__nim, self.__nilai_akhir, self.get_grade())