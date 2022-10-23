if count == 1:
    r = int(input_string)
    if r <= 0 :
        print('Такий круг не може існувати')
    else:
        p = 2 * 3,14 * r
        s = 3, 14 * r ** 2
        print(f'Circle: r = {r}; perimeter = {p}; square = {s}')

elif count == 2:
    a, b = values
    a1 = int(a)
    b1 = int(b)
    if a1 <= 0 or b1 <= 0:
        print('Такий прямокутник не може існувати')
    else:
        p = (a1 + b1) * 2
        s = a1 * b1
        print(f'Rectangle: a = {a1}, b = {b1}}; perimeter = {p}; square = {s}')
elif count == 3:
    a, b, c = values
    a1 = int(a)
    b1 = int(b)
    c1 = int(c)
    if a1 <= 0 or b1 <= 0 or c1 <= 0:
        print('Такий трикутник не може існувати')
    else:
        p = a1 + b1 + c1
        s = a1 * b1 * 0,5
        print(f'Triangle: a = {a1}, b = {b1}, c = {c1}; perimeter = {p}; square = {s}')
