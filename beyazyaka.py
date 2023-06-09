from çalışan import Calisan


class Beyazyaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas,  yeni_maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yeni_maas)
        self.__tesvik_primi = tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def zam_hakki(self):
        if self.get_tecrube() < 24:
            yeni_maas = self.get_maas() + self.__tesvik_primi
            return yeni_maas
        elif 24 <= self.get_tecrube() < 48 and self.get_maas() < 15000:
            yeni_maas = self.get_maas() + (self.get_maas() % self.get_tecrube()) * 5 + self.__tesvik_primi
            return yeni_maas
        elif self.get_tecrube() >= 48 and self.get_maas() < 25000:
            yeni_maas = self.get_maas() + (self.get_maas() % self.get_tecrube()) * 4 + self.__tesvik_primi
            return yeni_maas

    def __str__(self):
        return f"Çalışanın adı-soyadı:{self.get_ad()} {self.get_soyad()} \nÇalışanın tecrübesei: {self.get_tecrube()}  \
               \nÇalışanın yeni maaşı:{self.zam_hakki()}"





