# ## Проименованные символы, что есть что на карте
CELL_EMPTY_FLOOR = "."
CELL_VOID = " "
CELL_WALL = "#"
CELL_PLAYER = "@"

# ## "Тело" лабиринта, карта местности
x = CELL_VOID # Эти переменные-всевдонимы для удобства рисования карты
W = CELL_WALL
_ = CELL_EMPTY_FLOOR
maze_cells = [
    [_,_,_,_,_,_,_,x,x,_,_,_,],
    [_,W,W,_,W,W,_,_,_,_,_,_,],
    [_,W,_,_,_,W,_,_,_,_,_,x,],
    [_,W,_,_,_,W,_,_,_,_,x,x,],
    [_,W,W,W,W,W,_,_,x,_,_,x,],
    [_,_,_,_,_,_,_,x,x,_,_,_,],
    [_,_,_,_,x,x,x,x,x,x,_,_,],
]
del _ # Эти переменные-всевдонимы больше не нужны, удаляем
del W
del x
maze_height = len(maze_cells)
maze_width = len(maze_cells[0])

# ## Переменные, описывающие игрока (игрового персонажа)
player_y = 2  # Положение по высоте
player_x = 3  # Положение по ширине
player_dy = 0  # Намерения о смещении по вертикали
player_dx = 0  # Намерения о смещении по горизонтали

# ## Технические переменные
is_game_play = True
is_player_action_correct = True 


# ## Основной цикл приложения
while is_game_play:
    #-- Отрисовка --#
    # "Очистка" экрана
    print("\n" * 100)

    # Отрисовка лабиринта
    for y, cells_line in enumerate(maze_cells):
        for x, cell in enumerate(cells_line):
            if x == player_x and y == player_y:
                print(CELL_PLAYER, end=" ")
            else:
                print(cell, end=" ")
        print()

if not is_player_action_correct:
    print('\n')
    print('Введены не те символы')   

    # Отрисовка текста меню и пояснений
    print(
        "\n"
        "a - шаг влево   w - шаг вверх\n"
        "d - шаг вправо  s - шаг вниз\n"
        "   0 - выход из программы\n"
        "\n"
        ">>> ",
        end=""
    )

    #-- Ввод --#
    player_action = input().strip()  # strip для удаления внешних пробельных символов

    #-- Основная логика --#
    # Очистка намерения двигаться, оставшегося с прошлой итерации
    player_dx = 0
    player_dy = 0
    
    
    is_player_action_correct = True

    # Разбор пользовательского ввода
    if player_action == "0":
        is_game_play = False
    elif player_action == "a":
        player_dx = -1
    elif player_action == "d":
        player_dx = 1
    elif player_action == "w":
        player_dy = -1
    elif player_action == "s":
        player_dy = 1
    else:
        is_player_action_correct = False

    # Обработка намерения двигаться.
    # Желаемое новое положение игрока
    player_new_x = player_x + player_dx
    player_new_y = player_y + player_dy 

    # Проверки на невозможность движения
    is_player_x_correct = 0 <= player_new_x < maze_width
    is_player_y_correct = 0 <= player_new_y < maze_height
    is_player_inside_maze = is_player_x_correct and is_player_y_correct

    # Проверка выхода за пределы
    if not is_player_inside_maze:
        player_new_x = player_x  # Сброс в исходную позицию
        player_new_y = player_y

    # Проверка преград на пути
    if maze_cells[player_new_y][player_new_x] != CELL_EMPTY_FLOOR:
        player_new_x = player_x  # Сброс в исходную позицию
        player_new_y = player_y

    # Осуществление перемещения
    player_x = player_new_x
    player_y = player_new_y
