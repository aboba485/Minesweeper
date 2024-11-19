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

    return board


def display_the_board(board):
    for row in board:
        for item in row:
            if item != "b":
                if item == item.upper():
                    print(item, end = " ")

                else:
                    print("-", end = " ")

            elif item == "b":
                print("-", end = " ")
        print()


def make_a_turn(board):
    x = int(input("Input the x coordinate: "))
    y = int(input("Input the x coordinate: "))

    if board[x][y] != "b":
        board[x][y] = "E"

    elif board[x][y] == "b":
        print("You lost")

    return board


field = get_the_field(9, 10)
#beginer: 9x9, 10; medium: 16, 40; hard: 22, 99

display_the_board(field)
field = make_a_turn(field)
display_the_board(field)