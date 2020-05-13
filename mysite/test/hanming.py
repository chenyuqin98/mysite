n = int(input())
list = []
list = input().split(' ')
rlt=0
for i in range(n):
    list[i] = bin(int(list[i]))
# print(list)

for i in range(n-1):
    first = list[i]
    second = list[i + 1]
    first = first.replace("b", '')
    second = second.replace("b", '')
    # print(first,second)
    count=0
    for j in range(1,min(len(first), len(second))+1):
        # print(min(len(first), len(second)))
        # print(first[-1])
        if first[-j] != second[-j]:
            count += 1
        # print(count)
    if count>rlt:
        rlt=count
print(rlt)
