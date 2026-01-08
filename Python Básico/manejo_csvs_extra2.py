import csv


def search_esrb_csv(file_path):
    try:
        search = input("Buscar clasificación ESRB:")
        search = search.upper()
        count = 0
        with open(file_path, encoding="utf-8") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3] == search:
                    count += 1
        print(count)
    except Exception as ex:
        print(f"Error: {ex}")


search_esrb_csv("videojuegos.csv")