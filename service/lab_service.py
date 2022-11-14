from domain.entities import Student
from domain.entities import PbLaborator
from domain.validators import Validator
from repository.lab_repo import InMemoryRepository


class LabService:
    """
        GRASP Controller (Curs 6)
        Responsabil de efectuarea operatiilor cerute de utilizator
        Coordoneaza operatiile necesare pentru a realiza actiunea declansata de utilizator
        (i.e. declansare actiune: utilizator -> ui-> obiect tip service in ui -> service -> service coordoneaza operatiile
        folosind alte obiecte (e.g. repo, validator) pentru a realiza efectiv operatia)
        """
    def __init__(self, repo, validator):
        """
        Initializeaza service
        :param repo: obiect de tip repo care ne ajuta sa gestionam multimea de seriale
        :type repo: InMemoryRepository
        :param validator: validator pentru verificarea serialelor
        :type validator: ShowValidator
        """
        self.__repo = repo
        self.__validator = validator

    def add_student(self, studentID, nume, grupa):
        """
        Adauga serial
        :param titlu: titlul serialului
        :type titlu:str
        :param an_aparitie: anul de aparitie al serialului
        :type an_aparitie:int
        :param eps:numarul de episoade al serialului
        :type eps:int
        :return: obiectul de tip Serial creat
        :rtype:-; serialul s-a adaugat in lista
        :raises: ValueError daca serialul are date invalide
        """
        s = Student(studentID, nume, grupa)

        self.__validator.validate_student(s)
        self.__repo.store_student(s)
        return s


    def add_pbLab(self, nrLab_nrPb, descriere, deadline):
        """
        Adauga serial
        :param titlu: titlul serialului
        :type titlu:str
        :param an_aparitie: anul de aparitie al serialului
        :type an_aparitie:int
        :param eps:numarul de episoade al serialului
        :type eps:int
        :return: obiectul de tip Serial creat
        :rtype:-; serialul s-a adaugat in lista
        :raises: ValueError daca serialul are date invalide
        """
        p = PbLaborator(nrLab_nrPb, descriere, deadline)

        self.__validator.validate_pbLab(p)
        self.__repo.store_pbLab(p)
        return p

    def get_all_shows(self):
        """
        Returneaza o lista cu toate serialele disponibile
        :return: lista de seriale disponibile
        :rtype: list of objects de tip Serial
        """
        return self.__repo.get_all_shows()

    def delete_shows(self,an_inceput, an_sfarsit):
        pass


def test_add_student():
    repo = InMemoryRepository()
    validator = Validator()
    test_srv = LabService(repo, validator)

    added_student = test_srv.add_student(545677, 'Tractoreanu Leonardo', 12)
    assert (added_student.getStudentID() == 545677)
    assert (added_student.getNume() == 'Tractoreanu Leonardo')
    assert (added_student.getGrup() == 12)

    assert (len(test_srv.get_all_shows()) == 1)

    try:
        added_student = test_srv.add_student(545, 'Tractoreanu Leonardo', 12)
        assert False
    except ValueError:
        assert True