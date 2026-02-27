import csv
from models import Categoria, Movimiento


class Persistence:

    def read_data(self):
        categories = []
        movements = []
        try:
            with open("datos.csv", newline="", encoding="utf-8") as file:
                for row in csv.reader(file):
                    if not row:
                        continue
                    tag = row[0].strip().upper()
                    if tag == "CATEGORY":
                        categories.append(
                            Categoria(row[1], row[2] if len(row) > 2 else "#FFFFFF")
                        )
                    elif tag == "RESUMEN":
                        break
                    elif row[0] != "Fecha":
                        date, title, category_name, amount, movement_type = row
                        category = next(
                            (cat for cat in categories if cat.name == category_name),
                            None
                        )
                        if category:
                            amount = amount.replace("₡", "")
                            movements.append(
                                Movimiento(
                                    title,
                                    abs(float(amount)),
                                    category,
                                    movement_type,
                                    date
                                )
                            )
        except FileNotFoundError:
            pass
        return categories, movements

    def write_data(self, categories, movements, income, expenses, balance):
        with open("datos.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for category in categories:
                writer.writerow(["CATEGORY", category.name, category.color])
            writer.writerow([])
            writer.writerow(["Fecha", "Título", "Categoría", "Monto", "Tipo"])
            for movement in movements:
                writer.writerow(movement.to_row())
            writer.writerow([])
            writer.writerow(["RESUMEN"])
            writer.writerow(["Ingresos totales", f"₡{income}"])
            writer.writerow(["Gastos totales", f"₡{expenses}"])
            writer.writerow(["Balance neto", f"₡{balance}"])
