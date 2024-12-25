#               IF   ,  ELIF  ,   ELSE

'''
1.  IF  =   if condition - True, it runs a specific block of code. If condition - False, the program skips this code and moves to next condition
        =   when using multiple independent if statements (not elif), each if statement is evaluated separately. This means each if statement is checked, regardless of whether previous if statements were true or false.

2.  ELIF  =  It checks another condition if the previous if (or elif) condition is False.
          =  The first elif statement that is True will execute its code, and Python will skip any subsequent conditions.

3.  ELSE  =  provides a default action when none of the previous conditions are True.
          =  else doesn’t require a condition, as it will only execute if all previous conditions are False.

Short-Circuiting  =  Once Python finds a True condition, it stops evaluating any additional elif or else statements. This is known as short-circuiting and helps optimize code execution.
'''
price = 1000000
good_credit = False
if good_credit:
    x = 10/100*int(price)
else:
    x = 20/100*int(price)
print(f'Buyer needs to put down ${x}')


temperature = 25
if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's a nice day.")
elif temperature > 10:
    print("It's a bit cool.")