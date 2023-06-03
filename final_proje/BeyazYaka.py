class BeyazYaka:
    def __init__(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self, tecrube, maas):
        try:
            tecrube = int(tecrube)
            maas = float(maas)

            if tecrube < 24:
                return 0
            elif tecrube >= 24 and tecrube < 48 and maas < 15000:
                return (maas * tecrube / 100) * 5 + self.__tesvik_primi
            elif tecrube >= 48 and maas < 25000:
                return (maas * tecrube / 100) * 4 + self.__tesvik_primi
            else:
                return 0
        except ValueError:
            return 0

    def __str__(self):
        return f"Teşvik Prim: {self.__tesvik_primi}"

