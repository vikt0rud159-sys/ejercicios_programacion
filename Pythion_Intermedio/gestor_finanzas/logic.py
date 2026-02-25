from datetime import datetime
from persistence import Persistence


class CategoryManager():
    def get_categories(self,values=None):
        name = values.get("input_category")
        color = values.get("input_color") or "#FFFFFF"
        if name and name.strip() != "" and name.strip() not in [category["name"] for category in self.categories if isinstance(category, dict)] and name.strip() not in [category[0] for category in self.categories if isinstance(category, (list, tuple))]:
            return (name, color)
        else:
            return (None, None)

    def get_category_color(self, name):
        for category in self.categories:
            if isinstance(category, dict) and category.get("name") == name:
                return category.get("color") or "#FFFFFF"
            if isinstance(category, (list, tuple)) and category[0] == name:
                return category[1] if len(category) > 1 else "#FFFFFF"
        return "#FFFFFF"


class FinancialMovments:
    def filter_by_date(self, start_date_str, end_date_str):
            start_date = datetime.strptime(str(start_date_str), "%Y-%m-%d").date() if start_date_str else None
            end_date = datetime.strptime(str(end_date_str), "%Y-%m-%d").date() if end_date_str else None
            filtered_rows = []
            for row in self.table_rows:
                row_date = row[0]
                if isinstance(row_date, str):
                    try:
                        row_date = datetime.strptime(row_date, "%Y-%m-%d").date()
                    except ValueError:
                        return
                if (not start_date or row_date >= start_date) and (not end_date or row_date <= end_date):
                    filtered_rows.append(row)
            self.window["-TABLE-"].update(values=filtered_rows)
            filtered_row_colors = []
            for row_index, row in enumerate(filtered_rows):
                category_name = row[2] if len(row) > 2 else None
                if category_name:
                    filtered_row_colors.append((row_index, self.get_category_color(category_name)))
            self.window["-TABLE-"].update(row_colors=filtered_row_colors)

    def calculate_totals(self):
        income = expenses = 0
        for row in self.table_rows:
            try:
                amount = float(str(row[3]).replace("₡", "").strip())
                if row[4] == "Ingreso":
                    income += amount
                else:
                    expenses += abs(amount)
            except (ValueError, IndexError):
                pass
        return income, expenses, (income - expenses)

    def add_movement(self, title, amount, category, movement, date=None):
        if (amount := float(amount)) <= 0: raise ValueError
        if title.strip() == "": raise ValueError("title_error")
        try:
            date = datetime.strptime(date, "%Y-%m-%d").date()
            if date > self.get_date(): raise ValueError("future_date")
        except ValueError as error:
            if "future_date" in str(error):
                raise ValueError("future_date")
            else:
                date = self.get_date()
                raise ValueError("invalid_date")
        if movement == "Agregar Gasto": amount = -amount
        self.table_rows.append([date, title, category, f"₡{amount}", "Gasto" if movement == "Agregar Gasto" else "Ingreso"])
        self.window["-TABLE-"].update(values=self.table_rows)
        self.update_table_colors()
        return

    def get_date(self):
        return datetime.now().date()


class ApplicationLogic(Persistence, CategoryManager, FinancialMovments):
    def __init__(self):
            super().__init__()
            self.headers = ["Fecha", "Título", "Categoría", "Monto", "Tipo"]
            self.persistence = Persistence()

    def update_table_colors(self):
        row_colors = []
        for row_index, row in enumerate(self.table_rows):
            category_name = row[2] if len(row) > 2 else None
            if category_name:
                color = self.get_category_color(category_name)
                row_colors.append((row_index, color))
        try:
            if self.window is not None:
                self.window["-TABLE-"].update(row_colors=row_colors)
        except Exception:
            pass
