from domain.entities import Student
from domain.entities import PbLaborator


class Console:
    def __init__(self, srv):
        """
        Initializeaza consola
        :type srv: ShowService
        """
        self.__srv = srv

    """
    def __print_all_shows(self):

        show_list = self.__srv.get_all_shows()
        if len(show_list) == 0:
            print('Nu exista seriale in lista.')
        else:
            print('Lista de seriale este:')
            for show in show_list:
                # print(show)
                print('Titlu serial: ', show.getTitle(), ' - An aparitie: ',
                      str(show.getAnAparitie(), ' - Nr. episoade: ', str(
                          show.getEpisoade())))

        """

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
            added_student = self.__srv.add_student(id, nume, grupa)
            print('Studentul ' + added_student.getNume() + ' (ID:' + str(
                added_student.getStudentID()) + ') a fost adaugat cu succes.')
        except ValueError as ve:
            print(str(ve))

    def __add_pbLab(self):
        nrLab_nrPb = str(input("Numarul laboratorului si problemei:"))

        descriere = str(input("Descrierea problemei:"))
        deadline = str(input("Termenul limita:"))

        try:
            added_pbLab = self.__srv.add_pbLab(nrLab_nrPb, descriere, deadline)
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
            print('Comenzi disponibile: add, delete, edit, raport, search, asign lab, grade lab, stats, exit')
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
                self.__print_all_shows()
            elif cmd == 'exit':
                # this should not be here per principles of app organization
                # added just to showcase how the static method works
                print("Total number of show objects created (including tests):", Student.getNumberOfShowObjects())
                return
            else:
                print('Comanda invalida.')


"""
def print_menu():
    print("----------Gestiune laboratoare studenți----------")
    print("1. Adauga")
    print("2. Sterge")
    print("3. Modifica")
    print("4. Rapoarte")
    print("5. Cautare")
    print("6. Asignare laborator")
    print("7. Notare laborator")
    print("S: Statistici")
    print("Exit: Iesi din aplicatie")


def start():
    finished = False
    while not finished:
        print_menu()
        option = input("Optiunea dumneavoastra este: ")
        if option == '1':
            add_show_ui(show_manager)
        elif option == '2':
            delete_shows_ui(show_manager)
        elif option == '3':
            filter_shows_ui(get_show_list(show_manager))
        elif option == '4':
            undo_ui(show_manager)
        elif option == '5':
            undo_ui(show_manager)
        elif option == '6':
            undo_ui(show_manager)
        elif option == '7':
            undo_ui(show_manager)
        elif option.lower() == 's':
            print_show_list(get_show_list(show_manager))
        elif option.lower() == 'exit':
            finished = True
        else:
            print("Optiunea introdusa este invalida.")

"""
