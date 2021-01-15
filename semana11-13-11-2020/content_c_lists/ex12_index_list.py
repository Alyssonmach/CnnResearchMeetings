import sys
sys.path.append('../implementations/')

from implementations.bicycles import bicycles

print(bicycles)
print('{}, {}, {}'.format(bicycles[0].capitalize(), bicycles[1].capitalize(), 
                          bicycles[2].capitalize(), bicycles[3].capitalize()))

print(bicycles[0:4])

# las element
print(bicycles[-1])