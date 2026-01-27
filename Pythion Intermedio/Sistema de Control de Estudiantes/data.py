import csv


def export_csv(file_path, data, headers):
    try:
        with open(file_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, headers)
            writer.writeheader()
            for obj in data:
                obj_dict = vars(obj)
                obj_dict = {key: str(value).replace("(", "").replace(",", "").replace(")", "") for key, value in obj_dict.items()}
                writer.writerow(obj_dict)
        print("   Información exportada\n")
    except Exception as ex:
        print(f"Error: {ex}\n")


def import_csv():
    try:
        imported = []
        with open("students.csv", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                imported.append(row)
    except FileNotFoundError:
        print("   ¡Archivo no encontrado!\n")
    return imported