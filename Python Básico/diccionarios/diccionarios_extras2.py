employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
employees_dep = {}
for employee in employees:
    department = employee["department"]
    if department in employees_dep:
        employees_dep[department].append(employee)
    else:
        employees_dep[department] = [employee]
for dep, info in employees_dep.items():
    print(f"{dep}: {info}")