import consts
import Screen
import pygame
import sys

GUARD_HEIGHT = 4
GUARD_WIDTH = 2

GUARD_ROW_BOTTOM = GUARD_ROW_START = 24 - GUARD_HEIGHT + 1  # פינה שמאלית-תחתונה
GUARD_ROW_TOP = 0                                           # פינה ימנית-עליונה
GUARD_COL_LEFT = 0
GUARD_COL_RIGHT = 47                                         # 49 - GUARD_WIDTH


def _build_diagonal_path(row_start, col_start, row_end, col_end):
    """בונה רשימת נקודות על קו אלכסוני בין שתי הפינות (אלגוריתם Bresenham)."""
    points = []
    dx = col_end - col_start
    dy = row_end - row_start
    steps = max(abs(dx), abs(dy))
    for i in range(steps + 1):
        t = i / steps
        r = round(row_start + dy * t)
        c = round(col_start + dx * t)
        points.append((r, c))
    return points


GUARD_PATH = _build_diagonal_path(GUARD_ROW_START, GUARD_COL_LEFT, GUARD_ROW_TOP, GUARD_COL_RIGHT)
guard_path_index = 0
guard_direction = 1  # 1 = מתקדם בנתיב, -1 = חוזר בנתיב


def get_guard_position(matrix):
    r, c = GUARD_PATH[0]
    for row in range(r, r + GUARD_HEIGHT):
        for col in range(c, c + GUARD_WIDTH):
            matrix[row][col] = consts.GUARD
    return matrix


def draw_movment_guard(matrix, terrain):
    global guard_path_index, guard_direction

    current_row, current_col = GUARD_PATH[guard_path_index]

    guard_path_index += guard_direction
    if guard_path_index >= len(GUARD_PATH) - 1:
        guard_path_index = len(GUARD_PATH) - 1
        guard_direction = -1
    elif guard_path_index <= 0:
        guard_path_index = 0
        guard_direction = 1

    new_row, new_col = GUARD_PATH[guard_path_index]

    for r in range(current_row, current_row + GUARD_HEIGHT):
        for c in range(current_col, current_col + GUARD_WIDTH):
            matrix[r][c] = terrain[r][c]

    for r in range(new_row, new_row + GUARD_HEIGHT):
        for c in range(new_col, new_col + GUARD_WIDTH):
            matrix[r][c] = consts.GUARD

    return matrix


def Assault_on_a_security_guard(matrix):
    s_row, s_col = Screen.get_soldier_position(matrix)
    if s_row == -1:
        return
    for r in range(s_row, s_row + 4):
        for c in range(s_col, s_col + 2):
            if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]):
                if matrix[r][c] == consts.GUARD:
                    Screen.create_message("Lose message", "You lost")
                    pygame.quit()
                    sys.exit()