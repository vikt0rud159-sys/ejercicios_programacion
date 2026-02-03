class Employee:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @property
    def name(self):
        return self._name

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        try:
            if value < 0:
                raise ValueError
            self._salary = value
        except ValueError:
            print("El salario no puede ser negativo\n")
            exit()

    def promote(self, percentage):
        self.salary *= (1 + percentage)


employee = Employee("Ana", 1000)
employee.promote(0.1)
print(employee.name, [employee.salary])
print()