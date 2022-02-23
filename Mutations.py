# Question: https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

# Solution:
def mutate_string(string, pos, char):
    return (string[:pos] + char + string[pos+1:])