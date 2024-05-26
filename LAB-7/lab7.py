# Single Inheritance
class Fruit:
    def eat(self):
        print("Eating a fruit...")

class Apple(Fruit):
    def eat(self):
        print("Eating an apple.")

fruit = Fruit()
fruit.eat()

apple = Apple()
apple.eat()

# Multiple Inheritance
class Taste:
    def taste(self):
        print("This fruit has a unique taste.")

class Color:
    def color(self):
        print("This fruit has a vibrant color.")

class Mango(Taste, Color):
    def eat(self):
        print("Eating a mango.")

mango = Mango()
mango.eat()
mango.taste()
mango.color()

# Multilevel Inheritance
class Fruit:
    def eat(self):
        print("Eating a fruit...")

class Citrus(Fruit):
    def eat(self):
        print("Eating a citrus fruit.")

class Orange(Citrus):
    def eat(self):
        print("Eating an orange.")

fruit = Fruit()
fruit.eat()

citrus = Citrus()
citrus.eat()

orange = Orange()
orange.eat()

# Hierarchical Inheritance
class Fruit:
    def eat(self):
        print("Eating a fruit...")

class Strawberry(Fruit):
    def eat(self):
        print("Eating a strawberry.")

class Blueberry(Fruit):
    def eat(self):
        print("Eating a blueberry.")
class Mulberry(Fruit):
    def eat(self):
        print("Eating a mulberry")
strawberry = Strawberry()
strawberry.eat()

blueberry = Blueberry()
blueberry.eat()

mulberry = Mulberry()
mulberry.eat()

# Hybrid Inheritance
class Shape(Fruit):
    def describe_shape(self):
        print("This fruit has a particular shape.")

class Tropical(Fruit):
    def eat(self):
        print("Eating a tropical fruit.")

class Pineapple(Tropical, Shape):
    def eat(self):
        print("Eating a pineapple.")

pineapple = Pineapple()
pineapple.eat()
pineapple.describe_shape()