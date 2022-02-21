# Question: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

# solution:
if __name__ == '__main__':
   n=int(input())
   sam=[]
arr=list(map(int, input().split()))
great_num=max(arr)
for i in arr:
 if great_num != i:
   sam.append(i)
   
print(max(sam))