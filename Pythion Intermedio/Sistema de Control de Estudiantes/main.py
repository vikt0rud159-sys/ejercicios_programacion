import data
import menu
import actions


def program():
    students_data = []
    imported = []
    main_student = 0
    try:
        while True:
            request = (menu.menu_selection(menu.display_menu(),students_data, imported, main_student))
            students_data.append(request)
            students_data = [value for value in students_data if value is not None]
            if request == "6":
                students_data = []
                imported = data.import_csv()
                for main_student in range(len(imported)):
                    students_data.append(actions.add_student(students_data, imported, main_student))
                    students_data = [value for value in students_data if value is not None]
                imported = []
                print("   Archivo importado con exito\n")
    except Exception as ex:
        print(f"Error: {ex}\n")
        program()


program()