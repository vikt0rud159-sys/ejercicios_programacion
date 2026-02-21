my_str = "I love Nación Sushi"


def count_uppercase_and_lowercase(my_str):
    count_upper = 0
    count_lower = 0
    for char in my_str:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    print(f"There’s {count_upper} upper cases and {count_lower} lower cases")
    return count_upper, count_lower

count_uppercase_and_lowercase(my_str)