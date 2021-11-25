#1ое задание
n=int(input("Сколько зверьков рисуем от одного до девяти?" ))
cat=[' ^---^',
      '( o o )',
      ' ! = !/)']


for i in cat:
    print((i+" ") * n)



print()
print()
 #2ое задание
n = int(input("Введите число: "))
i = 1
x = 1
while n != x:
    for i in range(1, n + 1):
        if n > x:
            x = i ** 2
            i = i + 1
            print(x)
        elif n <= x:
            break

print()
print()
print()
#3ье задание
from random import*
max=1
min=5
k=randint(2,31)
print("В классе учеников:")
print(k)
print("Оценки учеников:")
for i in range(1,k):
    i=randint(1,5)
    if i>max:
        max=i
    if i<min:
        min=i
    print(i)
print("Максимальный результат",max)

print("Минимальный результат",min)



print()
print()
print()

#4ое задание
for i in range(1, 9):
    print("микробов",2 ** i)

print()
print()
#5ое задание
k=int(input("Сколько котлет у Губки боба? "))

m=int(input("Сколько помещается на сковородку? "))

fullpan=k//m
print("Пожариться полных сковородок:",fullpan)
another=k%m
print("Останеться пожврить:",another)