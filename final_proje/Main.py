import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

#Yeni terminalden "pandas" kütüphanesini indirdim

try:
    # Insan sınıfı için 2 nesne oluşturulması ve bilgilerin yazdırılması
    insan1 = Insan("1234567890", "Ahmet", "Yılmaz", 30, "Erkek", "Türk")
    insan2 = Insan("9876543210", "Ayşe", "Kaya", 25, "Kadın", "Türk")
    print("----- İnsanlar -----")
    print(insan1)
    print(insan2)
    print("--------------------")

    # Issiz sınıfı için 3 nesne oluşturulması ve bilgilerin yazdırılması
    issiz1 = Issiz({"mavi yaka": 2, "muhasabe": 5, "inşaat": 3})
    issiz2 = Issiz({"beyaz yaka": 4, "muhasabe": 6, "inşaat": 2})
    issiz3 = Issiz({"yönetici": 3, "muhasabe": 7, "inşaat": 4})

    print("----- İşsizler -----")
    print("İşsiz 1: Tecrubeler:", issiz1.get_tecrubeler(), "Statü:", issiz1.get_statu())
    print("İşsiz 2: Tecrubeler:", issiz2.get_tecrubeler(), "Statü:", issiz2.get_statu())
    print("İşsiz 3: Tecrubeler:", issiz3.get_tecrubeler(), "Statü:", issiz3.get_statu())
    print("--------------------")


    # Calisan sınıfı için 3 nesne oluşturulması ve bilgilerin yazdırılması
    calisan1 = Calisan("teknoloji", 3, 12000)
    calisan2 = Calisan("muhasabe", 5, 18000)
    calisan3 = Calisan("inşaat", 7, 25000)
    print("----- Çalışanlar -----")
    print(calisan1)
    print(calisan2)
    print(calisan3)
    print("---------------------")

    # MaviYaka sınıfı için 3 nesne oluşturulması ve bilgilerin yazdırılması
    mavi_yaka1 = MaviYaka(0.2)
    mavi_yaka2 = MaviYaka(0.3)
    mavi_yaka3 = MaviYaka(0.4)
    print("----- Mavi Yaka -----")
    print(mavi_yaka1)
    print(mavi_yaka2)
    print(mavi_yaka3)
    print("--------------------")

    # BeyazYaka sınıfı için 3 nesne oluşturulması ve bilgilerin yazdırılması
    beyaz_yaka1 = BeyazYaka(500)
    beyaz_yaka2 = BeyazYaka(1000)
    beyaz_yaka3 = BeyazYaka(1500)
    print("----- Beyaz Yaka -----")
    print(beyaz_yaka1)
    print(beyaz_yaka2)
    print(beyaz_yaka3)
    print("---------------------")
    

    # DataFrame oluşturma
    data = {
        'nesne': ['Çalışan'] * 3 + ['Mavi Yaka'] * 3 + ['Beyaz Yaka'] * 3,
        'tc_no': [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(),
                  0, 0, 0,
                  beyaz_yaka1.get_tc_no(), beyaz_yaka2.get_tc_no(), beyaz_yaka3.get_tc_no()],
        'ad': [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(),
               0, 0, 0,
               beyaz_yaka1.get_ad(), beyaz_yaka2.get_ad(), beyaz_yaka3.get_ad()],
        'soyad': [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(),
                  0, 0, 0,
                  beyaz_yaka1.get_soyad(), beyaz_yaka2.get_soyad(), beyaz_yaka3.get_soyad()],
        'yas': [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(),
                0, 0, 0,
                beyaz_yaka1.get_yas(), beyaz_yaka2.get_yas(), beyaz_yaka3.get_yas()],
        'cinsiyet': [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(),
                     0, 0, 0,
                     beyaz_yaka1.get_cinsiyet(), beyaz_yaka2.get_cinsiyet(), beyaz_yaka3.get_cinsiyet()],
        'uyruk': [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(),
                  0, 0, 0,
                  beyaz_yaka1.get_uyruk(), beyaz_yaka2.get_uyruk(), beyaz_yaka3.get_uyruk()],
        'sektor': [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(),
                   0, 0, 0,
                   beyaz_yaka1.get_sektor(), beyaz_yaka2.get_sektor(), beyaz_yaka3.get_sektor()],
          'tecrube': [calisan1.get_tecrube(), calisan2.get_tecrube(), calisan3.get_tecrube(),
                   0, 0, 0,
                   beyaz_yaka1.get_tecrube(), beyaz_yaka2.get_tecrube(), beyaz_yaka3.get_tecrube()],
        'maas': [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(),
                 0, 0, 0,
                 beyaz_yaka1.get_maas(), beyaz_yaka2.get_maas(), beyaz_yaka3.get_maas()],
        'yipranma_payi': [calisan1.get_yipranma_payi(), calisan2.get_yipranma_payi(), calisan3.get_yipranma_payi(),
                          0, 0, 0,
                          beyaz_yaka1.get_yipranma_payi(), beyaz_yaka2.get_yipranma_payi(), beyaz_yaka3.get_yipranma_payi()],
        'tesvik_primi': [calisan1.get_tesvik_primi(), calisan2.get_tesvik_primi(), calisan3.get_tesvik_primi(),
                         0, 0, 0,
                         beyaz_yaka1.get_tesvik_primi(), beyaz_yaka2.get_tesvik_primi(), beyaz_yaka3.get_tesvik_primi()],
        'yeni_maas': [calisan1.yeni_maas(), calisan2.yeni_maas(), calisan3.yeni_maas(),
                      mavi_yaka1.yeni_maas(), mavi_yaka2.yeni_maas(), mavi_yaka3.yeni_maas(),
                      beyaz_yaka1.yeni_maas(), beyaz_yaka2.yeni_maas(), beyaz_yaka3.yeni_maas()]
    }

    df = pd.DataFrame(data)

    # a) Boş değerlerin 0 olarak atanması
    df.fillna(0, inplace=True)

    # b) Gruplama ve ortalamaların hesaplanması
    grouped = df.groupby('nesne').agg({'tecrube': 'mean', 'yeni_maas': 'mean'})
    print("----- Gruplama ve Ortalamalar -----")
    print(grouped)
    print("-----------------------------------")

    # c) Maaşı 15000TL üzerinde olanların toplam sayısının bulunması
    # chatgpt yardımı ile bulabildim bunu
    above_15000 = df[df['maas'] > 15000].shape[0]
    print("Maaşı 15000TL üzerinde olanların toplam sayısı:", above_15000)

    # d) Yeni maaşa göre DataFrame'in küçükten büyüğe sıralanması ve yazdırılması
    sorted_df = df.sort_values('yeni_maas')
    print("--- Yeni Maaşa Göre Sıralı DataFrame ---")
    print(sorted_df)
    print("-------------------------------------------")
    
    # e) Tecrübesi 3 seneden fazla olan Beyaz yakalıların bulunması ve yazdırılması
    beyaz_yaka_tecrube_3 = df[(df['nesne'] == 'Beyaz Yaka') & (df['tecrube'] > 3)]
    print("----- Tecrübesi 3 Seneden Fazla Olan Beyaz Yakalılar -----")
    print(beyaz_yaka_tecrube_3)
    print("--------------------------------------------------------")

    # f) Yeni maaşı 10000 TL üzerinde olan 2-5 satır arası Beyaz Yakalıları seçme ve yazdırma
    yeni_maas_10000_ust = df[df['yeni_maas'] > 10000]
    selected_rows = yeni_maas_10000_ust.loc[2:5, ['tc_no', 'yeni_maas']]
    print("----- Yeni Maaşı 10000 TL Üzerinde Olan 2-5 Satır -----")
    print(selected_rows)
    print("-----------------------------------------------------")

    # g) Ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame oluşturma ve yazdırma
    new_df = df[['ad', 'soyad', 'sektor', 'yeni_maas']]
    print("----- Yeni DataFrame (Ad, Soyad, Sektör, Yeni Maaş) -----")
    print(new_df)
    print("--------------------------------------------------------")
except Exception as e:
    print("Hata oluştu:", str(e))