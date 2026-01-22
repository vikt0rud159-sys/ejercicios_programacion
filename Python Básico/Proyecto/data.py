import csv


def export_csv(file_path, data, headers):
    try:
        with open(file_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            writer.writerows(data)
        return print("Información exportada\n")
    except Exception as ex:
        print(f"Error: {ex}\n")


def import_csv():
    try:
        students_data = []
        with open("students.csv", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students_data.append(row)
    except FileNotFoundError:
        print("   ¡Archivo no encontrado!\n")
    return students_data