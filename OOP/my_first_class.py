class Dog: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f'{self.name} is sitting.')
    
    def bark(self):
        print(f'{self.name} is barking')

my_dog = Dog('Milo',4)
my_dog2 = Dog('Enoki', 5)

print(f'{my_dog.name} is {my_dog.age} year old')
my_dog2.bark()
