# Question can be found here: https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

# Solution:
def is_leap(year):
    leap = False
    if (year%100==0):
        if (year%400==0):
            return True
        else:
            return False
    
    elif (year%4==0):
        return True
    
    
    return leap;