# Write a simple class Person with attributes name and age,
# and a method to print the person's details.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def person_del(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")

person1 = Person('rojan', 22)

person1.person_del()