notes = input("Ingresar un número de notas: ")
if (notes == "0"):
    notes = 1
counter = 0
approved = 0
approved_total = 0
disapproved = 0
disapproved_total = 0
total = 0

while counter < int(notes):
    grade = int(input("Ingrese la nota: "))
    if grade >= 70:
        approved += 1
        total += grade
        approved_total += grade
    else:
        disapproved += 1
        total += grade
        disapproved_total += grade
    counter += 1
print("Aprobados:", approved)
print("Desaprobados:", disapproved)
if total == 0:
    print("Promedio de notas: 0")
else:
    print("Promedio de notas:", total / int(notes))
if approved == 0:
    print("Promedio de notas aprobadas: 0")
else:
    print("Promedio de notas aprobadas:", approved_total / approved)
if disapproved == 0:
    print("Promedio de notas desaprobadas: 0")
else:
    print("Promedio de notas desaprobadas:", disapproved_total / disapproved)