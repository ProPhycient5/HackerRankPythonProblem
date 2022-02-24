# Question: https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true

# Solution: 
def average(array):
    my_set=set(array)
    value=sum(my_set)/len(my_set)
    return value

