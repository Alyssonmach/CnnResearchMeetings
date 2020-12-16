import sys
sys.path.append('../implementations/')

from implementations.motorcycles import motorcycles

print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda'.capitalize())
motorcycles.append('yamaha'.capitalize())
motorcycles.append('suzuki'.capitalize())
print(motorcycles)