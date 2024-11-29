import random


def get_the_field(size_of_the_field, number_of_bombs):
    board = []
    for i in range(size_of_the_field):
        row = []
        for y in range(size_of_the_field):
            row.append("e")
        board.append(row)

    for i in range(number_of_bombs):
        y = random.randint(0, size_of_the_field - 1)
        x = random.randint(0, size_of_the_field - 1)

        while board[x][y] != "e":
            y = random.randint(0, size_of_the_field - 1)
            x = random.randint(0, size_of_the_field - 1)
        board[x][y] = "b"
    for i in range(size_of_the_field):
        for j in range(size_of_the_field):
            if board[i][j] != "b":
                board = number_place(board, i, j, size_of_the_field)

    return board


def display_the_board(board2):
    for i in range(len(board2)):
        print(*board2[i])


def check_range(row, column, size_of_the_field):
    start_row = 0
    start_column = 0
    if row != 0:
        start_row = row - 1
    if row + 1 < size_of_the_field:
        end_row = row + 1
    else:
        end_row = row
    if column != 0:
        start_column = column - 1
    if column + 1 < size_of_the_field:
        EndColumn = column + 1
    else:
        EndColumn = column
    return start_row, start_column, end_row, EndColumn


def number_place(board, row, column, size_of_the_field):
    counter_of_bombs = 0
    StartRow, StartColumn, EndRow, EndColumn = check_range(row, column, size_of_the_field)
    for i in range(StartRow, EndRow + 1):
        for j in range(StartColumn, EndColumn + 1):
            if board[i][j] == "b":
                counter_of_bombs += 1

    if board[row][column] == "e" and board[row][column] != "b":
        board[row][column] = counter_of_bombs
    return board


def get_field2(size_of_the_field):
    field2 = []
    for i in range(size_of_the_field):
        row = []
        for j in range(size_of_the_field):
            row.append("-")
        field2.append(row)
    return field2


def zeros(board, board2, row, column, size_of_the_field):
    StartRow, StartColumn, EndRow, EndColumn = check_range(row, column, size_of_the_field)
    board2[row][column] = board[row][column]
    if board[row][column] == 0:
        for x in range(StartRow, EndRow + 1):
            for y in range(StartColumn, EndColumn + 1):
                if board2[x][y] == "-":
                    board2 = zeros(board, board2, x, y, size_of_the_field)
    return board2


def get_coordinate(start, coordinate, size_of_the_board, size_of_the_cube):
    counter = - 1
    for i in range(start, size_of_the_board, size_of_the_cube+1):
        if i > coordinate > i - size_of_the_cube:
            return counter
        counter += 1

def define_coordinate(start_x,start_y, x, y, size_of_the_field, size_of_the_cube, change_board, board, size_of_the_board):
    list_number = get_coordinate(start_y, y, size_of_the_field, size_of_the_cube)
    item_number= get_coordinate(start_x, x, size_of_the_field, size_of_the_cube)

    change_board[list_number][item_number] = zeros(board, change_board, list_number, item_number, size_of_the_board)
    return change_board

sizeof_the_field = 9

print(get_field2(9))
print(get_the_field(9, 10))