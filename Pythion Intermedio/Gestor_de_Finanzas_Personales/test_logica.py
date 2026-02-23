from logica import ApplicationLogic


def test_get_category_color_from_dict():
    test_account = ApplicationLogic()
    test_account.categorys = [{"name": "Comida", "color": "#FF0000"}]
    color = test_account.get_category_color("Comida")
    assert color == "#FF0000"


def test_get_category_color_default():
    test_account = ApplicationLogic()
    test_account.categorys = []
    color = test_account.get_category_color("Inexistente")
    assert color == "#FFFFFF"


def test_get_category_color_without_color():
    test_account = ApplicationLogic()
    test_account.categorys = [{"name": "Comida"}]
    color = test_account.get_category_color("Comida")
    assert color == "#FFFFFF"


def test_calculate_totals_basic():
    test_account = ApplicationLogic()
    test_account.table_values = [
        ["2026-01-01", "Venta", "Trabajo", "₡1000", "Ingreso"],
        ["2026-01-02", "Compra", "Comida", "₡-400", "Gasto"],
    ]
    income, expenses, balance = test_account.calculate_totals()
    assert income == 1000.0
    assert expenses == 400.0
    assert balance == 600.0


def test_calculate_totals_only_expenses():
    test_account = ApplicationLogic()
    test_account.table_values = [
        ["2026-01-01", "Venta", "Trabajo", "₡-20000", "Gasto"],
        ["2026-01-02", "Compra", "Comida", "₡-400", "Gasto"],
    ]
    income, expenses, balance = test_account.calculate_totals()
    assert income == 0.0
    assert expenses == 20400.0
    assert balance == -20400.0


def test_calculate_totals_invalid_rows():
    test_account = ApplicationLogic()
    test_account.table_values = [
        ["2026-01-01", "Venta", "Trabajo", "₡1000", "Ingreso"],
        ["fila_invalida"],
        ["2026-01-02", "Compra", "Comida", "abc", "Gasto"],
    ]
    income, expenses, balance = test_account.calculate_totals()
    assert income == 1000.0
    assert expenses == 0.0
    assert balance == 1000.0


def test_calculate_totals_empty_table():
    test_account = ApplicationLogic()
    test_account.table_values = []
    income, expenses, balance = test_account.calculate_totals()
    assert income == 0
    assert expenses == 0
    assert balance == 0


def test_update_table_colors_no_window():
    test_account = ApplicationLogic()
    test_account.window = None
    test_account.update_table_colors()