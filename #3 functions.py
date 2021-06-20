# functions
x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))

def sum(a, b):
    return print(a + b)

sum(x, y)

def sum_2(a, b):
    return 1 - a + b

print(sum_2(x, y))

z = 0
def sum_3(a, b):
    return 3 + a + b

z = sum_3(x, y)
print(z)