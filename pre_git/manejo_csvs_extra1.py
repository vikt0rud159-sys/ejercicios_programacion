import csv


def read_csv_headers(file_path):
    with open(file_path, encoding="utf-8") as file:
        reader = csv.DictReader(file)
        headers = reader.fieldnames
    return headers


def read_csv_file(file_path, headers):
    with open(file_path, encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            nombre, genero, desarrollador, clasificacion = row
            print(f"{headers[0]}: {nombre}")
            print(f"{headers[1]}: {genero}")
            print(f"{headers[2]}: {desarrollador}")
            print(f"{headers[3]}: {clasificacion}")
            print()


def read_csv():
    try:
        headers = read_csv_headers("videojuegos.csv")
        read_csv_file("videojuegos.csv", headers)
    except Exception as ex:
        print(f"Error: {ex}")


read_csv()