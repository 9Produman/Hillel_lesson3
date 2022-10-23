input_string = input()
values = input_string.split()
count = len(values)
if count == 1:
    r = int(input_string)
    if r <= 0 :
        print('Такий круг не може існувати')
    else:
        s = 3,14 * r ** 2
        p = 2 * 3,14 * r
        print(f'Circle: {r}; {s}; {p}')

elif count == 2:
    a, b = values
    a1 = int(a)
    b1 = int(b)
    if a1 <= 0 or b1 <= 0:
        print('Такий прямокутник не може існувати')
    else:
        s = a1 * b1
        p = (a1 + b1) * 2
        print(f'Rectangle: {a1} {b1}; {s}; {p}')
elif count == 3:
    a, b, c = values
    a1 = int(a)
    b1 = int(b)
    c1 = int(c)
    if a1 <= 0 or b1 <= 0 or c1 <= 0:
        print('Такий трикутник не може існувати')
    else:
        s = a1 * b1
        p = a1 + b1 + c1
        print(f'Triangle: {a1} {b1} {c1}; {s}; {p}')