x = int(input(''))

if x >= 0 and x <= 36:
    if x == 0:
        print('зеленый')
    elif x > 0 and x <= 10:
        if x % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif x > 10 and x <= 18:
        if x % 2 == 0:
            print('красный')
        else:
            print('черный')
    elif x > 18 and x <= 28:
        if x % 2 == 0:
            print('черный')
        else:
            print('красный')
    elif x > 28 and x <= 36:
        if x % 2 == 0:
            print('красный')
        else:
            print('черный')
else:
    print('ошибка ввода')