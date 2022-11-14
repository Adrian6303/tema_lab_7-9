class Student:
    no_instances = 0

    def __init__(self, studentID, nume, grup):
        """
        Creeaza un nou serial cu titlul, anul aparitiei si numarul de episoade dat
        :param titlu: titlul serialului
        :type titlu: str
        :param an_aparitie: anul aparitiei serialului
        :type an_aparitie: int (1970-2021)
        :param eps: numarul de episoade din serial
        :type eps: int (>0)
        """
        self.__studentID = studentID
        self.__nume = nume
        self.__grup = grup
        Student.no_instances += 1

    def getStudentID(self):
        return self.__studentID

    def getNume(self):
        return self.__nume

    def getGrup(self):
        return self.__grup

    def setStudentID(self, value):
        self.__studentID = value

    def setNume(self, value):
        self.__nume = value

    def setGrup(self, value):
        self.__grup = value

    def __eq__(self, other):
        """
        Verifica egalitatea intre serialul curent si serialul other
        :param other:
        :type other: Serial
        :return: True daca serialele sunt egale (=au acelasi titlu si acelasi an de aparitie), False altfel
        :rtype: bool
        """
        if self.__studentID == other.getStudentID():
            return True
        return False

    # https://www.tutorialsteacher.com/python/magic-methods-in-python
    # puteti sa cititi aici pe link-ul de mai sus ce metode
    # se mai pot suprascrie pentru o clasa in afara de __eq__ si __str__

    def __str__(self):
        return "ID Student: " + self.__StudentID + '; Nume: ' + str(self.__nume) + '; Grupa: ' + str(
            self.__grupa)

    @staticmethod
    def getNumberOfShowObjects():
        return Student.no_instances


def test_create_student():
    student1 = Student(578102, 'Marinache Iberiu', 4)
    assert (student1.getStudentID() == 578102)
    assert (student1.getNume() == 'Marinache Iberiu')
    assert (student1.getGrup() == 4)

    student1.setStudentID(567123)
    student1.setNume('Pasare Valeriu')
    student1.setGrup(7)

    assert (student1.getStudentID() == 567123)
    assert (student1.getNume() == 'Pasare Valeriu')
    assert (student1.getGrup() == 7)


def test_equals_student():
    student1 = Student(895176,'Randunica Adriana', 12)
    student2 = Student(895176, 'Randunica Adriana', 10)

    assert (student1 == student2)

    student3 = Student(128626,'Randunica Adriana', 12)
    assert (student1 != student3)


test_create_student()
test_equals_student()

class PbLaborator:
    no_instances = 0

    def __init__(self, nrLab_nrPb, descriere, deadline):

        self.__nrLab_nrPb = nrLab_nrPb
        self.__descriere = descriere
        self.__deadline = deadline
        PbLaborator.no_instances += 1

    def getNrLab_nrPb(self):
        return self.__nrLab_nrPb

    def getDescriere(self):
        return self.__descriere

    def getDeadline(self):
        return self.__deadline

    def setNrLab_nrPb(self, value):
        self.__nrLab_nrPb = value

    def setDescriere(self, value):
        self.__descriere = value

    def setDeadline(self, value):
        self.__deadline = value

    def __eq__(self, other):
        """
        Verifica egalitatea intre serialul curent si serialul other
        :param other:
        :type other: Serial
        :return: True daca serialele sunt egale (=au acelasi titlu si acelasi an de aparitie), False altfel
        :rtype: bool
        """
        if self.__nrLab_nrPb == other.getNrLab_nrPb():
            return True
        return False

    # https://www.tutorialsteacher.com/python/magic-methods-in-python
    # puteti sa cititi aici pe link-ul de mai sus ce metode
    # se mai pot suprascrie pentru o clasa in afara de __eq__ si __str__

    def __str__(self):
        return "Nr lab si nr problema: " + str(self.__nrLab_nrPb) + '; Descriere: ' + str(self.__descriere) + '; Deadline: ' + str(
            self.__deadline)

    @staticmethod
    def getNumberOfShowObjects():
        return Student.no_instances


def test_create_PbLaborator():
    PbLaborator1 = PbLaborator('2_7', 'Cautare numere prime', '4 martie')
    assert (PbLaborator1.getNrLab_nrPb() == '2_7')
    assert (PbLaborator1.getDescriere() == 'Cautare numere prime')
    assert (PbLaborator1.getDeadline() == '4 martie')

    PbLaborator1.setNrLab_nrPb('5_12')
    PbLaborator1.setDescriere('Divizorii comuni')
    PbLaborator1.setDeadline('7 iunie')

    assert (PbLaborator1.getNrLab_nrPb() == '5_12')
    assert (PbLaborator1.getDescriere() == 'Divizorii comuni')
    assert (PbLaborator1.getDeadline() == '7 iunie')


def test_equals_PbLaborator():
    PbLaborator1 = PbLaborator('2_7', 'Cautare numere prime', '5 martie')
    PbLaborator2 = PbLaborator('2_7', 'Cautare numere prime', '1 martie')

    assert (PbLaborator1 == PbLaborator2)

    PbLaborator3 = PbLaborator('2_10', 'Cautare numere prime', '10 martie')
    assert (PbLaborator1 != PbLaborator3)


test_create_student()
test_equals_student()

test_create_PbLaborator()
test_equals_PbLaborator()
