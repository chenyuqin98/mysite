import pandas as pd
m,n =input().split(' ')
m=int(m)
n=int(n)
scores=[]
scores = [[] for i in range(m)]
for i in range(m):
    line = input().split(' ')
    for j in range(n):
        scores[i].append(int(line[j]))
# print(scores)

new_scores = []
for i in range(len(scores[0])):
    scores1 = []
    for j in range(len(scores)):
        scores1.append(scores[j][i])
    new_scores.append(scores1)
print(new_scores)

max_index=[]
for i in range(n):
    max_index.append(int(new_scores[i].index(max(new_scores[i]))))
print(max_index)

stu = []
for index in max_index:
    if not index in stu:
        stu.append(index)
print(len(stu))


