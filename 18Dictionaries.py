#      A.     DICTIONARIES
'''
stores the value in key: value pairs.
KEYS = case sensitive, must be immutable(strings,numbers or tuples , not lists), must be unique
VALUES = can be any data type, can be same as other values
'''

#   1.  CREATING a dictionary = using { : and comma } or dict( = and comma) 

d1 = {1: "shobhna" , 2:"sidhhi", "relation": "sisters"}   # here, keys are = int, int & string
d2 = dict(a = "Geeks", b = "for", name = "Geeks")                
print(d1)                                                 
print(d2)      

'''
 In Python, when creating a dictionary using the dict() constructor with keyword arguments,
 the keys must be valid Python identifiers.
      An identifier is a name that: 
             # Cannot start with a number.
             # Cannot include special characters, such as -, @, etc.
             # Must be a valid variable name in Python.
'''

#   2.   Accessing a value = [] or .get()
'''
  1.   []        =   If the Key Exists:          Returns the value associated with the key.
                 =   If the Key Does Not Exist:  Raises a KeyError.

  2.   .get(key)  =  SYNTAX  =  dictionary.get(key, default_value)
                  =  If the Key Exists: Returns the value associated with the key.
                  =  If the Key Does Not Exist: Returns the default_value (or None if no default is provided) without raising an error.
'''      





# Q.1) convert the phone no. into words. E.g.,  Phone_no = 1234  :  one two three four
num_dict = {0:'zero',1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven',8:'eight', 9:'nine' }
phone_no = input("Phone no. = ")
word = ''
for digit in phone_no :
    d= int(digit)
    word = word + ' ' + num_dict[d]
print(word)
    