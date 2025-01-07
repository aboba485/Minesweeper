import random


def get_empty_field(size_of_the_field):
    board = []
    for i in range(size_of_the_field):
        row = []
        for y in range(size_of_the_field):
            row.append("e")
        board.append(row)
    return board


def get_the_field(board, size_of_the_field, number_of_bombs, start_x, start_y, x, y, size_of_the_cube, size_of_the_display):
    row = get_coordinate(start_y, y, size_of_the_display, size_of_the_cube)
    column = get_coordinate(start_x, x, size_of_the_display, size_of_the_cube)
    print(row, column)
    StartRow, StartColumn, EndRow, EndColumn = check_range(row, column, size_of_the_field)
    for i in range(StartRow, EndRow+1):
        for j in range(StartColumn, EndColumn+1):
            board[i][j] = "E"
    for i in range(number_of_bombs):
        Y = random.randint(0, size_of_the_field - 1)
        X = random.randint(0, size_of_the_field - 1)

        while board[X][Y] != "e":
            Y = random.randint(0, size_of_the_field - 1)
            X = random.randint(0, size_of_the_field - 1)
        board[X][Y] = "b"
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

    if (board[row][column] == "e" or board[row][column] == "E") and board[row][column] != "b":
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
    try:
        board2[row][column] = board[row][column]
        if board[row][column] == 0:
            for x in range(StartRow, EndRow + 1):
                for y in range(StartColumn, EndColumn + 1):
                    if board2[x][y] == "-":
                        board2 = zeros(board, board2, x, y, size_of_the_field)
        return board2
    except:
        pass


def get_coordinate(start, coordinate, size_of_the_board, size_of_the_cube):
    counter = -1
    for i in range(start, size_of_the_board, size_of_the_cube+1):
        if i > coordinate > i - size_of_the_cube:
            return counter
        counter += 1
    return counter


def define_coordinate(start_x, start_y, x, y, size_of_the_field, size_of_the_cube, change_board, board, size_of_the_board):
    list_number = get_coordinate(start_y, y, size_of_the_field, size_of_the_cube)
    item_number = get_coordinate(start_x, x, size_of_the_field, size_of_the_cube)
    change_board = zeros(board, change_board, list_number, item_number, size_of_the_board)

    return change_board


def place_flag(start_x, start_y, x, y, size_of_the_field_in_px, size_of_the_cube, change_board, number_of_bombs, size_of_the_field):
    list_number = get_coordinate(start_y, y, size_of_the_field_in_px, size_of_the_cube)
    item_number = get_coordinate(start_x, x, size_of_the_field_in_px, size_of_the_cube)

    if change_board[list_number][item_number] == "-" and number_of_bombs > count_flags(change_board, size_of_the_field):
        change_board[list_number][item_number] = ">"
    elif change_board[list_number][item_number] == ">":
        change_board[list_number][item_number] = "-"

    return change_board




def count_correct_flags(board, change_board, size_of_the_field):
    counter = 0
    for i in range(size_of_the_field):
        for j in range(size_of_the_field):
            if board[i][j] == "b" and change_board[i][j] == ">":
                counter += 1
    return counter


def count_flags(change_board, size_of_the_field):
    counter = 0
    for i in range(size_of_the_field):
        for j in range(size_of_the_field):
            if change_board[i][j] == ">":
                counter += 1
    return counter


# def get_check_win(chag)
