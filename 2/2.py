import re
from collections import Counter

def parse_input():
    with open('input') as file:
        return file.readlines()

def is_password_valid(password_data):
    counts = Counter(password_data[3])
    range_min = password_data[0]
    range_max = password_data[1]
    character = password_data[2]
    return int(range_min) <= counts[character] <= int(range_max)

inputs = parse_input()
passwords_data = [re.findall(r'(\d+)-(\d+)\s(\w):\s(.*)', i) for i in inputs]

counter = 0
for password_data in passwords_data:
    if is_password_valid(password_data[0]):
        counter += 1

#a = Counter('abcdef')