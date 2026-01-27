import data
import menu


def program():
    students_data = []
    try:
        while True:
            request = (menu.menu_selection(menu.display_menu(),students_data))
            students_data.append(request)
            students_data = [value for value in students_data if value is not None]
            if request == "6":
                students_data = data.import_csv()
                print("   Archivo importado con exito\n")
    except Exception as ex:
        print(f"Error: {ex}\n")
        program()


program()