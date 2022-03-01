# Question:https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true

# Solution:

s=input()
lower=[];upper=[];odd=[];even=[]
for char in s:
  if char.isalpha():
     if char.islower():
        lower.append(char)
        lower.sort()
     elif char.isupper():
        upper.append(char)
        upper.sort()
  elif char.isdigit():
    if int(char)%2 == 1:
      odd.append(char)
      odd.sort()
    elif int(char)%2 ==0:
      even.append(char)
      even.sort()

word_1=''.join(lower)
word_2=''.join(upper)
word_3=''.join(odd)
word_4=''.join(even)


result=word_1+word_2+word_3+word_4
print(result)


