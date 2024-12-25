#             LOGICAL OPERATORS = AND , OR , NOT

'''
1.  AND  = returns True only if both conditions are True.
         = If any of the conditions is False, the result is False.

2.  OR  =  returns True if "at least one" condition is True.
        =  It only returns False if all conditions are False.

3.  NOT  = inverts the Boolean value of a condition.
         = TRUE ko FALSE   and   FALSE ko TRUE.
'''

# Q.1 = applicant should either have high income or good credit to be eligible for loan and shoukd not have any criminal record

high_income = True
good_credit = False
criminal = True 

if((high_income or good_credit) and not criminal):
    print("Eligible for loan.")
else:
    print("Not Eligible for loan.")
