information = {}
names = []
ages = []
weights = []
 
for i in range (0, 2):
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    weight = float(input('How much do you weigh? '))
    names.append(name)
    ages.append(age)
    weights.append(weight)

information['names'] = names
information['ages'] = ages
information['weights'] = weights

print('\n')

for informations, results in information.items():
    print('{} = {}'.format(informations.capitalize(), results))


