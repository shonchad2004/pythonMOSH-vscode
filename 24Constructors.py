#      A.     ATTRIBUTES
'''
Attributes can either belong to the class itself or to individual instances (objects).

1.  Instance Attributes
        Belong to individual objects.
        Unique to each object.
        Defined inside the __init__ method or directly through the object.

2.   Class Attributes
        Shared by all objects of the class.
        Defined outside the __init__ method.
        Useful for properties that are the same for every object.
'''

#     B.   CONSTRUCTOR   =    __init__(self, attritube1, attr2)
'''
1.  Without a constructor, you’d need to manually set attributes after creating an object, 
    which can be tedious. A constructor makes sure that every object is properly initialized as soon as it's created.

2.  Constructor is a special method used to initialize the 
    attributes of an object when it is created.

'''



class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, breed, color):
        self.breed = breed  # Instance attribute
        self.color = color  # Instance attribute

dog1 = Dog("Labrador", "Black")
dog2 = Dog("Poodle", "White")

print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris