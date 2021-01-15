number1 = 12
number2 = 12.0
number3 = 5 + 4j

print(type(number1))
print(type(number2))
print(type(number3))

number4 = 7 + 3.5j

print('Numerical Operation: {} + {} = {}'.format(number1, number2, (number1 + number2)))
print('Complex Operation: {} + {} = {}'.format(number3, number4, (number3 + number4)))