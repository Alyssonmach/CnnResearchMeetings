import sys
sys.path.append('../implementations/')

from implementations.cars import cars

print(cars)
print('\n')
print(sorted(cars)) # sorting temporaly
print(cars)
print('\n')
print(sorted(cars, reverse=True)) # sorting temporaly
print(cars)