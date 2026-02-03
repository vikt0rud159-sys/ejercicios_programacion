import actions
import data

def display_menu():
    while True:
        valid_num = ["1","2","3","4","5","6","7","8","9"]
        menu = input("[1.Ingresar estudiante] [2.Mostrar datos] [3.Mejores promedios] [4.Promedio general] [5.Exportar CSV] [6.Importar CSV] [7.Eliminar estudiante] [8.Reprobados] [9.Finalizar]    ")
        if menu in valid_num:
            return menu
        else:
            print("   ¡Ingrese valor válido! [1] [2] [3] [4] [5] [6] [7] [8] [9]\n")


def menu_selection(menu,students_data, imported, main_student):
    try:
        if menu == "1":
            student_info = actions.add_student(students_data, imported, main_student)
            return student_info
        elif menu == "2":
            if len(students_data) >= 1:
                for student in students_data:
                    print(f"Nombre: {student.name}")
                    print(f"Section: {student.section}")
                    print(f"Español: {student.spanish[0]}")
                    print(f"Ingles: {student.english[0]}")
                    print(f"Estudios Sociales: {student.social_studies[0]}")
                    print(f"Ciencias: {student.science[0]}")
                    print(f"Promedio: {student.average}")
                    print()
            else:
                print("   ¡No hay datos!\n")
        elif menu == "3":
            actions.get_higher_average(students_data)
        elif menu == "4":
            actions.get_general_average(students_data)
        elif menu == "5":
            headers = ("name", "section", "spanish", "english", "social_studies", "science", "average")
            data.export_csv('students.csv', students_data, headers)
        elif menu == "6":
            return "6"
        elif menu == "7":
            actions.del_student(students_data)
        elif menu == "8":
            actions.students_who_failed(students_data)
        elif menu == "9":
            print("   Programa finalizado.\n")
            exit()
    except IndexError:
        print("   ¡Sin datos para exportar!\n")
    except Exception as ex:
        print(f"Error: {ex}\n")