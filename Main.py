import numpy as np
import pandas as pd
from insan import Insan
from işsiz import Issiz
from çalışan import Calisan
from maviyaka import Maviyaka
from beyazyaka import Beyazyaka

insan1 = Insan(15812447902, "Ayşe", "Kuyu", 34, "Kadın", "T.C.")
insan2 = Insan(23721009216, "Damla", "Uyan", 28, "Kadın", "T.C.")
issiz1 = Issiz(21859230566, "Mehmet", "Taş", 43, "Erkek", "T.C.", "", [18, 25, 7])
issiz2 = Issiz(15823054173, "Büşra", "Yıldırım", 36, "Kadın", "T.C.", "", [13, 12, 0])
issiz3 = Issiz(45793125780, "Ahmet", "Yıldız", 33, "Erkek", "T.C.", "", [25, 15, 8])
calisan1 = Calisan(53921029325, "Suna", "Ünlü", 26, "Kadın", "T.C.", "teknoloji", 35, 14000, 0)
calisan2 = Calisan(41259923183, "Kazım", "Tatlıcı", 30, "Erkek", "T.C.", "inşaat", 42, 14500, 0)
calisan3 = Calisan(79423897238, "Kerem", "Ün", 36, "Erkek", "T.C.", "muhasebe", 68, 23000, 0)
mavi_yaka1 = Maviyaka(47383901094, "Aslı", "Güneş", 35, "Kadın", "T.C.", "inşaat", 73, 20000, 0, 0.6)
mavi_yaka2 = Maviyaka(63271793195, "Merve", "Gülen", 29, "Kadın", "T.C.", "teknoloji", 50, 15500, 0, 0.1)
mavi_yaka3 = Maviyaka(59328106922, "Hüseyin", "Gümüş", 38, "Erkek", "T.C.", "inşaat", 96, 24500, 0, 0.4)
beyaz_yaka1 = Beyazyaka(58301085324, "Enes", "Kara", 49, "Erkek", "T.C.", "muhasebe", 151, 24800, 0, 3000)
beyaz_yaka2 = Beyazyaka(98120584294, "Beyza", "Terzi", 32, "Kadın", "T.C.", "muhasebe", 79, 19900, 0, 1800)
beyaz_yaka3 = Beyazyaka(56373810247, "Seray", "Şaşı", 37, "Kadın", "T.C.", "teknoloji", 90, 23200, 0, 2500)

kutuphane = {"Nesne değeri": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka",
                                     "Mavi Yaka", "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"],
                    "T.C.No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(),
                                mavi_yaka1.get_tc_no(), mavi_yaka2.get_tc_no(), mavi_yaka3.get_tc_no(),
                                beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
                    "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(),
                           mavi_yaka1.get_ad(), mavi_yaka2.get_ad(), mavi_yaka3.get_ad(),
                           beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
                    "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(),
                              mavi_yaka1.get_soyad(), mavi_yaka2.get_soyad(), mavi_yaka3.get_soyad(),
                              beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
                    "Yaş": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(),
                            mavi_yaka1.get_yas(), mavi_yaka2.get_yas(), mavi_yaka3.get_yas(),
                            beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
                    "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(),
                                 mavi_yaka1.get_cinsiyet(), mavi_yaka2.get_cinsiyet(), mavi_yaka3.get_cinsiyet(),
                                 beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
                    "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(),
                              mavi_yaka1.get_uyruk(), mavi_yaka2.get_uyruk(), mavi_yaka3.get_uyruk(),
                              beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
                    "Sektör": [calisan1.get_sektor("teknoloji"), calisan2.get_sektor("inşaat"),
                               calisan3.get_sektor("muhasebe"),
                               mavi_yaka1.get_sektor("inşaat"), mavi_yaka2.get_sektor("teknoloji"),
                               mavi_yaka3.get_sektor("inşaat"),
                               beyaz_yaka1.get_sektor("muhasebe"), beyaz_yaka2.get_sektor("muhasebe"),
                               beyaz_yaka3.get_sektor("teknoloji")],
                    "Tecrübe(Ay)": [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(),
                                    mavi_yaka1.get_tecrube(), mavi_yaka2.get_tecrube(), mavi_yaka3.get_tecrube(),
                                    beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
                    "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(),
                             mavi_yaka1.get_maas(), mavi_yaka2.get_maas(), mavi_yaka3.get_maas(),
                             beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
                    "Yıpranma Payı": [np.nan, np.nan, np.nan, 0.6, 0.1, 0.4, np.nan, np.nan, np.nan],
                    "Teşvik Primi": [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, 3000, 1800, 2500],
                    "Yeni Maaş": [calisan1.zam_hakki(), calisan2.zam_hakki(), calisan3.zam_hakki(),
                                  mavi_yaka1.zam_hakki(), mavi_yaka2.zam_hakki(), mavi_yaka3.zam_hakki(),
                                  beyaz_yaka1.zam_hakki(), beyaz_yaka2.zam_hakki(), beyaz_yaka3.zam_hakki()]}

print(insan1, "\n")
print(insan2, "\n")
print(issiz1, "\n")
print(issiz2, "\n")
print(issiz3, "\n")
print(calisan1, "\n")
print(calisan2, "\n")
print(calisan3, "\n")
print(mavi_yaka1, "\n")
print(mavi_yaka2, "\n")
print(mavi_yaka3, "\n")
print(beyaz_yaka1, "\n")
print(beyaz_yaka2, "\n")
print(beyaz_yaka3, "\n")

df = pd.DataFrame(kutuphane)
print(df.to_string(), "\n")
print(pd.DataFrame(kutuphane, index=["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka","Mavi Yaka",
                                     "Beyaz Yaka", "Beyaz Yaka", "Beyaz Yaka"], columns=["Tecrübe(Ay)", "Yeni Maaş"]), "\n")
a = df.fillna(0).to_string()
print(a, "\n")

sayac = 0
for i in range(9):
    if df["Maaş"][i] >15000:
        sayac+=1
print(f"Maaşı 15000'den fazla olan kişi sayısı:{sayac} \n")

dat = df.sort_values(["Yeni Maaş"]).to_string()
print(dat, "\n")

abc = df.drop(df.columns[[0,1,4,5,6,8,9,10,11]], axis=1)
print(abc, "\n")






