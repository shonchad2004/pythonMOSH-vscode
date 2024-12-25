t = int (input('numbers in list? '))
listt = []
for i in range(t):
    numb = input('>')
    listt.append(numb)

print(listt)
    

def max_num(num):
    maximum = num[0]
    for i in num:
        if i > maximum :
            maximum = i
    return (maximum)


print(max_num(listt))