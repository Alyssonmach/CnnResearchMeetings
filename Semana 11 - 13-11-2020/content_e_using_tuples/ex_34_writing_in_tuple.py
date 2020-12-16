import sys
sys.path.append('../implementations/')

from implementations.dimensions import dimensions

for dimension in dimensions:
    print(dimension)

dimensions = (400, 30)

print(dimensions)