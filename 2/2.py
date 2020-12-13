import re
from collections import Counter

def parse_input():
    with open('input') as file:
        return file.readlines()

def is_password_valid(password_data):
    index_1 = int(password_data[0]) - 1
    index_2 = int(password_data[1]) - 1
    character = password_data[2]
    password = password_data[3]
    return (password[index_1] == character) + (password[index_2]== character)

inputs = parse_input()
passwords_data = [re.findall(r'(\d+)-(\d+)\s(\w):\s(.*)', i) for i in inputs]

counter = 0
for password_data in passwords_data:
    if is_password_valid(password_data[0]) == 1:
        counter += 1
print(counter)

#a = Counter('abcdef')