import FreeSimpleGUI as sg # type: ignore
from logic import ApplicationLogic


class FinancialManager(ApplicationLogic):

    def __init__(self):
        super().__init__()
        sg.theme("NeutralBlue")
        self.name = None

    def show_main_window(self):
        layout = [
            [sg.Text("Gestor de Finanzas Personales:", font=("Arial", 16))],
            [sg.Push(), sg.Text("Filtrar por fecha:", font=("Arial", 14)), sg.Text("Desde:"), sg.Input(self.get_date(), key="input_start_date", size=(12, 1)), sg.Text("Hasta:"), sg.Input(self.get_date(), key="input_end_date", size=(12, 1)), sg.Button("Filtrar")],
            [sg.Table(
                values=self.table_rows,
                headings=self.headers,
                size=(120, 20), auto_size_columns=False, justification="center",
                key="-TABLE-"
            )],
            [sg.Text("Agregar:", font=("Arial", 11))],
            [sg.Button("Categoría"), sg.Button("Gasto"), sg.Button("Ingreso"), sg.Push(), sg.Button("Exportar CSV", button_color=("white", "green"))],
        ]

        self.window = sg.Window("Gestor de Finanzas Personales", layout, finalize=True)
        self.update_table_colors()
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED:
                income, expenses, balance = self.calculate_totals()
                self.persistence.write_data(self.categories, self.table_rows, income, expenses, balance)
                break

            elif event == "Categoría":
                self.show_category_window()
                if self.name and self.color: self.categories.append({"name": self.name, "color": self.color})
            elif len(self.categories) == 0: sg.popup("Error:\nTodavía no tienes categorías creadas.", title="error_categorías")
            elif event == "Gasto": self.show_add_movement_window(movement="Agregar Gasto")
            elif event == "Ingreso": self.show_add_movement_window(movement="Agregar Ingreso")
            elif event == "Exportar CSV":
                income, expenses, balance = self.calculate_totals()
                self.persistence.write_data(self.categories, self.table_rows, income, expenses, balance)
                sg.popup("Datos exportados exitosamente a \"datos.csv\"", title="Exportación Exitosa")
            elif event == "Filtrar":
                self.filter_by_date(values["input_start_date"], values["input_end_date"])
        self.window.close()

    def show_category_window(self):
        layout = [
            [sg.Text("Agregar nueva categoría:")],
            [sg.Input(key="input_category")],
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

                    self.name, self.color = self.get_categories(values)
                    if self.name is None: sg.popup_error("Error:\nNo se pudo crear la categoría: ya existe o no cumple los criterios requeridos.", title="error_categoría")
            category_window.close()
        category_window.close()
        return None

    def show_add_movement_window(self, movement):
        category_names = [category["name"] if isinstance(category, dict) else (category[0] if isinstance(category, (list, tuple)) else str(category)) for category in self.categories]
        layout = [
            [sg.Text("Título:")],
            [sg.Input(key="input_title")],
            [sg.Text("Monto:")],
            [sg.Input(key="input_amount")],
            [sg.Text("Categoría :"), sg.Combo(category_names, key="input_category", readonly=True, size=(20, 1))],
            [sg.Text("Fecha: YYYY-MM-DD"), sg.Input(self.get_date(), key="input_date", size=(12, 1))],
            [sg.Button("Agregar"), sg.Button("Cancel")],
        ]

        movement_window = sg.Window(movement, layout, modal=True)
        while True:
            event, values = movement_window.read()
            if event in (sg.WIN_CLOSED, "Cancel"):
                break

            elif event == "Agregar":
                title = values["input_title"]
                amount = values["input_amount"]
                category = values["input_category"]
                if title and amount and category:
                    try:
                        self.add_movement(title, amount, category, movement, date=values["input_date"])
                        break
                    except ValueError as error:
                        if "title_error" in str(error):
                            sg.popup_error("Error:\nEl título no es válido. Verifique el formato e intente nuevamente.", title="error_titulo")
                        elif "future_date" in str(error):
                            sg.popup_error("Error:\nLa fecha debe ser igual o anterior a la fecha actual.", title="error_fecha")
                        elif "invalid_date" in str(error):
                            sg.popup_error("Error:\nFormato de fecha incorrecto. Use YYYY/MM/DD", title="fecha_invalida")
                        else:
                            sg.popup_error("Error:\nEl monto debe ser un número válido.", title="error_monto")
        movement_window.close()

def main():
    try:
        account = FinancialManager()
        account.read_data()
        account.show_main_window()
    except Exception as ex:
        sg.popup_error(f"Se produjo un error inesperado durante la operación:\n {ex}", title="Error Inesperado")


if __name__ == "__main__":
    main()
