# Question can be found here:  https://www.hackerrank.com/challenges/py-if-else/problem

# Solution

n = int(input())


if n in range (1,101):

  if (n %2 == 0):
     if (n in range(2,6) or n>20):
       print('Not Weird')
     elif (n in range(6, 21)):
       print('Weird')
  else:
    print('Weird') 