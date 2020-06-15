class Catalog_Prajituri():

    __prajituri = []

    def __init__(self, nume, pret, gramaj):
        if isinstance(nume, str) and isinstance(pret, int) and isinstance(gramaj, int):
            self.__nume = nume
            self.__pret = pret
            self.__gramaj = gramaj

    @classmethod
    def afisare_in_functie_de_pret(cls):
        prajituri_sortate_dupa_pret = sorted(cls.__prajituri, key=lambda x: x.__pret)
        text = ""

        for prajitura in prajituri_sortate_dupa_pret:
            text += f"Pret: {prajitura.__pret}, nume: {prajitura.__nume}, gramaj: {prajitura.__gramaj}\n"

        return text

    @classmethod
    def afisare_in_functie_de_gramaj(cls):
        prajituri_sortate_dupa_pret = sorted(cls.__prajituri, key=lambda x: x.__gramaj)
        text = ""

        for prajitura in prajituri_sortate_dupa_pret:
            text += f"Gramaj: {prajitura.__gramaj}, nume: {prajitura.__nume}, pret: {prajitura.__pret}\n"

        return text

    def __str__(self):
        return f"Nume prajitura: {self.__nume}, pret: {self.__pret}, gramaj:{self.__gramaj}\n"

class Tort(Catalog_Prajituri):
    def __init__(self, nume, pret, gramaj, etajat=False, glazura="ciocolata"):
        super().__init__(nume, pret, gramaj)
        self.__etajat = etajat
        self.__glazura = glazura

    def modificare_atribute(self, etajat, glazura):
        self.__etajat = etajat
        self.__glazura = glazura

    def __str__(self):
        text = super().__str__().replace("prajitura", "tort")
        text += f"Tortul {'nu ' if self.__etajat == False else ''}este etajat.\n"
        text += f"Tortul are glazura de {self.__glazura}"
        return text

class Fursec(Catalog_Prajituri):
    def __init__(self, nume, pret, gramaj):
        super().__init__(nume, pret, gramaj)

    def __str__(self):
        return super().__str__().replace("prajitura", "fursec")


tort1 = Tort("Tort Chocolate",  60 , 500)
tort2 = Tort("Tort Cremsmit ", 35 , 250, True, "vanilie")
tort3 = Tort("Tortul Raspberry 3", 80, 750)

fursec1 = Fursec("Fursec Cookie", 5, 25)
fursec2 = Fursec("Fursec Chocolate Bar", 10, 50)
fursec3 = Fursec("Fursec Biscuit", 15, 75)

print(Catalog_Prajituri.afisare_in_functie_de_gramaj())
print(Catalog_Prajituri.afisare_in_functie_de_pret())

tort1.modificare_atribute(True, "cacao")
print(tort1)
