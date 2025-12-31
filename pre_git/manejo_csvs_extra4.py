import csv


def search_dev_csv(file_path):
    try:
        search = input("Buscar desarrolladora: ")
        print(f"\nVideojuegos desarrollados por {search}")
        with open(file_path, encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[2] == search:
                    print(f"- {row[0]}")
    except Exception as ex:
        print(f"Error: {ex}")


search_dev_csv("videojuegos.csv")