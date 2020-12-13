def parse_input():
    with open('input') as file:
        numbers = [int(number.strip()) for number in file.readlines()]
    return numbers

input = parse_input()

for number1 in input:
    for number2 in input:
        to_find = 2020 - number1 - number2
        if to_find in input:
            print(number1 * number2 * to_find)
            break
