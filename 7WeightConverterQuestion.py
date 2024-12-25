# Q. ask for eight . if in kgs, convert to pounds, or vice versa

weight = int( input("What's your weight?"))
choice = input("Is it in lbs or kg? Type l or k.")

if choice=='l' or choice=='L':
    kg_weight = 0.453592 * (weight)
    print(f'Weight in kgs = {kg_weight} kg.')

else: 
    lbs_weight = 2.20462 * (weight)
    print(f'Weight in pounds = {lbs_weight} lbs.')


#   2ND ANSWER - in place of using " l or L". use upper()

weight = int( input("weight : "))
unit = input("Is it in lbs or kg? Type l or k.")

if unit.upper()=='L':
    kg_weight = 0.453592 * (weight)
    print(f'Weight in kgs = {kg_weight} kg.')

else: 
    lbs_weight = 2.20462 * (weight)
    print(f'Weight in pounds = {lbs_weight} lbs.')
