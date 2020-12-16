import sys
sys.path.append('../implementations/')

from implementations.bicycles import bicycles

print('My first bicycle was a {}.'.format(bicycles[3].capitalize()))