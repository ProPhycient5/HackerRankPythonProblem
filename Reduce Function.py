# Question: https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true

# Solution: 

def product(fracs):
    def mul(ini, item):
      return ini*item 
    t = reduce( mul, fracs,1)
    return t.numerator, t.denominator