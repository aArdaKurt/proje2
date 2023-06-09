from insan import Insan


class Calisan(Insan):

    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas
        self.__yeni_maas = yeni_maas

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def set_maas(self, maas):
        self.__tecrube = maas

    def set_yeni_maas(self, yeni_maas):
        self.__yeni_maas = yeni_maas

    def get_sektor(self, sektor):
        if self.__sektor == "teknoloji":
            self.__sektor = sektor
            return self.__sektor
        elif self.__sektor == "muhasebe":
            self.__sektor = sektor
            return self.__sektor
        elif self.__sektor == "inşaat":
            self.__sektor = sektor
            return self.__sektor
        else:
            sektor = "diğer"
            self.__sektor = sektor
            return self.__sektor

    def get_tecrube(self):
        return self.__tecrube

    def get_maas(self):
        return self.__maas

    def get_yeni_maas(self):
        return self.__yeni_maas

    def zam_hakki(self):
        if self.__tecrube < 24:
            self.__maas += 0
            yeni_maas = self.__maas
            return yeni_maas
        elif 24 <= self.__tecrube < 48 and self.__maas < 15000:
            yeni_maas = self.__maas * (100 + (self.__maas % self.__tecrube)) / 100
            return yeni_maas
        elif self.__tecrube >= 48 and self.__maas < 25000:
            yeni_maas = self.__maas * (100 + (self.__maas % self.__tecrube) / 2) / 100
            return yeni_maas

    def __str__(self):
        return f"Çalışanın adı-soyadı:{self.get_ad()} {self.get_soyad()} \nÇalışanın tecrübesei: {self.get_tecrube()}  \
               \nÇalışanın yeni maaşı:{self.zam_hakki()}"



