pole = ["   0  1  2", "0| ", "1| ", "2| "]  # Переменная для вывода игрового поля
igra = []  # Хранит игровые данные (расположение крестиков и ноликов)


def check_end():
    #  Проверка победы (Дописать )
    i = 1
    i += 1


def game(fs):
    # Ход игры
    for i in range(1, 11):
        if i < 10:
            print(f"Ход номер " + str(i))
            print(f"Игрок за {fs[i%2]}, ваш ход, введите координаты через пробел (слева, сверху)")
            cords = input().split()
            cords = list(map(int, cords))
            if igra[cords[0]][cords[1]] == "-":
                igra[cords[0]][cords[1]] = fs[i % 2]
                view_game()
            else:
                print("Данная ячейка занята, выберите другую")
        else:
            print("Конец Игры - Победила дружба")


def view_game():
    # Функиця выводит игровое поле
    print(pole[0])
    for i in range(0, 3):
        vivid = pole[i+1]
        for j in range(0, 3):
            vivid += igra[i][j] + "  "
        print(vivid)


def new_game():
    # функция начала новой игры, очищает игровое поле и выводит его
    print("************* Новая Игра *************")
    igra.clear()
    for i in range(3):
        igra.append(["-", "-", "-"])
    view_game()
    print("Кто будет ходить первым, X или 0 ?")
    fs = input()
    if fs != "X" or fs != "x":
        fs = ["0", "X"]
    else:
        fs = ["X", "0"]
    game(fs)


new_game()

# Пример вывода
'''
print("   0  1  2")
print("0| o  x  x")
print("1| x  o  x")
print("2| x  x  o")
'''
