from insan import Insan


class Issiz(Insan):

    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, statu, gecmis_tecrube):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__statu = statu
        self.__gecmis_tecrube = gecmis_tecrube
        self.__kutuphane = [gecmis_tecrube[0], gecmis_tecrube[1], gecmis_tecrube[2]]

    def set_statu(self, statu):
        self.__statu = statu

    def set_gecmis_tecrube(self, gecmis_tecrube):
        self.__gecmis_tecrube = gecmis_tecrube

    def get_statu(self):
        return self.__statu

    def get_gecmis_tecrube(self):
        return self.__gecmis_tecrube

    def statu_bul(self, gecmis_tecrube):

        gecmis_tecrube[0] = gecmis_tecrube[0] * 20 / 100
        gecmis_tecrube[1] = gecmis_tecrube[1] * 35 / 100
        gecmis_tecrube[2] = gecmis_tecrube[2] * 45 / 100
        gecmis_tecrube_depo = [gecmis_tecrube[0], gecmis_tecrube[1], gecmis_tecrube[2]]
        if max(gecmis_tecrube_depo) == gecmis_tecrube[0]:
            self.__statu = "Mavi Yaka"
        elif max(gecmis_tecrube_depo) == gecmis_tecrube[1]:
            self.__statu = "Beyaz Yaka"
        elif max(gecmis_tecrube_depo) == gecmis_tecrube[2]:
            self.__statu = "Yönetici"
        return self.__statu

    def __str__(self):
        return f"Çalışanın adı-soyadı:{self.get_ad()} {self.get_soyad()}  \
               \nÇalışanın en uygun statüsü:{self.statu_bul(self.__gecmis_tecrube)} "





