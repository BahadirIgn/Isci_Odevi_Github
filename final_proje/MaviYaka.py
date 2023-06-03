class MaviYaka:
    def __init__(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = yipranma_payi

    def zam_hakki(self, tecrube, maas):
        try:
            tecrube = int(tecrube)
            maas = float(maas)

            if tecrube < 24:
                return 0
            elif tecrube >= 24 and tecrube < 48 and maas < 15000:
                return (maas * tecrube / 100) / 2 + (self.__yipranma_payi * 10)
            elif tecrube >= 48 and maas < 25000:
                return (maas * tecrube / 100) / 3 + (self.__yipranma_payi * 10)
            else:
                return 0
        except ValueError:
            return 0

    def __str__(self):
        return f"Yıpranma Payı: {self.__yipranma_payi}"
