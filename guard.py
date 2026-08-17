from main import *
from consts import *

guard_img = pygame.image.load(consts.SOLDIER_IMG)
guard_img = pygame.transform.scale(soldier_img, (BLOCK_SIZE * 2, BLOCK_SIZE * 4))

def get_guard_position(matrix):
    for r in range(20,24):
        for c in range(0,2):
            matrix[r][c] = consts.GUARD
    return matrix


def draw_movment(matrix):
        current_row = -1
        current_col = -1
        direction = 1
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c] == consts.GUARD:
                    current_row = r
                    current_col = c
                    break
            if current_row != -1:
                break

        new_row = current_row
        new_col = current_col
        if current_row == -1:
            return matrix
        matrix[new_row][new_col] = consts.EMPTY_BLOCK
        new_col += direction
        new_row += direction

        if new_col == 49:
            direction = -1
        elif new_col == 0:
            direction = 1
        matrix[new_row][new_col] = consts.GUARD

        return matrix

def Assault_on_a_security_guard (matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == consts.GUARD:
                if matrix[r][c] == consts.SOLDIER:
                    create_message("Lose message", "You lost")
                    pygame.quit()
                    sys.exit()

def draw_guard(matrix):
    for row_idx in range(len(matrix)):
        for col_idx in range(len(matrix[row_idx])):

