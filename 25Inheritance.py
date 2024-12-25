#        A.         INHERITANCE 
'''
1.  Inheritance allows a child class to inherit attributes and methods from another parent class.

'''  

#        B.        __init__    

#           SUPER(). FUNCTION  = TO USE __INIT__() IN CHILD CLASS
'''
super() function is used to call the parent class’s methods. 
In particular, it is commonly used in the child class’s __init__() method to initialize inherited attributes. 
This way, the child class can leverage the functionality of the parent class.
'''

class Person:
    def __init__(self, name,id):
        self.name=name
        self.id = id

    def person_details(self):
        print(self.name,self.id)
        

class Employee(Person):
    def __init__(self, name, id,salary,post):
        super().__init__(name, id)        #  attributes inherited from Person class

        self.salary = salary              #  Attributes defined for just the child class
        self.post = post
    def emp_details(self):
        print(self.name,self.id,self.salary,self.post)


e1 = Employee('Avni',105,20000,'accountant')
print (e1.emp_details())
    


    