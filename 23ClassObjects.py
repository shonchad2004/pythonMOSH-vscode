#    A.     CLASSES
'''
1. New type ke objects create krne ke liye we use classes.
   A class is just a blueprint/template for creating objects.
2. It contains Attributes() and Methods(functions).
3. SYNTAX =  class class_name:     
4. First letter of class name must be CAPITAL.

'''

#   B.     OBJECTS
'''
1.  Objects are the instances of classes(based on the blueprint)
2.  To create an object =  type the name of the class & call it like a function using()
    SYNTAX =  Class_name()

3.  Using dot operator on objects(or the variable in which object is stored),
    we can access the methods in that class.
'''



'''
1.  Imagine a class as a blueprint or a recipe. It’s like saying, “Here’s how to make a car.” 
    It doesn’t create a car itself; it just tells you what a car should have (like wheels and a color) and what it can do (like drive or stop).

2.  An object is the actual car you make using the blueprint. 
    You can make many cars (objects) from the same recipe (class), and each car can have different properties (like color or speed).
'''
class Car:                       # Blueprint
    color = "Red"             # Attribute (property of the car)

    def drive(self):                    # Method (what the car can do)
        print("The car is driving")

# Creating an object
my_car = Car()           # Object of the Car class
print(my_car.color)      # Accessing the color attribute
my_car.drive()           # Calling the drive method



class Point:
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point1 = Point()     # syntax of object
point1.x = 10                               # attribute of point1 object only
point1.y = 40
point1.draw()        # calling a method