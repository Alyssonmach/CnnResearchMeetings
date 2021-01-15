import sys
sys.path.append('../implementations/')


from implementations.motorcycles import motorcycles

print(motorcycles)

motorcycles[0] = 'ducati'

print(motorcycles)