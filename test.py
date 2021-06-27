# Напишите программу, которая определяет наименьшее из четырёх чисел.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

ab = 0
cd = 0

if a < b:
    ab = ab + a
else:
    ab = ab + b
if c < d:
    cd = cd + c
else:
    cd = cd + d
if ab < cd:
    print(ab)
else:
    print(cd)