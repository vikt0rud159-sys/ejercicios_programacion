import csv


def classify_genres_csv(file_path, gender_dict):
    with open(file_path, encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1] in gender_dict:
                gender_dict[row[1]] += 1
            else:
                gender_dict[row[1]] = 1


def show_gender_csv():
    try:
        gender_dict = {}
        classify_genres_csv("videojuegos.csv", gender_dict)
        for gender, value in gender_dict.items():
            print(f"{gender}: {value}")
    except Exception as ex:
        print(f"Error: {ex}")


show_gender_csv()