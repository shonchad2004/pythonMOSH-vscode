#        A.    TUPLES  = parenthesis() to definr tuples
'''
Similar to lists = used to store a list of items / have index / 
Tuples are immutable = can't mutate/ change/ modify them.

ONLY =  count()  and  index()

Different operations related to tuples in Python:

1. Traversing
2. Concatenation
3. Nesting
4. Repetition
5. Slicing
6. Deleting
7. Finding the length
8. Multiple Data Types with tuples
9. Conversion of lists to tuples
10.Tuples in a Loop

'''
#  1.   SLICING 
t = (0 ,1, 2, 3)

print(t[1:])
print(t[::-1])   # slicing with negative no. = from end to start

# Tuple & Lists  allows multiple data type 
lis = ['string', True, 13]
tup = ('string2', True, 13)


#  2. CONVERTING a LIST to a TUPLE  =    by using the tuple() constructor and passing the list as its parameters.

a = [0, 1, 2]
t = tuple(a)

print(t)