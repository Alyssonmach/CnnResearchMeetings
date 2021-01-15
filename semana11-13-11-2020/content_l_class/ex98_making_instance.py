from ex97_dog_class import Dog

my_dog = Dog()
your_dog = Dog('Freddie', 8)

name = input('Enter first name of the dog: ')
age = input('Enter age of the dog: ')
age = int(age)

my_dog.__init__(name, age)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")



