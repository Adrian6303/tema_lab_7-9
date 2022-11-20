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
        pass

    def gestiune_lab_ui(self):
        # command-driven menu (just to have something different)
        # Lab7-9 oricare varianta (print-menu + optiuni/comenzi) este ok
        # dar si la comenzi sa existe un user guide, ce comenzi sunt dispobibile, cum le folosim
        # if using Python 3.10 and bored with if statements,
        # you can try: https://learnpython.com/blog/python-match-case-statement/
        while True:
            print('Comenzi disponibile: add, delete, edit, raport, search, asign lab, grade lab, stats, show_all, exit')
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
            elif cmd == 'show_all':
                self.__print_all()
            elif cmd == 'exit':
                # this should not be here per principles of app organization
                # added just to showcase how the static method works
                print("Total number of show objects created (including tests):", Student.getNumberOfShowObjects())
                return
            else:
                print('Comanda invalida.')
