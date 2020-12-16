import sys
sys.path.append('../implementations/')

from implementations.foods import foods

print('List of foods: {}'.format(foods))

my_foods = foods[:-2]
friend_foods = foods[0:2]

print('My food: {}'.format(my_foods))
print('My friend foods: {}'.format(friend_foods))