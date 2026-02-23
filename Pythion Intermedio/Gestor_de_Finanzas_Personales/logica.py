import FreeSimpleGUI as sg
from datetime import datetime
from persistencia import Persistence


class ApplicationLogic:
    
    def __init__(self):
        self.table_values = []
        self.categorys = []
        self.headers = ["Fecha", "Título", "Categoría", "Monto", "Tipo"]
        self.persistence = Persistence()
        self.window = None

    def get_category_color(self, name):
        for category in self.categorys:
            if isinstance(category, dict) and category.get("name") == name:
                return category.get("color") or "#FFFFFF"
            if isinstance(category, (list, tuple)) and category[0] == name:
                return category[1] if len(category) > 1 else "#FFFFFF"
        return "#FFFFFF"

    def update_table_colors(self):
        row_colors = []
        for row_index, row in enumerate(self.table_values):
            category_name = row[2] if len(row) > 2 else None
            if category_name:
                color = self.get_category_color(category_name)
                row_colors.append((row_index, color))
        try:
            if self.window is not None:
                self.window["-TABLA-"].update(row_colors=row_colors)
        except Exception:
            pass

    def filter_by_date(self, start_date_str, end_date_str):
        try:
            start_date = datetime.strptime(str(start_date_str), "%Y-%m-%d").date() if start_date_str else None
            end_date = datetime.strptime(str(end_date_str), "%Y-%m-%d").date() if end_date_str else None
            filtered_values = []
            for row in self.table_values:
                row_date = row[0]
                if isinstance(row_date, str):
                    try:
                        row_date = datetime.strptime(row_date, "%Y-%m-%d").date()
                    except ValueError:
                        continue
                if (not start_date or row_date >= start_date) and (not end_date or row_date <= end_date):
                    filtered_values.append(row)
            self.window["-TABLA-"].update(values=filtered_values)
            filtered_row_colors = []
            for row_index, row in enumerate(filtered_values):
                category_name = row[2] if len(row) > 2 else None
                if category_name:
                    filtered_row_colors.append((row_index, self.get_category_color(category_name)))
            self.window["-TABLA-"].update(row_colors=filtered_row_colors)
        except ValueError:
            sg.popup("Error:\nFormato de fecha inválido. Use YYYY-MM-DD.")

    def show_category_window(self):
        layout = [
            [sg.Text("Agregar nueva categoría:")],
            [sg.Input(key="input_categoria")],
            [sg.Text("Agregar color:")],
            [sg.Input("#FFFFFF", key="input_color", size=(15,1), readonly=True), sg.ColorChooserButton("Elegir color", target="input_color")],
            [sg.Button("Agregar"), sg.Button("Cancelar")]
        ]
        category_window = sg.Window("Nueva Categoría", layout, modal=True)
        while True:
            event, values = category_window.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                break
            elif event == "Agregar":
                name = values.get("input_categoria")
                color = values.get("input_color") or "#FFFFFF"
                if name:
                    category_window.close()
                    return (name, color)
        category_window.close()
        return None

    def show_add_movement_window(self, movement):
        category_names = [category["name"] if isinstance(category, dict) else (category[0] if isinstance(category, (list, tuple)) else str(category)) for category in self.categorys]
        layout = [
            [sg.Text("Título:")],
            [sg.Input(key="input_título")],
            [sg.Text("Monto:")],
            [sg.Input(key="input_monto")],
            [sg.Text("Categoría :"), sg.Combo(category_names, key="input_categoría", readonly=True, size=(20, 1))],
            [sg.Text("Fecha: YYYY-MM-DD"), sg.Input(datetime.now().date(), key="input_fecha", size=(12, 1))],
            [sg.Button("Agregar"), sg.Button("Cancel")],
        ]
        movements_window = sg.Window(movement, layout, modal=True)
        while True:
            event, values = movements_window.read()
            if event in (sg.WIN_CLOSED, "Cancel"):
                break
            elif event == "Agregar":
                title = values["input_título"]
                amount = values["input_monto"]
                category = values["input_categoría"]
                if title and amount and category:
                    try:
                        if (amount := float(amount)) <= 0: raise ValueError
                        try:
                            date = datetime.strptime(values["input_fecha"], "%Y-%m-%d").date()
                            if date > datetime.now().date(): raise ValueError("fecha_futura.")
                        except ValueError as error:
                            if "fecha_futura." in str(error):
                                sg.popup("Error:\nLa fecha no puede ser futura. Se usará la fecha actual.", title="error_fecha")
                            else:
                                date = datetime.now().date()
                                sg.popup("Formato de fecha inválido. Se usará la fecha actual.", title="error_fecha")
                        if movement == "Agregar Gasto":
                            amount = -amount
                        self.table_values.append([date, title, category, f"₡{amount}", "Gasto" if movement == "Agregar Gasto" else "Ingreso"])
                        self.window["-TABLA-"].update(values=self.table_values)
                        self.update_table_colors()
                        break
                    except ValueError:
                        sg.popup_error("Error:\nEl monto debe ser un número válido.", title="error_monto")
        movements_window.close()

    def calculate_totals(self):
        income = expenses = 0
        for row in self.table_values:
            try:
                amount = float(str(row[3]).replace("₡", "").strip())
                if row[4] == "Ingreso":
                    income += amount
                else:
                    expenses += abs(amount)
            except (ValueError, IndexError):
                pass
        return income, expenses, (income - expenses)

    def load_data(self):
        data = self.persistence.read_data()
        self.categorys = data["categorys"]
        self.table_values = data["table_values"]

    def show_main_window(self):
        layout = [
            [sg.Text("Gestor de Finanzas Personales:", font=("Arial", 16))],
            [sg.Push(), sg.Text("Filtrar por fecha:", font=("Arial", 14)), sg.Text("Desde:"), sg.Input(datetime.now().date(), key="input_fecha_inicio", size=(12, 1)), sg.Text("Hasta:"), sg.Input(datetime.now().date(), key="input_fecha_fin", size=(12, 1)), sg.Button("Filtrar")],
            [sg.Table(
                values=self.table_values,
                headings=self.headers,
                size=(120, 20), auto_size_columns=False, justification="center",
                key="-TABLA-"
            )],
            [sg.Text("Agregar:", font=("Arial", 11))],
            [sg.Button("Categoría"), sg.Button("Gasto"), sg.Button("Ingreso"), sg.Push(), sg.Button("Exportar CSV", button_color=("white", "green"))],
        ]
        self.window = sg.Window("Gestor de Finanzas Personales", layout, finalize=True)
        self.update_table_colors()
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                break
            elif event == "Categoría":
                new_category = self.show_category_window()
                if new_category:
                    name, color = new_category
                    self.categorys.append({"name": name, "color": color})
            elif len(self.categorys) == 0:
                sg.popup("Error:\nTodavía no tienes categorías creadas.", title="error_categorias")
            elif event == "Gasto":
                self.show_add_movement_window(movement="Agregar Gasto")
            elif event == "Ingreso":
                self.show_add_movement_window(movement="Agregar Ingreso")
            elif event == "Exportar CSV":
                income, expenses, balance = self.calculate_totals()
                self.persistence.write_data(self.categorys, self.table_values, income, expenses, balance)
                sg.popup("Datos exportados exitosamente a \"datos.csv\"", title="Exportación Exitosa")
            elif event == "Filtrar":
                self.filter_by_date(values["input_fecha_inicio"], values["input_fecha_fin"])
        self.window.close()