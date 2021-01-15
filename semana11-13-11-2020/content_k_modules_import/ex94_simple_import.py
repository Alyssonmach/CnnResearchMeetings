import sys
sys.path.append('implementations/')

import implementations.pizzaria as pizzaria

pizzaria.make_pizza(16, 'pepperoni')
pizzaria.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')