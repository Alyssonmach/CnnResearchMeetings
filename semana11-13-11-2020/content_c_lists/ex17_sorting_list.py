import sys
sys.path.append('../implementations/')

from implementations.cars import cars
print(cars)
cars.sort() # alphabetical order
print(cars)
cars.sort(reverse=True) # reverse alphabetical order
print(cars)