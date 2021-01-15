import sys
sys.path.append('../implementations/')

from implementations.motorcycles import motorcycles

print(motorcycles)

del motorcycles[0], motorcycles[1]
print(motorcycles)

motorcycles = []
motorcycles.append('honda'.capitalize())
motorcycles.append('yamaha'.capitalize())
motorcycles.append('suzuki'.capitalize())
print(motorcycles)

# removing the las item in a list
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print('The first motorcycle I owned was a ' + motorcycles.pop(0) + '.')
print(motorcycles)

motorcycles = []
motorcycles.append('honda'.capitalize())
motorcycles.append('yamaha'.capitalize())
motorcycles.append('suzuki'.capitalize())
print(motorcycles)

# removing by value

motorcycles.remove('honda'.capitalize())
print(motorcycles)

small_motorcycle = 'Yamaha'
motorcycles.remove(small_motorcycle)
print(motorcycles)


