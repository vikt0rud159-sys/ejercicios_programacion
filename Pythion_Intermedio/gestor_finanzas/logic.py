from datetime import datetime
from models import Categoria, Movimiento


class ApplicationLogic:

    def __init__(self):
        self.headers = ["Fecha", "Título", "Categoría", "Monto", "Tipo"]
        self.categories = []
        self.movements = []

    def set_data(self, categories, movements):
        self.categories = categories
        self.movements = movements

    def get_current_date(self):
        return datetime.now().date().isoformat()

    def add_category(self, name, color):
        if not name or name.strip() == "":
            raise ValueError("invalid_category_name")
        if any(cat.name == name.strip() for cat in self.categories):
            raise ValueError("duplicate_category")
        category = Categoria(name, color)
        self.categories.append(category)
        return category

    def add_movement(self, title, amount, category_name, movement_label, date):
        category = next(
            (cat for cat in self.categories if cat.name == category_name),
            None
        )
        if not category:
            raise ValueError("category_not_found")
        movement_type = "Gasto" if movement_label == "Gasto" else "Ingreso"
        movement = Movimiento(
            title,
            amount,
            category,
            movement_type,
            date
        )
        self.movements.append(movement)

    def get_movements(self):
        return self.movements

    def filter_by_date(self, start_date, end_date):
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d").date()
            end = datetime.strptime(end_date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("invalid_date")
        return [
            m for m in self.movements
            if start <= m.date <= end
        ]

    def calculate_totals(self):
        income = sum(m.amount for m in self.movements if m.type == "Ingreso")
        expenses = abs(sum(m.amount for m in self.movements if m.type == "Gasto"))
        return income, expenses, income - expenses
