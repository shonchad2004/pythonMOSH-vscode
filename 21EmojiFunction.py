# Never include these parts in the function =  taking of the input from user
#                                           =  printing output

def emoji_func(message):
    words = message.split(' ')   # it gives a list ->  ['x' , 'y' , 'z' ]
    emojis = {
        ":)" : '😊',
        ":(" : '😔'
    }

    output = ''
    for i in words :
         output += emojis.get(i,i) + ' '
    return output

# 
sentence = input(">")
print(emoji_func(sentence))