from domain.entities import Student
from domain.entities import PbLaborator


class Console:
    def __init__(self, srvL, srvS):
        """
        Initializeaza consola
        :type srvL: LabService
        :type srvS: StudentService
        """
        self.__srvL = srvL
        self.__srvS = srvS


    def __print_all(self):

        student_list = self.__srvS.get_all_students()
        if len(student_list) == 0:
            print('Nu exista studenti in lista.')
        else:
            print('Lista de studenti este:')
            for student in student_list:
                # print(student)
                print('Studentul ' + str(student.getNume()) + ' (ID:' + str(
                student.getStudentID()) + ') din grupa: ' + str(student.getGrup()))

        probleme_list = self.__srvL.get_all_problems()
        if len(probleme_list) == 0:
            print('Nu exista probleme in lista.')
        else:
            print('Lista de probleme este:')
            for problema in probleme_list:
                # print(student)
                print('Problema nr ' + str(problema.getNrLab_nrPb()) + ': ' + str(
                    problema.getDescriere()) + ', termen limita ' + str(problema.getDeadline()))


    def __add_student(self):
        """
        Adauga un serial cu datele citite de la tastatura
        """
        nume = str(input("Numele Studentului:"))

        try:
            id = int(input("ID-ul studentului:"))
            grupa = int(input("Numarul grupei:"))
        except ValueError:
            print('Numarul grupei si id-ul trebuie sa fie un numar.')
            return

        try:
            added_student = self.__srvS.add_student(id, nume, grupa)
            print('Studentul ' + added_student.getNume() + ' (ID:' + str(
                added_student.getStudentID()) + ') a fost adaugat cu succes.')
        except ValueError as ve:
            print(str(ve))

    def __add_pbLab(self):
        nrLab_nrPb = str(input("Numarul laboratorului si problemei:"))

        descriere = str(input("Descrierea problemei:"))
        deadline = str(input("Termenul limita:"))

        try:
            added_pbLab = self.__srvL.add_pbLab(nrLab_nrPb, descriere, deadline)
            print('Problema ' + str(added_pbLab.getNrLab_nrPb()) + ' : ' + str(
                added_pbLab.getDescriere()) + '; Termen limita: ' + str(
                added_pbLab.getDeadline()), '; a fost adaugata cu succes')
        except ValueError as ve:
            print(str(ve))

    def __delete_student(self):
        id = int(input("ID-ul studentului:"))
        try:
            deleted_student = self.__srvS.delete_student(id)
            print('Studentul ' + deleted_student.getNume() + ' din grupa ' + str(
                deleted_student.getGrup()) + ' a fost sters cu succes (IDStudent=' + str(deleted_student.getStudentID()) + ').')
        except ValueError as ve:
            print(str(ve))

    def __delete_pbLab(self):
        nr = str(input("Nr lab si pb:"))
        try:
            deleted_pbLab = self.__srvL.delete_pbLab(nr)
            print('Problema nr ' + deleted_pbLab.getNrLab_nrPb() + ' cu termen ' + str(
                deleted_pbLab.getDeadline()) + ' a fost sters cu succes')
        except ValueError as ve:
            print(str(ve))

    def __edit_student(self):
        id = int(input('ID-ul studentului:'))
        nume = input("Numele studentului:")

        try:
            grupa = int(input("Grupa din care face parte studentul:"))
        except ValueError:
            print('Grupa trebuie sa fie un numar.')
            return

        try:
            modified_student = self.__srvS.edit_student(id, nume, grupa)
            print('Studentul ' + modified_student.getNume() + ' (' + str(
                modified_student.getStudentID()) + ') a fost modificat cu succes.')
        except ValueError as ve:
            print(str(ve))

    def __edit_pbLab(self):
        nr = str(input('Nr lab si pb:'))
        descriere = str(input("Descrierea problemei:"))
        deadline = str(input("Termenul limita:"))

        try:
            modified_problem = self.__srvL.edit_pbLab(nr, descriere, deadline)
            print('Problema ' + modified_problem.getNrLab_nrPb() + ' cu termen limita ' + str(
                modified_problem.getDeadline()) + ' a fost modificat cu succes.')
        except ValueError as ve:
            print(str(ve))


    def gestiune_lab_ui(self):
        # command-driven menu (just to have something different)
        # Lab7-9 oricare varianta (print-menu + optiuni/comenzi) este ok
        # dar si la comenzi sa existe un user guide, ce comenzi sunt dispobibile, cum le folosim
        # if using Python 3.10 and bored with if statements,
        # you can try: https://learnpython.com/blog/python-match-case-statement/
        while True:
            print('Comenzi disponibile: add, delete, edit, raport, search, asign lab, grade lab, stats, show all, exit')
            cmd = input('Comanda este:')
            cmd = cmd.lower().strip()
            if cmd == 'add':
                print('Selecteaza: student, pb_lab')
                cmd = input('Comanda este:')
                if cmd == 'student':
                    self.__add_student()
                elif cmd == 'pb_lab':
                    self.__add_pbLab()
                else:
                    print('Comanda invalida.')
            elif cmd == 'delete':
                print('Selecteaza: student, pb_lab')
                cmd = input('Comanda este:')
                if cmd == 'student':
                    self.__delete_student()
                elif cmd == 'pb_lab':
                    self.__delete_pbLab()
                else:
                    print('Comanda invalida.')
            elif cmd =='edit':
                print('Selecteaza: student, pb_lab')
                cmd = input('Comanda este:')
                if cmd == 'student':
                    self.__edit_student()
                elif cmd == 'pb_lab':
                    self.__edit_pbLab()
                else:
                    print('Comanda invalida.')
            elif cmd == 'show all':
                self.__print_all()
            elif cmd == 'exit':
                # this should not be here per principles of app organization
                # added just to showcase how the static method works
                print("Total number of student objects created (including tests):", Student.getNumberOfStudentObjects())
                print("Total number of PbLaborator objects created (including tests):", PbLaborator.getNumberOfProblemObjects())
                return
            else:
                print('Comanda invalida.')
