# Условные конструкции
# if - если. elif - или же если. else - вдругом же случае
# and - и, or - или, not - не.
a = int(input("Введите число: "))

if (a > 50):
    print(str(a) + " больше 50")
elif (a < 30):
    print(str(a) + " меньше чем 30")
else:
    print("Ошибка")