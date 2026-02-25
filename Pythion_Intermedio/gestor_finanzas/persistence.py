import csv


class Persistence:
    def __init__(self):
        self.headers = ["Fecha", "Título", "Categoría", "Monto", "Tipo"]
        self.categories = []
        self.table_rows = []

    def read_data(self):
        try:
            with open("datos.csv", newline="", encoding="utf-8") as file:
                for row in csv.reader(file):
                    if not row:
                        continue
                    tag = row[0].strip().upper()
                    if tag == "FECHA":
                        continue
                    if tag == "CATEGORY":
                        name = row[1] if len(row) > 1 else ""
                        color = row[2] if len(row) > 2 and row[2] else "#FFFFFF"
                        self.categories.append({"name": name, "color": color})
                    elif tag == "RESUMEN":
                        break
                    else:
                        if row != self.headers:
                            self.table_rows.append(row)
        except FileNotFoundError:
            pass

    def write_data(self=0, categories=0, table_rows=0, income=0, expenses=0, balance=0):
        with open("datos.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for category in categories:
                if isinstance(category, dict):
                    writer.writerow(["CATEGORY", category.get("name"), category.get("color", "#FFFFFF")])
                elif isinstance(category, (list, tuple)):
                    writer.writerow(["CATEGORY", category[0], category[1] if len(category) > 1 else "#FFFFFF"])
                else:
                    writer.writerow(["CATEGORY", str(category), "#FFFFFF"])
            writer.writerow([])
            writer.writerow(["Fecha", "Título", "Categoría", "Monto", "Tipo"])
            for row in table_rows:
                new_row = list(row)
                if hasattr(new_row[0], "isoformat"):
                    new_row[0] = new_row[0].isoformat()
                writer.writerow(new_row)
            writer.writerow([])
            writer.writerow(["RESUMEN"])
            writer.writerow(["Ingresos totales", f"₡{income}"])
            writer.writerow(["Gastos totales", f"₡{expenses}"])
            writer.writerow(["Balance neto", f"₡{balance}"])
