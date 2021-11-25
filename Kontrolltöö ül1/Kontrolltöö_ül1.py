#1ое задание
n=int(input("Сколько зверьков рисуем от одного до девяти?" ))
osa1=print(" ^---^")
osa2=print("( o o )")
osa3=print("! = !/)")

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
