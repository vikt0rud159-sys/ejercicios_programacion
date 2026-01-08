my_list = [1, 4, 6, 7, 13, 9, 67]


def get_prime_numbers():
    mod_list = [2, 3, 4, 5, 6, 7, 8, 9]
    prime_numbers = []
    for num in my_list:
        counter = 0
        for number in mod_list:
            if number == num:
                number += 1
            residue = num % number
            if residue == 0:
                counter = -20
            elif counter == 7:
                prime_numbers.append(num)
            elif num == 1:
                counter = -20
            counter += 1
    return print(prime_numbers)


get_prime_numbers()