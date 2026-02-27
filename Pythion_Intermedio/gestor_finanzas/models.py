from datetime import datetime


class Categoria:

    def __init__(self, name, color="#FFFFFF"):
        if not name or name.strip() == "":
            raise ValueError("invalid_category_name")
        self.name = name.strip()
        self.color = color or "#FFFFFF"


class Movimiento:

    def __init__(self, title, amount, category, movement_type, date):
        if not title or title.strip() == "":
            raise ValueError("title_error")
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("invalid_amount")
        if amount <= 0:
            raise ValueError("invalid_amount")
        try:
            date = datetime.strptime(date, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError("invalid_date")
        if movement_type not in ("Ingreso", "Gasto"):
            raise ValueError("invalid_type")
        if movement_type == "Gasto":
            amount = -amount
        self.title = title.strip()
        self.amount = amount
        self.category = category
        self.type = movement_type
        self.date = date

    def to_row(self):
        return [
            self.date.isoformat(),
            self.title,
            self.category.name,
            f"₡{self.amount}",
            self.type
        ]
