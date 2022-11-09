
def print_menu():
    print("----------Gestiune laboratoare studenți----------")
    print("1. Adauga")
    print("2. Sterge")
    print("3. Modifica")
    print("4. Rapoarte")
    print("5. Cautare")
    print("6. Asignare laborator")
    print("7. Notare laborator")
    print("8. Statistici")
    print("9. Iesi din aplicatie")

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
        elif option == '8':
            undo_ui(show_manager)
        elif option.lower() == 'p':
            print_show_list(get_show_list(show_manager))

        elif option == '9':
            finished = True
        else:
            print("Optiunea introdusa este invalida.")

# TODO: tema pana marti