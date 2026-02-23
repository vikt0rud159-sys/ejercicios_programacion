import FreeSimpleGUI as sg
from datetime import datetime
from logica import ApplicationLogic


class FinancialManager(ApplicationLogic):

    def __init__(self):
        super().__init__()
        sg.theme("NeutralBlue")

    def show_main_window(self):
        layout = [
            [sg.Text("Gestor de Finanzas Personales:", font=("Arial", 16))],
            [sg.Push(), sg.Text("Filtrar por fecha:", font=("Arial", 14)),sg.Text("Desde:"), sg.Input(datetime.now().date(), key="input_fecha_inicio", size=(12, 1)), sg.Text("Hasta:"), sg.Input(datetime.now().date(), key="input_fecha_fin", size=(12, 1)), sg.Button("Filtrar")],
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
                self.persistence.write_data(self.categorys, self.table_values)
                sg.popup("Gracias por usar el Gestor de Finanzas Personales.\nDatos guardados exitosamente.", title="Guardado Exitoso", auto_close=True, auto_close_duration=1.2)
                break
            elif event == "Categoría":
                new_category = self.show_category_window()
                if new_category:
                    name, color = new_category
                    self.categorys.append({"name": name, "color": color})
            elif len(self.categorys) == 0: sg.popup("Error:\nTodavía no tienes categorías creadas.", title="error_categorias")
            elif event == "Gasto": self.show_add_movement_window(movement="Agregar Gasto")
            elif event == "Ingreso": self.show_add_movement_window(movement="Agregar Ingreso")
            elif event == "Exportar CSV":
                self.persistence.write_data(self.categorys, self.table_values)
                sg.popup("Datos exportados exitosamente a \"datos.csv\"", title="Exportación Exitosa")
            elif event == "Filtrar": self.filter_by_date(values["input_fecha_inicio"], values["input_fecha_fin"])
        self.window.close()

def main():
    try:
        account = FinancialManager()
        account.load_data()
        account.show_main_window()
    except Exception as ex:
        sg.popup_error(f"Se produjo un error inesperado durante la operación:\n {ex}", title="Error Inesperado")

if __name__ == "__main__":
    main()