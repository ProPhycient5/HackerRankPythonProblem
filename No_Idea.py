# Question: https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true

# Solution: 
n, m = input().split()
user = input().split()
A = set(input().split())
B = set(input().split())

print(len([num for num in user if num in A])-len([num for num in user if num in B]))


# or

# n, m = input().split()
# user = input().split()
# A = set(input().split())
# B = set(input().split())


# good=[num for num in user if num in A]
# bad=[num for num in user if num in B]
# print(len(good)-len(bad))