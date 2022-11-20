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

    def find_student(self, id):
        """
        Cauta studentul cu id dat
        :param id: id dat
        :type id: int
        :return: studentul cu id dat, None daca nu exista
        :rtype: Student
        """
        for student in self.__studenti:
            if student.getStudentID() == id:
                return student
        return None

    def find_problema(self, nr):
        """
        Cauta problema cu nr dat
        :param nr: nr dat
        :type nr: str
        :return: problema cu nr dat, None daca nu exista
        :rtype: PbLaborator
        """
        for problema in self.__probleme:
            if problema.getNrLab_nrPb() == nr:
                return problema
        return None

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
        :rtype:Nu exista serial cu acest id.
        """
        self.__probleme.append(problema)

    def get_all_students(self):
        """
        Returneaza o lista cu toati studenti existenti
        :rtype: list of objects de tip Student
        """
        return self.__studenti

    def get_all_problems(self):
        """
        Returneaza o lista cu toate problemele de laborator existente
        :rtype: list of objects de tip PbLaborator
        """
        return self.__probleme

    def delete_student(self, id):
        """
        Sterge student dupa id
        :param id: id-ul dat
        :type id: int
        :return: studentul sters
        :rtype: Student
        :raises: ValueError daca id-ul nu exista
        """

        student = self.find_student(id)
        if student is None:
            raise ValueError('Nu exista student cu acest id.')

        self.__studenti.remove(student)
        return student


    def delete_pbLab(self, nr):
        """
        Sterge problema dupa nr
        :param nr: nr dat
        :type nr: str
        :return: studentul sters
        :rtype:  PbLaborator
        :raises: ValueError daca nr nu exista
        """

        problema = self.find_problema(nr)
        if problema is None:
            raise ValueError('Nu exista problema cu acest nr.')

        self.__probleme.remove(problema)
        return problema
    def edit_student(self,id, modified_student):
        """
                Modifica datele studentului cu id dat
                :param id: id dat
                :type id: int
                :param modified_student: studentul-ul cu datele noi
                :type modified_student: Student
                :return: studentul-ul modificat
                :rtype: Student
                """
        student = self.find_student(id)
        if student is None:
            raise ValueError('Nu exista student cu acest id.')

        self.delete_student(id)
        self.store_student(modified_student)

        return modified_student

    def edit_pbLab(self,nr, modified_problem):
        """
                Modifica datele studentului cu id dat
                :param nr: nr dat
                :type nr: str
                :param modified_problem: studentul-ul cu datele noi
                :type modified_problem: PbLaborator
                :return: problema modificata
                :rtype: PbLaborator
                """
        problem = self.find_problema(nr)
        if problem is None:
            raise ValueError('Nu exista problema cu acest nr.')

        self.delete_pbLab(nr)
        self.store_pbLab(modified_problem)

        return modified_problem




def test_store_studenti():
    pass


def test_store_pbLab():
    pass
