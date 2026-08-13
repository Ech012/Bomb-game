import random


import consts

def create():
    matricx_game = [[consts.EMPTY_BLOCK for j in range(50)] for i in range(25)]
    for row in range(22, 25):
        for col in range(46, 50):
            matricx_game[row][col] = consts.FLAG

    return matricx_game


def put_bombs(matricx_game):
    count = 0
    for i in range(25):
        for j in range(50 - 3):
            rnd_place_row = random.randint(0, 24)
            rnd_place_col = random.randint(0, 50 - 3)
            if matricx_game[rnd_place_row][rnd_place_col] == consts.EMPTY_BLOCK and count < 20:
                matricx_game[rnd_place_row][rnd_place_col] = consts.BOMB
                matricx_game[rnd_place_row][rnd_place_col + 1] = consts.BOMB
                matricx_game[rnd_place_row][rnd_place_col + 2] = consts.BOMB
                count += 1
    return matricx_game

def put_bushes(matricx_game):
    count = 0
    for i in range(25):
        for j in range(50):
            rnd_place_row = random.randint(0, 24)
            rnd_place_col = random.randint(0, 49)
            if matricx_game[rnd_place_row][rnd_place_col] == consts.EMPTY_BLOCK and count < 20:
                matricx_game[rnd_place_row][rnd_place_col] = consts.BUSH
                count += 1
    return matricx_game

def put_soldier(matricx_game):
    for row in range(0, 4):
        for col in range(0, 2):
            matricx_game[row][col] = consts.SOLDIER

    return matricx_game


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
        print()


def return_matricx():
    matrix = create()
    matrix = put_bombs(matrix)
    matrix_bushes = put_bushes(matrix)
    matrix = put_soldier(matrix)
    return matrix, matrix_bushes, create(), create()

