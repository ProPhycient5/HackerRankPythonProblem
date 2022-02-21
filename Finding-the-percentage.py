# Question: https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true

# Solution:
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()


if (query_name in student_marks.keys()):
  sam= student_marks.get(query_name)

avg=sum(sam)/len(sam)
print("{:.2f}".format(avg))
