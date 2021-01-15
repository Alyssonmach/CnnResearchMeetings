import json

filename = 'content_n_exceptions/json/numbers.json'
with open(filename, 'r') as f_obj:
    numbers = json.load(f_obj)

print(numbers)
print(type(numbers))