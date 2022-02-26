# Question: https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

# Solution:
n=int(input())
result =  set()
for _ in range(n):
    result.add(input())
print(len(result))
