"""
Exercise 7: Animal Inheritance

Create an inheritance hierarchy:

Base class `Animal`:
- Attributes: name, age, species
- Methods: eat(), sleep(), make_sound() (prints generic sound)

Child classes:
- Dog(Animal) - override make_sound() to bark
- Cat(Animal) - override make_sound() to meow
- Bird(Animal) - add fly() method, override make_sound() to chirp

Create a list of different animals and call make_sound() on each.
"""

# TODO: Write your Animal, Dog, Cat, and Bird classes here
class Animal: 
    def __init__(self, name, age, species): 
        self._name = name
        self._age = age
        self._species = species
    def eat(self):
        print(f"{self._name} is eating.")
    def sleep(self):
        print(f"{self._name} is sleeping.")
    def make_sound(self):
        print(f"{self._name} makes a generic sound.")      
class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Dog")
    def make_sound(self):
        print(f"{self._name} barks: Woof Woof!")
class Cat(Animal):  
    def __init__(self, name, age):
        super().__init__(name, age, "Cat")
    def make_sound(self):
        print(f"{self._name} meows: Meow Meow!")
class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age, "Bird")
    def make_sound(self):
        print(f"{self._name} chirps: Chirp Chirp!")
    def fly(self):
        print(f"{self._name} is flying.")

# Test code (uncomment when ready)
animals = [
    Dog("Buddy", 3),
    Cat("Whiskers", 2),
    Bird("Tweety", 1)
]

for animal in animals:
    animal.eat()
    animal.make_sound()
