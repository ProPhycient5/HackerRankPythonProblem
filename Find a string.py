# Question: https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

# Solution: 
def count_substring(string, sub_string):
    d= len(sub_string); occur=0
    for i in range(0, len(string)):
      if (string[i: d+i] == sub_string):
        occur+=1
    return occur

