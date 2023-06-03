class Issiz:
    def __init__(self, tecrubeler):
        self.__tecrubeler = tecrubeler
        self.__statu = self.statu_bul()

    def get_tecrubeler(self):
        return self.__tecrubeler

    def set_tecrubeler(self, tecrubeler):
        self.__tecrubeler = tecrubeler
        self.__statu = self.statu_bul()

    def get_statu(self):
        return self.__statu

    def statu_bul(self):
        etkiler = {"mavi yaka": 0.20, "beyaz yaka": 0.35, "yönetici": 0.45}
        max_etki = 0
        max_statu = None

        for statu, etki in etkiler.items():
            if statu in self.__tecrubeler and self.__tecrubeler[statu] * etki > max_etki:
                max_etki = self.__tecrubeler[statu] * etki
                max_statu = statu

        return max_statu
