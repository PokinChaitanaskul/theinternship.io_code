import sys


def is_prime(input_number):
    if input_number > 1:
        for i in range(2, (input_number // 2) + 1):
            if input_number % i == 0:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    input_number = float(input())

    if input_number < 1 or input_number > 10:
        sys.exit()

    FIRST_DECIMAL_INDEX = 2
    input_string = str(input_number)
    current_number_to_check = input_string[0]
    current_decimal_index = FIRST_DECIMAL_INDEX
    decimal_places_to_check = 3
    is_floating_prime = "FALSE"
    decimal_places = len(input_string[2:len(input_string)])

    if decimal_places > 12:
        sys.exit()

    if decimal_places < 3:
        decimal_places_to_check = decimal_places

    for i in range(decimal_places_to_check):
        current_number_to_check += input_string[current_decimal_index]
        number = int(current_number_to_check)

        if is_prime(number):
            is_floating_prime = "TRUE"
            break

        current_decimal_index += 1


    print(is_floating_prime)
