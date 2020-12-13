def parse_input():
    with open('input') as file:
        numbers = [int(number.strip()) for number in file.readlines()]
    return numbers

input = parse_input()

for number in input:
    to_find = 2020 - number
    if to_find in input:
        print(number * to_find)
        break
