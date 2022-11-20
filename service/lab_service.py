from domain.entities import Student
from domain.entities import PbLaborator
from domain.validators import Validator
from repository.lab_repo import InMemoryRepository


class StudentService:
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
        Adauga student
        :param studentID: Id-ul studentului
        :type studentID:int
        :param nume: numele studentului
        :type nume:str
        :param grupa:numarul grupei de care apartine
        :type grupa:int
        :return: obiectul de tip Student creat
        :rtype:-; studentul s-a adaugat in lista
        :raises: ValueError daca studentul are date invalide
        """
        s = Student(studentID, nume, grupa)

        self.__validator.validate_student(s)
        self.__repo.store_student(s)
        return s

    def get_all_students(self):
        """
        Returneaza o lista cu toati studenti disponibili
        :return: lista de studenti disponibili
        :rtype: list of objects de tip Student
        """
        return self.__repo.get_all_students()

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


    def add_pbLab(self, nrLab_nrPb, descriere, deadline):
        """
        Adauga pbLab
        :param nrLab_nrPb: nr lab si nr pb
        :type nrLab_nrPb:str
        :param descriere: descrierea problemei
        :type descriere:str
        :param deadline:termenul de predare a problemei
        :type deadline:str
        :return: obiectul de tip PbLaborator creat
        :rtype:-; problema s-a adaugat in lista
        :raises: ValueError daca problema are date invalide
        """
        p = PbLaborator(nrLab_nrPb, descriere, deadline)

        self.__validator.validate_pbLab(p)
        self.__repo.store_pbLab(p)
        return p

    def get_all_problems(self):
        """
        Returneaza o lista cu toate problemele disponibile
        :return: lista de probleme disponibile
        :rtype: list of objects de tip PbLaborator
        """
        return self.__repo.get_all_problems()
    """  de intrebat ce nu merge"""

    def delete_shows(self, an_inceput, an_sfarsit):
        pass


def test_add_student():
    repo = InMemoryRepository()
    validator = Validator()
    test_srv = StudentService(repo, validator)

    added_student = test_srv.add_student(545677, 'Tractoreanu Leonardo', 12)
    assert (added_student.getStudentID() == 545677)
    assert (added_student.getNume() == 'Tractoreanu Leonardo')
    assert (added_student.getGrup() == 12)

    assert (len(test_srv.get_all_students()) == 1)

    try:
        added_student = test_srv.add_student(545, 'Tractoreanu Leonardo', 12)
        assert False
    except ValueError:
        assert True

def test_add_probleme():
    repo = InMemoryRepository()
    validator = Validator()
    test_srv = LabService(repo, validator)

    added_problem = test_srv.add_pbLab('1_5', 'Sirul lui Fibbonaci', '10 octombrie')
    assert (added_problem. getNrLab_nrPb() == '1_5')
    assert (added_problem.getDescriere() == 'Sirul lui Fibbonaci')
    assert (added_problem.getDeadline() == '10 octombrie')

    assert (len(test_srv.get_all_problems()) == 1)

    try:
        added_problem = test_srv.add_pbLab('1231233_51231', 'Sirul lui Fibbonaci', '10 octombrie')
        assert False
    except ValueError:
        assert True
