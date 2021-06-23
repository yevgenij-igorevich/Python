# Cycles for, while.
name = "Hello, world!"

for a in name:
    print(a)

for b in range(1, 11):
    print(name)

i = 1
while i <= 10:
    print(i)
    i += 1

a = 1
while a <= 10:
    print(a)
    a += 1
    break

b = 1
while b <= 10:
    if b != 5:
        print(b)
    b += 1
    continue