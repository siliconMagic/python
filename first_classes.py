class Parent:
    """docstring for Parent"""

    CLASS_CONSTANTS = ["a", "b", "c"]

    def __init__(self, eye_color, hair_color="brown"):
        self.eye_color = eye_color
        self.hair_color = hair_color

    def do_something(self):
        print("Do something, Parent")

    def something_else(self):
        print("Do something else, Parent")
        
class Child(Parent):
    """docstring for Child"""
    def __init__(self, number_of_toys, *args):
        Parent.__init__(self, *args)
        self.number_of_toys = number_of_toys

    def do_something(self):
        print("Do something, Child")

        
dad = Parent("green", "brown")
son = Child(5, "blue", "blonde")
mom = Parent("blue")
daughter = Child(3, "black")



print(dad.eye_color)
print(son.eye_color)
print(son.number_of_toys)
print(mom.hair_color)
print(daughter.hair_color)
son.do_something()
dad.do_something()
son.something_else()