# Question: https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

# Solution:
n=input()
A=set(input().split())
m=input()
B=set(input().split())
result=A | B
print(len(result))

