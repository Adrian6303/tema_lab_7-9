class InMemoryRepository:
    """
        Clasa creata cu responsabilitatea de a gestiona
        multimea de studenti si probleme (i.e. sa ofere un depozit persistent pentru obiecte
        de tip student si pb)

    """

    def __init__(self):
        # shows - multimea de seriale pe care o gestionam
        # poate fi si dictionar, este la latitudinea noastra cum stocam datele
        # e.g. stocare in dict cu un camp in plus id_serial (dar se poate lua titlu ca si cheie
        # de ex, daca am sti ca e unic):
        # {idSerial1: Serial1, idSerial2: Serial2}
        # vs. [serial1, serial2]
        self.__studenti = []
        self.__probleme = []

    def store_student(self, student):
        """
        Adauga un student in lista
        :param student: serialul care se adauga
        :type student: Student
        :return: -; lista de studenti se modifica prin adaugarea studentului dat
        :rtype:
        """
        self.__studenti.append(student)

    def store_pbLab(self, problema):
        """
        Adauga un serial in lista
        :param problema: problema care se adauga
        :type problema: PbLaborator
        :return: -; lista de probleme se modifica prin adaugarea problemei date
        :rtype:
        """
        self.__probleme.append(problema)

    def get_all_students(self):
        """
        Returneaza o lista cu toati studenti existenti
        :rtype: list of objects de tip Student
        """
        return self.__studenti

    def get_all_pbLab(self):
        """
        Returneaza o lista cu toate problemele de laborator existente
        :rtype: list of objects de tip PbLaborator
        """
        return self.__probleme


def test_store_studenti():
    pass


def test_store_pbLab():
    pass
