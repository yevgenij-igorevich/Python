# Вариации отрезков
a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 < b1 and a2 < b2:
    if b1 < a2 or a1 > b2:  # Пустое множество
        print('пустое множество')
    elif b1 == a2:  # 1,5,5,10
        print(b1)
    elif a1 == b2:  # 5,10,1,5
        print(a1)
    elif a1 <= a2 < b1 < b2:
        print(a2, b1)
    elif a2 <= a1 < b2 < b1:
        print(a1, b2)
    elif a1 < a2 < b2 <= b1:
        print(a2, b2)
    else:
        if a2 < a1 < b1 <= b2:
            print(a1, b1)
        elif a1 == a2 and b1 == b2:
            print(a1, b1)