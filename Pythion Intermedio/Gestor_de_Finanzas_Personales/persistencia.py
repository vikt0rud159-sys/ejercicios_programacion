import csv


class Persistence:
    def __init__(self):
        self.headers = ["Fecha", "Título", "Categoría", "Monto", "Tipo"]

    def read_data(self):
        categorys = []
        table_values = []
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
                        categorys.append({"name": name, "color": color})
                    elif tag == "RESUMEN":
                        break
                    else:
                        if row != self.headers:
                            table_values.append(row)
        except FileNotFoundError:
            pass
        return {"categorys": categorys, "table_values": table_values}

    def write_data(self, categorys, table_values, income=0, expenses=0, balance=0):
        with open("datos.csv", "w", newline="", encoding="utf-8") as file:
            write = csv.writer(file)
            for cat in categorys:
                if isinstance(cat, dict):
                    write.writerow(["CATEGORY", cat.get("name"), cat.get("color", "#FFFFFF")])
                elif isinstance(cat, (list, tuple)):
                    write.writerow(["CATEGORY", cat[0], cat[1] if len(cat) > 1 else "#FFFFFF"])
                else:
                    write.writerow(["CATEGORY", str(cat), "#FFFFFF"])
            write.writerow([])
            write.writerow(["Fecha", "Título", "Categoría", "Monto", "Tipo"])
            for row in table_values:
                new_row = list(row)
                if hasattr(new_row[0], "isoformat"):
                    new_row[0] = new_row[0].isoformat()
                write.writerow(new_row)
            write.writerow([])
            write.writerow(["RESUMEN"])
            write.writerow(["Ingresos totales", f"₡{income}"])
            write.writerow(["Gastos totales", f"₡{expenses}"])
            write.writerow(["Balance neto", f"₡{balance}"])