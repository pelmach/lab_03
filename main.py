import random as rnd

n = int(input())
list = []

for i in range(n):
    list.append(rnd.randint(1, 99))
print(list)

for i in range(n - 1):
    for j in range(n - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]

print(list)
