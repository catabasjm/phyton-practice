class Organism:
    alive = True
class Animal(Organism):

    def eat(self):
        print('is eating')
    def sleep(self):
        print('is sleeping')

class Rabbit(Animal):
    def run(self):
        print('this rabbit is running')
class Cat(Animal):
    def meow(self):
        print('this cat is meowinggg')
class Dog(Animal):
    def bark(self):
        print('this dog is barking')

rabbit = Rabbit()
cat = Cat()
dog = Dog()

rabbit.sleep()
print(rabbit.alive)
dog.eat()
rabbit.run()
dog.bark()
print(dog.alive)
