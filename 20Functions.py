#     A.      FUNCTIONS =   SYNTAX  =  { def func_name(parameters : data type):  }
#                                      { statement                               }
#                                      { reurn expression                        }

def greet_user(first_name, last_name):          # It is compulsory to give value for the parameters vrna error will occur.
    print(f'Hi! {first_name} { last_name}.')
    print("Welcome aboard.")

print("Start")
greet_user("Shobhna", 'Dwivedi')
print("Finish")

#    B.       PARAMETERS vs ARGUMENTS
'''
1.  Parameters are variables defined in a function declaration. 
    This act as placeholders for the values (arguments) that will be passed to the function.

2.  Arguments are the actual values that you pass to the function when you call it. 
    These values replace the parameters defined in the function.

3. TYPES OF ARGUMNENTS =    Default argument
                            Keyword arguments (named arguments)
                            Positional arguments
                            Arbitrary arguments (variable-length arguments *args and **kwargs)
'''

#   1.      DEFAULT ARGUMENTS
'''

'''


#   2.      KEYWORD ARGUMENTS (named arguments)
'''

'''


#   3.      POSITIONAL ARGUMENTS
'''

'''


#   4.      ARBITRARY ARGUMENTS (variable-length arguments *args and **kwargs)
'''

'''


#    C.   RETURN FUNCTIONS   =  if we don't write a return statement,
#                               by default it gives { None }
def square(n):
    return n*n

print(square(5))


