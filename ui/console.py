from domain.entities import Student
from domain.entities import PbLaborator
from domain.entities import Grade
from termcolor import colored
from exceptions.exceptions import *


class Console:
    def __init__(self, srvL, srvS, srvR, srvG):
        """
        Initializeaza consola
        :type srvL: LabService
        :type srvS: StudentService
        """
        self.__srvL = srvL
        self.__srvS = srvS
        self.__srvR = srvR
        self.__srvG = srvG

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

    def __print_grades(self, grades_list):
        """
        Afiseaza o lista de rating-uri

        """

        if len(grades_list) == 0:
            print('Nu exista note in lista.')
        else:
            print('Lista de grade-uri este:')
            for grade in grades_list:
                print('Student: [', colored(str(grade.getStudent().getNume()), 'cyan'), '; ID:',
                      colored(str(grade.getStudent().getStudentID()), 'cyan'), ']',
                      'PbLab: [', colored(str(grade.getPbLab().getNrLab_nrPb()), 'magenta'), '; ',
                      colored(str(grade.getPbLab().getDescriere()), 'magenta'), ']', 'Rating: ', colored(str(
                        grade.getGrade()), 'blue'))

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
            print(colored(str(ve), 'red'))

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
            print(colored(str(ve), 'red'))

    def __delete_student(self):
        id = int(input("ID-ul studentului:"))
        try:
            deleted_student = self.__srvS.delete_student(id)
            print('Studentul ' + deleted_student.getNume() + ' din grupa ' + str(
                deleted_student.getGrup()) + ' a fost sters cu succes (IDStudent=' + str(
                deleted_student.getStudentID()) + ').')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __delete_pbLab(self):
        nr = str(input("Nr lab si pb:"))
        try:
            deleted_pbLab = self.__srvL.delete_pbLab(nr)
            print('Problema nr ' + deleted_pbLab.getNrLab_nrPb() + ' cu termen ' + str(
                deleted_pbLab.getDeadline()) + ' a fost sters cu succes')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

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
            print('Studentul ' + modified_student.getNume() + ' (ID: ' + str(
                modified_student.getStudentID()) + ') a fost modificat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __edit_pbLab(self):
        nr = str(input('Nr lab si pb:'))
        descriere = str(input("Descrierea problemei:"))
        deadline = str(input("Termenul limita:"))

        try:
            modified_problem = self.__srvL.edit_pbLab(nr, descriere, deadline)
            print('Problema ' + modified_problem.getNrLab_nrPb() + ' cu termen limita ' + str(
                modified_problem.getDeadline()) + ' a fost modificat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __search_student(self):
        id = int(input('ID-ul studentului:'))

        try:
            searched_student = self.__srvS.search_student(id)
            print('Studentul ' + searched_student.getNume() + ' (ID: ' + str(
                searched_student.getStudentID()) + ') din grupa ' + str(
                searched_student.getGrup()))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __search_pbLab(self):
        nr = input('Nr-ul problemei:')

        try:
            searched_problem = self.__srvL.search_pbLab(nr)
            print('Problema nr' + searched_problem.getNrLab_nrPb() + ' cu termen limita  ' + str(
                searched_problem.getDeadline()) + ': ' + str(searched_problem.getDescriere()))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __random_student(self):
        """
        Genereaza un student random
        """
        nr = int(input("Numar studenti random:"))

        try:
            for i in range(nr):
                random_student = self.__srvR.random_student()
                print('Studentul ' + random_student.getNume() + ' (ID:' + str(
                    random_student.getStudentID()) + ') a fost adaugat cu succes.')
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __random_pbLab(self):
        """
        Genereaza un problema random
        """
        nr = int(input("Numar probleme random:"))

        try:
            for i in range(nr):
                random_problem = self.__srvR.random_pbLab()
                print('Problema nr ' + random_problem.getNrLab_nrPb() + ' cu termen limita ' + str(
                    random_problem.getDeadline()) + ' : ' + str(
                    random_problem.getDescriere()))
        except ValueError as ve:
            print(colored(str(ve), 'red'))

    def __assign_grade(self):
        id_student = int(input('ID student:'))
        nr_pbLab = input('Numar PbLab')
        try:
            grade_val = float(input('Nota problema laborator:'))
            grade = self.__srvG.create_grade(id_student, nr_pbLab, grade_val)
            print('Rating-ul', grade, 'a fost adaugat cu succes.')
        except ValueError:
            print(colored('Nota trebuie sa fie un numar.', 'red'))
        except ValidationException as ve:
            print(colored(str(ve), 'red'))
        except StudentNotFoundException as ve:
            print(colored(str(ve), 'red'))
        except PbLabNotFoundException as ve:
            print(colored(str(ve), 'red'))
        except GradeAlreadyAssignedException as ve:
            print(colored(str(ve), 'red'))

    def gestiune_lab_ui(self):
        # command-driven menu (just to have something different)
        # Lab7-9 oricare varianta (print-menu + optiuni/comenzi) este ok
        # dar si la comenzi sa existe un user guide, ce comenzi sunt dispobibile, cum le folosim
        # if using Python 3.10 and bored with if statements,
        # you can try: https://learnpython.com/blog/python-match-case-statement/
        while True:
            print('Comenzi disponibile: add, delete, edit, search, asign lab, grade lab, stats, random, show all, exit')
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
            elif cmd == 'edit':
                print('Selecteaza: student, pb_lab')
                cmd = input('Comanda este:')
                if cmd == 'student':
                    self.__edit_student()
                elif cmd == 'pb_lab':
                    self.__edit_pbLab()
                else:
                    print('Comanda invalida.')
            elif cmd == 'search':
                print('Selecteaza: student, pb_lab')
                cmd = input('Comanda este:')
                if cmd == 'student':
                    self.__search_student()
                elif cmd == 'pb_lab':
                    self.__search_pbLab()
                else:
                    print('Comanda invalida.')
            elif cmd == 'random':
                print('Selecteaza: student, pb_lab')
                cmd = input('Comanda este:')
                if cmd == 'student':
                    self.__random_student()
                elif cmd == 'pb_lab':
                    self.__random_pbLab()
                else:
                    print('Comanda invalida.')
            elif cmd == 'assign grade':
                self.__assign_grade()
            elif cmd == 'grade lab':
                self.__grade_pbLab()
            elif cmd == 'show grades':
                self.__print_grades(self.__srvG.get_all_grades())
            elif cmd == 'show all':
                self.__print_all()
            elif cmd == 'exit':
                # this should not be here per principles of app organization
                # added just to showcase how the static method works
                print("Total number of student objects created (including tests):", Student.getNumberOfStudentObjects())
                print("Total number of PbLaborator objects created (including tests):",
                      PbLaborator.getNumberOfProblemObjects())
                return
            else:
                print('Comanda invalida.')
