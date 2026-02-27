import FreeSimpleGUI as sg
from logic import ApplicationLogic
from persistence import Persistence


class FinancialManager:

    def __init__(self):
        sg.theme("NeutralBlue")
        self.logic = ApplicationLogic()
        self.persistence = Persistence()
        categories, movements = self.persistence.read_data()
        self.logic.set_data(categories, movements)

    def refresh_table(self, window, movements=None):
        if movements is None:
            movements = self.logic.get_movements()
        data = [m.to_row() for m in movements]
        row_colors = []
        for i, m in enumerate(movements):
            text_color = "black"
            row_colors.append((i, text_color, m.category.color))
        table = window["-TABLE-"]
        table.update(values=data)
        if data:
            table.update(row_colors=row_colors)

    def show_main_window(self):
        layout = [
            [sg.Text("Gestor de Finanzas Personales:", font=("Arial", 16, "bold"))],
            [sg.Push(),
            sg.Text("Filtrar por fecha:", font=("Arial", 14, )),
            sg.Text("Desde:"),
            sg.Input(key="input_start_date", size=(12, 1)),
            sg.Text("Hasta:"),
            sg.Input(key="input_end_date", size=(12, 1)),
            sg.Button("Filtrar")],
            [sg.Table(
                values=[],
                headings=self.logic.headers,
                size=(120, 20),
                key="-TABLE-",
                auto_size_columns=False,
                justification="center",
                font=("Arial", 11, "bold")
            )],
            [sg.Text("Agregar:", font=("Arial", 11))],
            [sg.Button("Categoría"),
            sg.Button("Gasto"),
            sg.Button("Ingreso"),
            sg.Push(),
            sg.Button("Exportar CSV", button_color=("white", "green"))],
        ]
        window = sg.Window("Gestor de Finanzas Personales", layout, finalize=True)
        window.read(timeout=0)
        self.refresh_table(window)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                income, expenses, balance = self.logic.calculate_totals()
                self.persistence.write_data(
                    self.logic.categories,
                    self.logic.movements,
                    income,
                    expenses,
                    balance
                )
                break
            elif event == "Categoría":
                self.show_category_window(window)
            elif event in ("Gasto", "Ingreso"):
                if not self.logic.categories:
                    sg.popup_error(
                    "Error:\nTodavía no tienes categorías creadas.",
                    title="error_categorías"
                    )
                    continue
                self.show_movement_window(window, event)
            elif event == "Exportar CSV":
                income, expenses, balance = self.logic.calculate_totals()
                self.persistence.write_data(
                    self.logic.categories,
                    self.logic.movements,
                    income,
                    expenses,
                    balance
                )
                sg.popup(
                    "Datos exportados exitosamente a \"datos.csv\"",
                    title="Exportación Exitosa"
                    )
            elif event == "Filtrar":
                try:
                    filtered = self.logic.filter_by_date(
                        values["input_start_date"],
                        values["input_end_date"]
                    )
                    self.refresh_table(window, filtered)
                except ValueError:
                    sg.popup_error(
                    "Error:\nFormato de fecha incorrecto. Use YYYY/MM/DD",
                    title="fecha_invalida"
                    )
        window.close()

    def show_category_window(self, parent):
        layout = [
            [sg.Text("Agregar nueva categoría:")],
            [sg.Input(key="input_category")],
            [sg.Text("Agregar color:")],
            [sg.Input("#FFFFFF", key="input_color", size=(15, 1), readonly=True),
            sg.ColorChooserButton("Elegir color", target="input_color")],
            [sg.Button("Agregar"), sg.Button("Cancelar")]
        ]
        win = sg.Window("Nueva Categoría", layout, modal=True)
        while True:
            event, values = win.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                break
            elif event == "Agregar":
                try:
                    self.logic.add_category(
                        values["input_category"],
                        values["input_color"]
                    )
                    break
                except ValueError:
                    sg.popup_error(
                        "Error:\nNo se pudo crear la categoría: ya existe o no cumple los criterios requeridos.",
                        title="error_categoría"
                        )
        win.close()
        self.refresh_table(parent)

    def show_movement_window(self, parent, movement_label):
        category_names = [c.name for c in self.logic.categories]
        layout = [
            [sg.Text("Título:")],
            [sg.Input(key="input_title")],
            [sg.Text("Monto:")],
            [sg.Input(key="input_amount")],
            [sg.Text("Categoría:"),
            sg.Combo(category_names, key="input_category", readonly=True)],
            [sg.Text("Fecha (YYYY-MM-DD):")],
            [sg.Input(self.logic.get_current_date(), key="input_date")],
            [sg.Button("Agregar"), sg.Button("Cancelar")]
        ]
        win = sg.Window(movement_label, layout, modal=True)
        while True:
            event, values = win.read()
            if event in (sg.WIN_CLOSED, "Cancelar"):
                break
            elif event == "Agregar":
                try:
                    if values["input_date"] > self.logic.get_current_date():
                        raise ValueError("future_date")
                    self.logic.add_movement(
                        values["input_title"],
                        values["input_amount"],
                        values["input_category"],
                        movement_label,
                        values["input_date"]
                    )
                    break
                except ValueError as ex:
                    if str(ex) == "category_not_found":
                        sg.popup_error(
                            "Error:\nDebe seleccionar una categoría antes de continuar.",
                            title="error_category"
                            )
                    elif str(ex) == "title_error":
                        sg.popup_error(
                            "Error:\nEl título no es válido. Verifique el formato e intente nuevamente.",
                            title="error_title"
                            )
                    elif str(ex) == "invalid_amount":
                        sg.popup_error(
                            "Error:\nEl monto debe ser un número válido.",
                            title="error_monto"
                            )
                    elif str(ex) == "invalid_date":
                        sg.popup_error(
                            "Error:\nFormato de fecha incorrecto. Use YYYY/MM/DD",
                            title="fecha_invalida"
                            )
                    elif str(ex) == "future_date":
                        sg.popup_error(
                            "Error:\nLa fecha debe ser igual o anterior a la fecha actual.",
                            title="error_fecha"
                            )
        win.close()
        self.refresh_table(parent)

def main():
    app = FinancialManager()
    app.show_main_window()


if __name__ == "__main__":
    main()
