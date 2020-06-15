class Catalog:
    def __init__(self, nume, prenume):
        self.__nume = nume
        self.__prenume = prenume
        self.__materii = dict()
        self.__absente = 0

    def adauga_absente(self):
        self.__absente += 1

    def sterge_absente(self, numar_absente):
        if isinstance(numar_absente, int):
            if numar_absente <= self.__absente:
                self.__absente -= numar_absente

    def __str__(self):
        return f"Studentul {self.__nume} {self.__prenume} are {self.__absente} absente."


class Materii(Catalog):
    def __init__(self, nume, prenume):
        super().__init__(nume, prenume)

    def adauga_materie(self, materie, note):
        if isinstance(materie, str) and isinstance(note, list):
            self._Catalog__materii[materie] = note

    def afisare_materii(self):
        text = f"\nMateriile studentului {self._Catalog__nume} {self._Catalog__prenume} sunt:\n"
        for materie in self._Catalog__materii.keys():
            text += f"{materie} "
        return text

    def afisare_medii(self):

        text = f"\nMateriile studentului {self._Catalog__nume} {self._Catalog__prenume} si mediile lor:\n"
        for materie, note in self._Catalog__materii.items():
            Note = [x for x in note if isinstance(x, int)]
            medie = sum(Note) / len(Note)
            text = text + f"La materia {materie} studentul are media: {medie}\n"
        return

student_1 = Materii("Ion", "Roata")
student_1.adauga_absente()
student_1.adauga_absente()
student_1.adauga_absente()
student_1.sterge_absente(2)

student_2 = Materii("George", "Cerc")
student_2.adauga_absente()
student_2.adauga_absente()
student_2.adauga_absente()
student_2.adauga_absente()
student_2.sterge_absente(2)

print(student_1)
print(student_2)

student_1.adauga_materie("Python", [4, 5, 5])
student_2.adauga_materie("Python", [7, 8, 9])

student_2.adauga_materie("Matematica", [4, 7, 9])
student_1.adauga_materie("Romana", [5, 9, 6])

print(student_1.afisare_materii())
print(student_2.afisare_materii())

print(student_1.afisare_medii())
print(student_2.afisare_medii())

