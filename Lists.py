# Question: https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

# Solution:
n=int(input()); pack={}; index=[]; arr=[]
for i in range(n):
  opera,*num= input().split()
  digit=list(map(int, num))
  pack[opera]=digit
  index.append(pack.get(opera))

  if (opera=='print'):
     print(arr)
  elif (opera=='insert'):
    arr.insert(index[i][0], index[i][1])
  elif (opera=='remove'):
    arr.remove(index[i][0])
  elif ( opera=='append'):
    arr.append(index[i][0])
  elif (opera=='sort'):
    arr.sort()
  elif(opera=='pop'):
    arr.pop()
  elif(opera=='reverse'):
    arr.reverse()
