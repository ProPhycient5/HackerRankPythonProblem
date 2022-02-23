# Question: https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

# Solution:
s=input()
a=0; n=0
for char in s:
  if char.isalpha()==True:
    a+=1
  if char.isdigit()==True:
    n+=1

if a>0 and n>0:
    print('True'); print('True'); print('True')
elif a>0 and n==0:
   print('True'); print('True'); print('False')
elif a==0 and n>0:
    print('True'); print('False'); print('True')
else:
    print('False'); print('False');print('False')
 

m=0
for char in s:
  if char.islower()==True:
    m+=1

if m>0:
  print('True')
else:
  print('False')

b=0
for char in s:
  if char.isupper()==True:
    b+=1
    
if b>0:
  print('True')
else:
  print('False')  
