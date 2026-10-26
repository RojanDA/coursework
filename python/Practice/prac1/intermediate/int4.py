# Create a base class Animal with a method speak.
# Create a derived class Dog that overrides the speak method
#  to print "Woof".


class animal:
    def speak(self):
        print("lailailai")

class Dog(animal):
    def speak(self):
        print("wolf")

dog = Dog()

dog.speak()
    