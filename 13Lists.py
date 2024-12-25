#       A. LISTS = 
#  1.  Concatenation in lists 
l1= [2,3,4]
l2= [1]
print(l2+l1)   

#  2.   SLICING = list_name[start : stop : steps ]  = same for TUPLES
'''

Slicing Parameters(for reverse) = [ : : -1]
start = default (end of the sequence when step is negative).
stop = default (start of the sequence when step is negative).
step = -1 (move backward).

'''



#  Q.1)    Write a program to find the largest number in a list
num = [200,55,30,7,10,9,4]
last_index = len(num)-1
temp=num[0]
for i in range(last_index):
    
    if (temp > num[i+1]):
        max = temp
    else :
        max = num[i+1]
        temp = max
print(max)

       #  OR 

last_index = len(num)
temp=int()             # when no argument is passed in int(). its default value is ZERO 0.
for i in range(last_index):
    
    if (temp > num[i]):
        max = temp
    else :
        max = num[i]
        temp = max
print(max)

#   SOLUTION BY MOSH - 
maximum = num[0]
for i in num:
    if i > maximum :
        maximum = i
print (maximum)

    