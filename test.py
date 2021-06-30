x = int(input(''))
y = int(input(''))
a = input('')

if a == '+':
    print(x + y)
elif a == '-':
    print(x - y)
elif a == '*':
    print(x * y)
elif a == '/':
    if y != 0:
        print(x / y)
    else:
        print('На ноль делить нельзя!')
elif a != '*' and a != '/' and a != '+' and a != '-':
    print('Неверная операция')