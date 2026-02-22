list_of_keys = ["access_level", "age"]
employee = {"name": "John", "email": "john@ecorp.com", "access_level": 5, "age": 28}
employee.pop(list_of_keys[0])
employee.pop(list_of_keys[1])
print(employee)