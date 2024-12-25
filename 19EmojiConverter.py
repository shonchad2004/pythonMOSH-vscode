message = input(">")
words = message.split(' ')   # it gives a list ->  ['x' , 'y' , 'z' ]
emojis = {
 ":)" : '😊',
 ":(" : '😔'
}

output = ''
for i in words :
    output += emojis.get(i,i) + ' '
print(output)

#    .split()  function :
'''
1. The split() method in Python is used to divide a string into a list of substrings based on a specified delimiter. 
2. If no delimiter is specified, it splits the string based on whitespace (spaces, tabs, or newlines) by default.

SYNTAX = string.split(separator=None, maxsplit=-1)

3. Operates only on strings.
4. Returns a list containing the split parts of the string.
'''