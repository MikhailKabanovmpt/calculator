def main():
    try:
        n1 = int(input("Введи первое число: "))
    except ValueError as e:
        print("Ошибка: "+ str(e))
        main()
    try:
        n2 = int(input("Введи второе число: "))
    except ValueError as а:
        print("Ошибка: "+ str(а))
        main()
    print("Список действий: \n "
          "1.Сложение\n"
          "2.Вычитание\n"
          "3.Умножение\n"
          "4.Деление\n"
          "5.Целоисленное деление\n"
          "6.Остаток от деления\n"
          "7.Возведение в степень\n"
          "8.Равно\n"
          "9.Не равно\n"
          "10.Больше\n"
          "11.Меньше\n"
          "12.Больше или равно\n"
          "13.Меньше или равно\n"
          "14.Логическое И\n"
          "15.Логическое ИЛИ\n"
          "16.Логическое НЕ\n"
          "17.Побитовое И\n"
          "18.Побитовое ИЛИ\n"
          "19.Побитовое ИСКЛЮЧАЮЩЕЕ ИЛИ\n"
          "20.Побитовое НЕ\n"
          "21.Побитовый сдвиг влево\n"
          "22.Побитывый сдвиг вправо\n"
          "23.Принадлежность\n"
          "24.Не принадлежность\n"
          "25.Тождественно\n"
          "26.Не тождественно\n")
    deistv = int(input("Какое действие сделать: "))
    if deistv == 1:
        print(n1+n2)
        main()
    elif deistv == 2:
        print(n1-n2)
        main()
    elif deistv == 3:
        print(n1*n2)
        main()
    elif deistv == 4:
        try:
            print(n1/n2)
            main()
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            main()
    elif deistv == 5:
        try:
            print(n1//n2)
            main()
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            main()
    elif deistv == 6:
        try:
            print(n1%n2)
            main()
        except ZeroDivisionError:
            print("На ноль делить нельзя")
            main()
    elif deistv == 7:
        print(n1**n2)
        main()
    elif deistv == 8:
        if n1 == n2:
            print("Первое число равно второму")
            main()
        else:
            print("Первое число не равно второму")
            main()
    elif deistv == 9:
        if n1 != n2:
            print("Первое число не равно второму")
            main()
        else:
            print("Первое число равно второму")
            main()
    elif deistv == 10:
        if n1>n2:
            print("Первое число больше второго")
            main()
        else:
            print("Первое число меньше второго")
            main()
    elif deistv == 11:
        if n1<n2:
            print("Первое число меньше второго")
            main()
        else:
            print("Первое число больше второго")
            main()
    elif deistv == 12:
        if n1>=n2:
            print("Первое число больше или равно второму")
            main()
        else:
            print("Первое число меньше второго")
            main()
    elif deistv == 13:
        if n1<=n2:
            print("Первое число меньше или равно второму")
            main()
        else:
            print("Первое число больше второго")
            main()
    elif deistv == 14:
        print(n1 and n2)
        main()
    elif deistv == 15:
        print(n1 or n2)
        main()
    elif deistv == 16:
        print(not n1)
        print(not n2)
        main()
    elif deistv == 17:
        print(n1&n2)
        main()
    elif deistv == 18:
        print(n1|n2)
        main()
    elif deistv == 19:
        print(n1^n2)
        main()
    elif deistv == 20:
        print(~n1)
        print(~n2)
        main()
    elif deistv == 21:
        print(n1<<n2)
        main()
    elif deistv == 22:
        print(n1>>n2)
        main()
    elif deistv == 23:
        if n1 in n2:
            print("Первое число принадлежит второму")
            main()
        else:
            print("Первое число не принадлежит второму")
            main()
    elif deistv == 24:
        if n1 not in n2:
            print("Первое число не принадлежит второму")
            main()
        else:
            print("Первое число принадлежит второму")
            main()
    elif deistv == 25:
        if n1 is n2:
            print("Первое число тождественно второму")
            main()
        else:
            print("Первое число не тождественно второму")
            main()
    elif deistv == 26:
        if n1 is not n2:
            print("Первое число не тождественно второму")
            main()
        else:
            print("Первое число тождественно второму")
            main()
    else:
        print("Такого действия нет")
        main()

main()
