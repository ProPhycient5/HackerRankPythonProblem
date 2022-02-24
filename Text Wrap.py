# Question: https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

# Solution: 
def wrap( string, max_width):
  if (len(string)% max_width == 0):
    d=len(string)//max_width
  else:
    d=(len(string)//max_width)+1
  i=0
  while (i < d):
    if i==d-1:
      return (string[max_width*i: max_width*i+max_width])
    print(string[max_width*i: max_width*i+max_width])
    i+=1


