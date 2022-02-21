# Question: https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

# Solution:
n=int(input())
var=[]; num=[]
for _ in range(n):
  name=input()
  var.append(name)
  score=float(input())
  num.append(score)

small=min(num); rep=0
var2=[]; num2=[]
for i in range(0,n):
  if (small != num[i]):
    rep+=1
    num2.append(num[i])
    var2.append(var[i])

small2= min(num2); result=[]

for j in range(rep):
  if (small2 == num2[j]):
    result.append(var2[j])

for item in sorted(result):
  print(item)

