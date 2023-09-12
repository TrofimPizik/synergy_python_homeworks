# Задание №1
amount = int(input("Введите количество элементов списка "))
data = list(map(int, input().split()))[:amount]
data_set = set(data)

print(len(data_set))


# Задание №2
a=set(input().split())
b=set(input().split())

print (len(a.intersection(b)))


# Задание №3
a=set()

for i in input().split():
    if i not in a:
        a.add(i)
        print('NO')
else:
    print('YES')