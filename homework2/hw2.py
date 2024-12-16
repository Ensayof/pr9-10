while(True):
    x = str(input("Введите 0 для выхода из цикла или целую цифру. которую программа приплюсует к сумме: "))
    if x.isdigit() == False:
        print("Введено не число.")
        break
    if int(x) == 0:
        print("Вы вышли из цикла.")
        break
    else:
        y = str(input("Введите вторую цифру для суммы: "))
        if y.isdigit() == False:
            print("Введено не число.")
            break
        print("Сумма равна: ", int(x) + int(y))