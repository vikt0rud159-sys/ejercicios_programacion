def get_name():
    invalid_characters = "1234567890"
    while True:
        try:
            name = input("Nombre completo del estudiante: ")
            if name == "" or name[0] == " ":
                raise ValueError
            for name_char in name:
                if name_char in invalid_characters:
                    raise ValueError
            return name
        except ValueError:
            print("¡Formato no válido!\n")


def get_section():
    while True:
        try:
            section = "00"
            section = input("Sección: ")
            if section[0].isdigit() and section[-1].isupper() and len(section) <= 3:
                if len(section) == 2:
                    return section
                elif len(section) == 3 and section[1].isdigit():
                    return section
                raise
            else:
                raise
        except:
            print("¡Formato no válido! [1A] [22B]\n")


def get_spanish_note():
    while True:
        try:
            spanish_note = float(input("Nota de español: "))
            if spanish_note >= 0 and spanish_note <= 100:
                return spanish_note
            else:
                raise ValueError
        except ValueError:
            print("¡Formato no válido! Ingresar valor entre 0 y 100\n")


def get_english_note():
    while True:
        try:
            english_note = float(input("Nota de inglés: "))
            if english_note >= 0 and english_note <= 100:
                return english_note
            else:
                raise ValueError
        except ValueError:
            print("¡Formato no válido! Ingresar valor entre 0 y 100\n")


def get_social_studies_note():
    while True:
        try:
            social_studies_note = float(input("Nota de sociales: "))
            if social_studies_note >= 0 and social_studies_note <= 100:
                return social_studies_note
            else:
                raise ValueError
        except ValueError:
            print("¡Formato no válido! Ingresar valor entre 0 y 100\n")


def get_science_note():
    while True:
        try:
            science_note = float(input("Nota de ciencias: "))
            if science_note >= 0 and science_note <= 100:
                print("\n")
                return science_note
            else:
                raise ValueError
        except ValueError:
            print("¡Formato no válido! Ingresar valor entre 0 y 100\n")


def get_student_info(students_data):
    try:
        name = get_name()
        section = get_section()
        for student in range(len(students_data)):
            if name == students_data[student]["Name"] and str(section) in str(students_data[student]["Section"]):
                print("¡Estudiante ya registrado!\n")
                return
        new_student = {
        "Name": name,
        "Section": section,
        "Spanish": get_spanish_note(),
        "English": get_english_note(),
        "Social Studies": get_social_studies_note(),
        "Science": get_science_note(),
        }
        new_student["Average"] = (new_student["Spanish"] + new_student["English"] + new_student["Social Studies"] + new_student["Science"]) / 4
        return new_student
    except Exception as ex:
        print(f"Error: {ex}\n")


def get_higher_average(students_data):
    student_higher = []
    higher = []
    try:
        for student in range(len(students_data)):
            if len(student_higher) == 0:
        # if len(students_data) > 0:
        # for student in students_data:
                student_higher = [students_data[0]["Name"]]
                higher = [students_data[0]["Average"]]
            elif float(students_data[student]["Average"]) >= float(higher[0]):
                student_higher.insert(0, students_data[student]["Name"])
                higher.insert(0, students_data[student]["Average"])
            elif len(student_higher) == 1:
                student_higher.append(students_data[student]["Name"])
                higher.append(students_data[student]["Average"])
            elif float(students_data[student]["Average"]) >= float(higher[1]):
                student_higher.insert(1, students_data[student]["Name"])
                higher.insert(1, students_data[student]["Average"])
            elif len(student_higher) == 2:
                student_higher.append(students_data[student]["Name"])
                higher.append(students_data[student]["Average"])
            elif len(student_higher) <= 3:
                if float(students_data[student]["Average"]) >= float(higher[2]):
                    student_higher.insert(2, students_data[student]["Name"])
                    higher.insert(2, students_data[student]["Average"])
        for top in range(len(student_higher)):
            if top == 3:
                return
            print(f"[Nombre: {student_higher[top]}]       [Promedio: {higher[top]}]")
        print()
    except Exception as ex:
        print(f"Error: {ex}\n")
        return print()


def get_general_average(students_data):
    general_average = 0
    try:
        for average in students_data:
            if general_average == 0:
                general_average = float(average["Average"])
                counter = 1
            else:
                general_average += float(average["Average"])
                counter += 1
        return print(f"Promedio general: {general_average / counter}\n")
    except Exception as ex:
        print(f"Error: {ex}\n")


def del_student(students_data):
    try:
        del_name = get_name()
        del_sec = get_section()
        for index in range(len(students_data)):
            if students_data[index]["Name"].lower() == del_name.lower() and students_data[index]["Section"].lower() == del_sec.lower():
                confirm = input(f"Confirmación requerida (Presione [S])    ")
                if confirm.lower() == "s":
                    students_data.remove(students_data[index])
                    print(f"[Nombre: {del_name}][Sección: {del_sec}] Eliminado con éxito.\n")
                else:
                    print("¡Eliminación de estudiante cancelada!\n")
                    return
        else:
            print("¡Estudiante no encontrado!\n")
    except IndexError:
        ""
    except Exception as ex:
        print(f"Error: {ex}\n")


def students_who_failed(students_data):
    who_failed = []
    try:
        for student in range(len(students_data)):
            if float(students_data[student]["English"]) < 60 or float(students_data[student]["Spanish"]) < 60 or float(students_data[student]["Social Studies"]) < 60 or  float(students_data[student]["Science"]) < 60:
                new_who_failed = {
                    "Name": students_data[student]["Name"],
                    "Section": students_data[student]["Section"],
                }
                if float(students_data[student]["Spanish"]) < 60:
                    new_who_failed["Spanish"] = (students_data[student]["Spanish"])
                if float(students_data[student]["English"]) < 60:
                    new_who_failed["English"] = students_data[student]["English"]
                if float(students_data[student]["Social Studies"]) < 60:
                    new_who_failed["Social Studies"] = students_data[student]["Social Studies"]
                if float(students_data[student]["Science"]) < 60:
                    new_who_failed["Science"] = students_data[student]["Science"]
                who_failed.append(new_who_failed)
        for student in range(len(who_failed)):
            for key, value in who_failed[student].items():
                print(f"{key}: {value}")
            print()
    except Exception as ex:
        print(f"Error: {ex}\n")
    return print()

