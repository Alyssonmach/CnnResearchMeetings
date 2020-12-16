import sys
sys.path.append('implementations/')

from implementations.pizzaria import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')