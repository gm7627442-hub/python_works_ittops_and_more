CELL_EMPTY_FLOOR = "."
CELL_VOID = " "
CELL_WALL = "#"
CELL_PLAYER = "@"

X = CELL_VOID
W = CELL_WALL
_ = CELL_EMPTY_FLOOR

maze_cells = [
    [W,W,W,_,W,W,W,W,W,W,W,W,W,W,W,W,W],
    [W,_,_,_,W,_,_,_,_,_,_,_,_,_,_,_,W],
    [W,_,W,W,W,_,W,W,W,W,W,W,W,W,W,_,W],
    [W,_,W,_,W,_,W,_,_,_,_,W,_,_,_,_,W],
    [W,_,W,_,W,_,W,_,X,X,_,W,_,W,W,W,W],
    [W,_,W,_,W,_,W,_,X,X,_,W,_,_,_,_,W],
    [W,_,W,_,_,_,W,_,W,w,_,W,_,W,W,W,W],
    [W,_,W,_,W,_,W,_,W,_,_,W,_,_,_,_,W],
    [W,_,W,_,W,_,W,_,W,W,W,W,W,W,W,_,W],
    [W,_,_,_,W,_,W,_,_,_,_,_,_,_,_,_,W],
    [W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W,W],
]

del _
del X
del W
maze_height = len(maze_cells)
maze_widht =len(maze_cells[0])

player_y = 3
player_x = 9
Player_dy = 0
player_dx = 0

is_game_play = True

while is_game_play:
    print("\n" * 100)

    
    for y, cells_line in enumerate(maze_cells):
        for x, cells in enumerate(cells_line):
            if x == player_x and y == player_y:
                print(CELL_PLAYER, end=" ")
            else:   
                print(cells, end = " ")
        print()
    
    
    is_game_play = False