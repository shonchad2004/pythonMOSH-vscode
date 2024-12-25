# 1. CAR GAME OF COMMANDS.

command = ""

while (command.upper() != 'QUIT') :
    command = input("Command : " )
    if command.upper()=="HELP" :
        print("Start - to start the car.\nStop - to stop the car.\nQuit - to exit. \n")
    
    elif command.upper()=="START" :  
        print("Car started...Ready to go !!") 

    elif command.upper()=="STOP" :
        print("Car stoped.")
        
    else : 
        print("I don't understand that...")
    


#  2.  To avoid using .upper() multiple times....usko input lete time, input ke upar hi laga denge.
# So jab input lenge ...vo apne aap upper case me ho jayega.

command = ""

while (command != 'QUIT') :
    command = input("Command : " ).upper()   # INPUT().UPPER()
    if command =="HELP" :
        print("Start - to start the car.\nStop - to stop the car.\nQuit - to exit. \n")
    
    elif command=="START" :  
        print("Car started...Ready to go !!") 

    elif command=="STOP" :
        print("Car stoped.")
        
    else : 
        print("I don't understand that...")



#  3.  TO SKIP THE ELSE WALA PART TO BE PRINTED WHEN "QUIT" IS TYPED.
#     Add one more condition =     elif command=="QUIT" :  break      = means exit the loop immediately


command = ""

while (command != 'QUIT') :
    command = input("Command : " ).upper()   # INPUT().UPPER()
    if command =="HELP" :
        print("Start - to start the car.\nStop - to stop the car.\nQuit - to exit. \n")
    
    elif command=="START" :   
        print("Car started...Ready to go !!")
            
    
    elif command=="STOP" :
        print("Car stopped.")

    elif command=="QUIT" :
        break                    # Immediately exit the loop without executing the else block

    else : 
        print("I don't understand that...")



#  4.  TO REMOVE REPEATION OF "QUIT" at  -   while (command != 'QUIT') :
#                                     -   elif command=="QUIT" :  break
#    USE  " WHILE True : "

responses = {                                       # DICTIONARY - 
"HELP" :  '''Start - to start the car.              
Stop - to stop the car.
Quit - to exit.
''',
"START" : "Car started...Ready to go!!",
"STOP" : "Car stopped.",
}

while True :
    command = input("Command :").upper()
    
    if command == "QUIT":
        break

    print(responses.get(command, "I don't understand that..."))      # Show response or default
          


#      In Python, the .get() method is a built-in function of dictionaries that retrieves the value associated with a specified key. 
#      It’s like using square brackets ([]) to access a value, but with one key difference:
#      If the key does not exist:
#           - dict[key] raises a KeyError (an error that stops your program).
#           - dict.get(key) returns a default value (you can specify this).

#     SYNTAX of .get()  =     dictionary.get(key, default_value)




car_started = False
car_stopped = False
command = ""

while (command != 'QUIT') :
    command = input("Command : " ).upper()   # INPUT().UPPER()
    if command =="HELP" :
        print("Start - to start the car.\nStop - to stop the car.\nQuit - to exit. \n")
    
    elif command=="START" :   
        if car_started:
          print("Car started already")
        else :
            print("Car started...Ready to go !!")
            car_started= True
    
    elif command=="STOP" :
        if car_stopped:
            print("Car already stopped")
        else:
          print("Car stopped.")
          car_stopped = True

    elif command=="QUIT" :
        break                    # Immediately exit the loop without executing the else block

    else : 
        print("I don't understand that...")