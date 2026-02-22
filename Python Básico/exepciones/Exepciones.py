def get_num():
    num = input("Ingrese un número: ")
    try:
        num = float(num)
    except ValueError:
        print(f"ValueError: Debe ingresar un número.\n")
        num = get_num()
    return num


def get_op():
    op_list = ["1.Suma", "2.Resta", "3.Multiplicación", "4.División", "5.Borrar resultado"]
    print (op_list)
    op = input("Operación: ")
    try:
        op = int(op)
    except ValueError:
        print(f"ValueError: Debe ingresar un valor de operación valido.\n")
        op = get_op()
    try:
        if op < 6:
            ""
        else:
            raise KeyError
    except KeyError:
        print(f"KeyError: Debe ingresar un valor de operación valido.\n")
        op = get_op()
    return op


def get_new_num():
    new_num = input("Ingrese un número: ")
    try:
        new_num = float(new_num)
    except ValueError:
        print(f"ValueError: Debe ingresar un número.\n")
        new_num = get_new_num()
    return new_num


def get_sum(num, new_num):
    num += new_num
    return num


def get_sub(num, new_num):
    num += -new_num
    return num


def get_mult(num, new_num):
    num = num * new_num
    return num


def get_div(num, new_num):
    count = 0
    try:
        num = num / new_num
        return num
    except ZeroDivisionError:
        num = 0
        return num


def calc():
    num = get_num()
    while True:
        op = get_op()
        new_num = get_new_num()
        if op == 1:
            get_sum(num, new_num)
            num = get_sum(num, new_num)
            print(f"{num}\n")
        elif op == 2:
            get_sub(num, new_num)
            num = get_sub(num, new_num)
            print(f"{num}\n")
        elif op == 3:
            get_mult(num, new_num)
            num = get_mult(num, new_num)
            print(f"{num}\n")
        elif op == 4:
            get_div(num, new_num)
            num = get_div(num, new_num)
            if num == 0:
                print("No se puede divir por 0")
            print(f"{num}\n")
        elif op == 5:
            num = new_num


calc()