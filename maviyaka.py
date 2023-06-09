from çalışan import Calisan


class Maviyaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas)
        self.__yipranma_payi = yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def zam_hakki(self):
        if self.get_tecrube() < 24:
            yeni_maas = self.get_maas() * (100 + self.__yipranma_payi * 10) / 100
            return yeni_maas
        elif 24 <= self.get_tecrube() < 48 and self.get_maas() < 15000:
            yeni_maas = self.get_maas() * (100 + ((self.get_maas() % self.get_tecrube()) / 2 + (self.__yipranma_payi * 10))) / 100
            return yeni_maas
        elif self.get_tecrube() >= 48 and self.get_maas() < 25000:
            yeni_maas = self.get_maas() * (100 + ((self.get_maas() % self.get_tecrube()) / 3 + (self.__yipranma_payi * 10))) / 100
            return yeni_maas

    def __str__(self):
        return f"Çalışanın adı-soyadı:{self.get_ad()} {self.get_soyad()} \nÇalışanın tecrübesei: {self.get_tecrube()} \
               \nÇalışanın yeni maaşı:{self.zam_hakki()} "
