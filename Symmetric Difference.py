# Question: https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

# Solution: 
a=int(input())
sam=set(map(int, input().split()))
b=int(input())
sam2=set(map(int, input().split()))
res=sam.difference(sam2)
res2=sam2.difference(sam)
result=res | res2

for item in sorted(result):
    print(item)
