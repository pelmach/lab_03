import random as rnd

n = int(input())
list = []
num = int(input("По возрастанию - 1, по убыванию - 2"))

for i in range(n):
    list.append(rnd.randint(1, 99))
print(list)

if num == 1:
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    print(list)
else:
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    list.reverse()
    print(list)

