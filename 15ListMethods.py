#  LIST METHODS = are the built-in functions that can be performed on lists
'''
append():  Adds an element to the end of the list.                   |  list_name.append(element)         
copy():    Returns a shallow copy of the list.                       |  list_name.copy()
clear():   Removes all elements from the list.                       |  list_name.clear()
count():   Returns the number of times a specified                   |  list_name.count(element)
           element appears in the list.                              |
extend():  Adds elements from another list to the                    |  list_name.extend(iterable)
           end of the current list.                                  |
index():   Returns the index of the first occurrence                 |  list_name.index(element)
           of a specified element.                                   |
insert():  Inserts an element at a specified position.               |  list_name.insert(index, element)
pop():     Removes and returns the element at the specified          |  list_name.pop(index)
           position (or the last element if no index is specified).  |
remove():  Removes the first occurrence of a specified element.      |  list_name.remove(element)
reverse(): Reverses the order of the elements in the list.           |  list_name.reverse()
sort():    Sorts the list in ascending order (by default).           |  list_name.sort(key=None, reverse=False)  for DESCENDING ORDER -> reverse= True
'''
# sort() alters the original list
list1=[3,2,5,6]
list2= list1.sort()
print(list1)         # output will not be the original list1

# Q.1)      WAP to remove the duplicates in a list

list3=[4,2,6,8,3,6,7,4,6,5,1,0 ]

for i in list3:
    count_no = list3.count(i)
    if(count_no>1):
        list3.remove(i)

print(list3)
        
#  Solution by MOSH
numbers=[2,2,4,6,5,6,1,3,1]
uniques=[]                   # define an empty list...iterate over 1st list...
for i in numbers:            # check if each item exists in the empty list...if it does not....the add it to the empty one.
    if (i not in uniques):
        uniques.append(i)
print(uniques)