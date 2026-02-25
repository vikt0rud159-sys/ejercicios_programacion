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
                            sg.popup("Error:\nLa fecha no puede ser futura. Se usará la fecha actual.", title="error_fecha")
                        else:
                            sg.popup_error("Error:\nEl monto debe ser un número válido.", title="error_monto")
        movement_window.close()