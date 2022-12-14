pole = ["   0  1  2", "0| ", "1| ", "2| "]  # Переменная для вывода игрового поля
igra = []  # Хранит игровые данные (расположение крестиков и ноликов)


def check_end():
    """ Проверка победы """
    winh = []  # проверяем горизонтали
    winv = []  # проверяем вертикали
    wind1 = []  # Проверяем победу по первой диагонали
    wind2 = []  # Проверяем победу по второй диагонали
    wind1.clear()
    wind2.clear()
    for i in range(3):
        winh.clear()
        winv.clear()
        wind1.append(igra[i][i])
        wind2.append(igra[2-i][0+i])
        for j in range(3):
            winh.append(igra[i][j])
            winv.append(igra[j][i])
        if (winv[0] == winv[1] == winv[2]) and (winv[0] != '-'):
            return winv[0]  # Победа по вертикали
        elif (winh[0] == winh[1] == winh[2]) and (winh[0] != '-'):
            return winh[0]  # Победа по горизонтали
    if (wind1[0] == wind1[1] == wind1[2]) and (wind1[0] != '-'):
        return wind1[0]  # Победа по перовой горизонтали
    elif (wind2[0] == wind2[1] == wind2[2]) and (wind2[0] != '-'):
        return wind2[0]  # Победа по второй горизонтали


def game(fs=['0', 'X']):
    """ Ход игры на вход принемает список очередностей ходов, по умолчанию первым ходит Х"""
    for i in range(1, 11):
        check = True
        if i < 10:
            print(f"*** Ход номер " + str(i) + " ***")
            while check:  # Проверка правильности ввода координат
                try:
                    print(f"Игрок за {fs[i % 2]}, ваш ход, введите координаты через пробел (слева, сверху)")
                    cords = input().split()
                    cords = list(map(int, cords))
                    if igra[cords[0]][cords[1]] == "-":
                        igra[cords[0]][cords[1]] = fs[i % 2]
                        check = False
                        view_game()
                    else:
                        print("\n\nДанная ячейка занята, выберите другую\n\n")
                except:
                    print("\n\nНеверный формат ввода\n\n")
        end = check_end()
        if end:
            print(" ***** Победил игрок за " + str(end) + " ***** ")
            return new_game()
    end = check_end()
    if end:
        print(" ***** Победил игрок за " + str(end) + " ***** ")
        return new_game()
    else:
        print(" ***** Победила дружба !!! ***** ")


def view_game():
    """Функиця выводит игровое поле"""
    print(pole[0])
    for i in range(0, 3):
        vivid = pole[i + 1]
        for j in range(0, 3):
            vivid += igra[i][j] + "  "
        print(vivid)


def new_game():
    """функция начала новой игры, очищает игровое поле и выводит его"""
    print("************* Новая Игра *************")
    igra.clear()
    for i in range(3):
        igra.append(["-", "-", "-"])
    view_game()
    print("Кто будет ходить первым, X или 0 ?")
    fs = str(input())
    if fs == '0' or fs == 'o':
        fs = ['X', '0']
    else:
        fs = ['0', 'X']
    game(fs)


new_game()
