import random


def get_the_field(size_of_the_field, number_of_bombs):
    board = []
    for i in range(size_of_the_field):
        row = []
        for y in range(size_of_the_field):
            row.append("e")
        board.append(row)

    for i in range(number_of_bombs):
        y = random.randint(0,size_of_the_field - 1)
        x = random.randint(0,size_of_the_field - 1)

        while board[x][y] != "e":
            y = random.randint(0, size_of_the_field - 1)
            x = random.randint(0, size_of_the_field - 1)
        board[x][y] = "b"
    for i in range(size_of_the_field):
        for j in range(size_of_the_field):
            if board[i][j] != "b":
                board=NumberPlace(board, i, j)

    return board


def display_the_board(board2):
    for i in range(len(board2)):
        print(*board2[i])


def CheckRange(board, row, column):
    StartRow=0
    StartColumn=0
    if row!=0:
        StartRow=row-1
    if row+1<sizeof_the_field:
        EndRow=row+1
    else:
        EndRow=row
    if column!=0:
        StartColumn=column-1
    if column+1<sizeof_the_field:
        EndColumn=column+1
    else:
        EndColumn=column
    return StartRow, StartColumn, EndRow, EndColumn


def NumberPlace(board, row, column):
    counter_of_bombs=0
    StartRow, StartColumn, EndRow, EndColumn = CheckRange(board, row, column)
    for i in range(StartRow, EndRow+1):
            for j in range(StartColumn, EndColumn+1):
                if board[i][j]=="b":
                        counter_of_bombs+=1

    if board[row][column]=="e" and board[row][column]!="b":
        board[row][column]=counter_of_bombs
    return board

def get_Field2():
    field2 = []
    for i in range(sizeof_the_field):
         row=[]
         for j in range(sizeof_the_field):
             row.append("-")
         field2.append(row)
    return field2


def Zeros(board, board2, row, column):
    StartRow, StartColumn, EndRow, EndColumn = CheckRange(board, row, column)
    board2[row][column]=board[row][column]
    if board[row][column]==0:
        for x in range(StartRow, EndRow):
            for y in range(StartColumn, EndColumn):
                if board2[x][y]=="-":
                    board2=Zeros(board, board2, x, y)
    return board2

def make_a_turn(board, board2):
    column = int(input("Input the x coordinate: "))
    row = int(input("Input the y coordinate: "))

    if board[row][column] != "b":
        board2 = Zeros(board, board2, row, column)

    elif board[row][column] == "b":
        print("You lost")
        return False

    return board2

sizeof_the_field = 16
#
# field = get_the_field(22, 99)
#field2 = get_field2()
# win=True
# while  make_a_turn(field, field2):
#     display_the_board(field2)
