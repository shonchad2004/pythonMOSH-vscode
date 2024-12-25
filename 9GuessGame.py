# Q.  There is a secret no. set already, u have 3 chances to find it.

secret_No = 5
i=1
while i<=3:
    guess = int(input('Guess: '))
    i+=1
    if guess==secret_No: 
        print('You Won!!')
        break
    
else: print('You Lost.')  
# WHILE statement can also have " ELSE " part

# If the user completes the while loop, it prints the else part next . 
# but in case it follows the IF statement the code will break out of while as well as else part.