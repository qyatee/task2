while True:
    a = int(input("Введите переменную A\n"))
    b = int(input("Введите переменную B\n"))
    c = int(input("Введите переменную C\n"))
    D = b**2-4*a*c
    if D>0:
        x1=(-b+D**0.5)/2*a
        x2=(-b-D**0.5)/2*a
        print(x1, x2)
    elif D==0:
        x1=-b/2*a
        print(x1)
    else:
        print("Корней нет")