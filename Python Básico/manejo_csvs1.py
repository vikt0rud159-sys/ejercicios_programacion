import csv


video_games_list = [
	{
		"Nombre": "Grand Theft Auto IV",
		"Género": "Accion",
		"Desarrollador": "Rockstar Games",
		"Clasificación ESRB": "M",
	},
	{
		"Nombre": "The Elder Scrolls IV",
		"Género": "RPG",
		"Desarrollador": "Bethesda",
		"Clasificación ESRB": "M",
	},
	{
		"Nombre": "Tony Hawk's Pro Skater 2",
		"Género": "Deportes",
		"Desarrollador": "Activision",
		"Clasificación ESRB": "T",
	},
]


video_games_headers = (
	"Nombre",
	"Género",
	"Desarrollador",
	"Clasificación ESRB",
)


def write_csv_file(file_path, data, headers):
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(data)

write_csv_file("videojuegos.csv", video_games_list, video_games_headers)