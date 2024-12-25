#         COMPARISON OPERATORS

# Q. if temperature is greater than 30 - it;s a hot day. otherwise if less than 10 - it;s a cold day .
#    otherwise neither hot nor cold

temp = 30
if(temp > 30):
    print("It's a hot day")
elif(temp<10):
    print("It's a cold day.")
else:
    print("Neither hot nor cold.")

# Q. if name has less than 3 characters, 'name must be 3 characters long'. if more than 50," name can be maximum of 50 char."
#  otherwise name is perfect!

name = "shobhna"

if(len(name) <3 ):
    print('Name must be at least 3 char long. ')
elif(len(name)> 50):
    print('Name can have max 50 char.')
else:
    print("Name is perfect!")
