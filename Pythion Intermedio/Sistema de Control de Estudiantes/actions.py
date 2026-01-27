class StudentInfo:
    def __init__(self, students_data, imported, main_student):
        main_studemt=0
        try:
            if len(imported) > 0:
                self.name = imported[main_student]["name"]
                self.section = imported[main_student]["section"]
                self.spanish = imported[main_student]["spanish"].replace("(","").replace(",","").replace(")","")
                self.english = imported[main_student]["english"].replace("(","").replace(",","").replace(")","")
                self.social_studies = imported[main_student]["social_studies"].replace("(","").replace(",","").replace(")","")
                self.science = imported[main_student]["science"].replace("(","").replace(",","").replace(")","")
                self.average = imported[main_student]["average"].replace("(","").replace(",","").replace(")","")
                return
            self.name = get_name()
            self.section = get_section()
            for student in students_data:
                if student.name == self.name:
                    print("¡Estudiante ya registrado!\n")
                    return "No"
            self.spanish = float(get_spanish_note()),
            self.english = float(get_english_note()),
            self.social_studies = float(get_social_studies_note()),
            self.science = float(get_science_note()),
            self.average = sum(self.spanish + self.english + self.social_studies + self.science) / 4
        except Exception as ex:
            print(f"Error: {ex}\n")


def add_student(students_data, imported, main_student):
    try:
        new_student = StudentInfo(students_data, imported, main_student)
        students_data.append(new_student)
    except TypeError:
        ""


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


def get_higher_average(students_data):
    student_higher = []
    higher = []
    try:
        if len(students_data) == 0:
            print("   ¡No hay datos!\n")
            return
        for student in range(len(students_data)):
            if len(student_higher) == 0:
                student_higher = [students_data[0].name]
                higher = [students_data[0].average]
            elif float(students_data[student].average) >= float(higher[0]):
                student_higher.insert(0, students_data[student].name)
                higher.insert(0, students_data[student].average)
            elif len(student_higher) == 1:
                student_higher.append(students_data[student].name)
                higher.append(students_data[student].average)
            elif float(students_data[student].average) >= float(higher[1]):
                student_higher.insert(1, students_data[student].name)
                higher.insert(1, students_data[student].average)
            elif len(student_higher) == 2:
                student_higher.append(students_data[student].name)
                higher.append(students_data[student].average)
            elif len(student_higher) <= 3:
                if float(students_data[student].average) >= float(higher[2]):
                    student_higher.insert(2, students_data[student].name)
                    higher.insert(2, students_data[student].average)
        for top in range(len(student_higher)):
            if top == 3:
                print()
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
                general_average = float(average.average)
                counter = 1
            else:
                general_average += float(average.average)
                counter += 1
        return print(f"Promedio general: {general_average / counter}\n")
    except UnboundLocalError:
        print("   ¡No hay datos!\n")
    except Exception as ex:
        print(f"Error: {ex}\n")


def del_student(students_data):
    try:
        del_name = get_name()
        del_sec = get_section()
        for index in range(len(students_data)):
            if students_data[index].name.lower() == del_name.lower() and students_data[index].section.lower() == del_sec.lower():
                confirm = input(f"Confirmación requerida (Presione [S])    ")
                if confirm.lower() == "s":
                    students_data.remove(students_data[index])
                    print(f"[Nombre: {del_name}][Sección: {del_sec}] Eliminado con éxito.\n")
                else:
                    print("¡Eliminación de estudiante cancelada!\n")
                    return
        else:
            print("   ¡Estudiante no encontrado!\n")
    except IndexError:
        ""
    except Exception as ex:
        print(f"Error: {ex}\n")


def students_who_failed(students_data):
    who_failed = []
    try:
        for student in range(len(students_data)):
            if students_data[student].english[0] < 60 or students_data[student].spanish[0] < 60 or students_data[student].social_studies[0] < 60 or  students_data[student].science[0] < 60:
                new_who_failed = {
                    "Name": students_data[student].name,
                    "Section": students_data[student].section,
                }
                if students_data[student].spanish[0] < 60:
                    new_who_failed["Spanish"] = (students_data[student].spanish)
                if students_data[student].english[0] < 60:
                    new_who_failed["English"] = students_data[student].english
                if students_data[student].social_studies[0] < 60:
                    new_who_failed["Social Studies"] = students_data[student].social_studies
                if students_data[student].science[0] < 60:
                    new_who_failed["Science"] = students_data[student].science
                who_failed.append(new_who_failed)
        for student in range(len(who_failed)):
            for key, value in who_failed[student].items():
                print(f"{key}: {value[0]}")
            print()
    except Exception as ex:
        print(f"Error: {ex}\n")
    return print()
