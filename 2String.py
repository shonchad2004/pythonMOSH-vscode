#    A.    WHEN TO USE WHICH QOUTES; SINGLE/DOUBLE/TRIPLE
 
# 1. When the sentence has an APOSTROPHE = use " "
course = "Python's course for beginners."
print(course)

# 2. When the sentence has "" in it = use ''
course2 = 'Python course for "beginners". '
print(course2)

# 3. To type large amount of text 
mail = ''' Hi there,
This is our first mail to you.

Thank You, '''
print(mail)


#    B.      INDEX No. FOR POSITION IN STRING

# 1.  string_name[4] = denotes character of 4th position in string
print(course[0])            # P=0 , y=1 , t=2 , space=8 , etc

# 2. [-1]  = negative means starting from end
print(course[-1])      # last element is dot(.)

# 3. [0:4]  = means 0 to 3rd one....excluding 4th
name= "Me name is Shobhna."
print(name[0:4])        # output = 'Me n' = 0123

# 4. [3:]  = when end not specified it means by default till end.
print(name[4:])         # output = ame is Shobhna.

# 5. [:5]  = when start not specified - by default from 0.
print(name[:5])          # output = 'Me na' = 012345

# 6. [:]  = when both start & end are not specified  =  by default from 0 till end
intro= name[:]
print(intro)       # here 'intro' is same as 'name'.

#
thanks= 'Thank you beyonce'
print(thanks[1:-1])


#     C.     CONCATENATION 
first = 'Shobhna'
last = 'Dwivedi'
message = first + ' [' + last + '] is my name. '
print(message)


#     D.     FORMATTED STRING = f'  {varibale} in rly bracket & normal text aise hi '
msg = f'Hamara naam h {first} {last}.'
print(msg)


#     E.   STRING METHODS =  COOL FUNCTIONS  = TO ACCESS THESE FUNCTION = use DOT OPERATOR = string_name.op_name
#                           in OOPs these functions are called methods

#  1.   len(string_name)  = counts the no. of characters in the string / itmes in list
#                         = can be used to enforce limit on how many char can be entered in input
#                         = not a method , it is a general purpose function as it is not strings specified only
name2 = 'Hamra naam hai xyz. '
print(len(name2))

#  2.   str_name.upper()  = to convert all characters in upper case  = does not change/modify the original string 
print(course.upper())

#  3.   str_name.find( ' char/word to find ' )  = to find some char in a large string 
#                                          = output is the index no. of the first occurence of that char 
#                                          = output = (-1)  if the char doesn't exist in the str
print(name2.find('a')) 

#  4.   str_name.replace( ' char to replace ' , ' new char ' )   = all those char get replaced 
print(course2.replace('e',"a"))

# 5. in = 'char' in str.name  = a boolean expression to check existence of char/words in a string
#                           = output is true/false when print func. is used
print('naam' in name2)
