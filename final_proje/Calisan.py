class Calisan:
    def __init__(self, sektor, tecrube, maas):
        self.__sektor = self.kontrol_sektor(sektor)
        self.__tecrube = tecrube
        self.__maas = maas

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = self.kontrol_sektor(sektor)

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def kontrol_sektor(self, sektor):
        sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]
        if sektor.lower() in sektorler:
            return sektor.lower()
        else:
            return "diğer"

    def zam_hakki(self):
        if self.__tecrube < 24:
            return 0
        elif self.__tecrube >= 24 and self.__tecrube < 48 and self.__maas < 15000:
            return self.__maas * self.__tecrube / 100
        elif self.__tecrube >= 48 and self.__maas < 25000:
            return (self.__maas * self.__tecrube) / 200
        else:
            return 0

    def __str__(self):
        return f"Sektör: {self.__sektor}\nTecrübe: {self.__tecrube} ay\nYeni Maaş: {self.zam_hakki()}"

