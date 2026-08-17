import time
import copy
import pygame
import consts
import random
import game_field
import sys
import tkinter as tk
import guard

import random
BLOCK_SIZE = consts.BLOCK_SIZE
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))


last_teleport_coords = None

bush_img = pygame.image.load(consts.BUSH_IMG)
bush_img = pygame.transform.scale(bush_img, (BLOCK_SIZE * 3, BLOCK_SIZE * 3))

bomb_img = pygame.image.load(consts.MINE_IMG)
bomb_img = pygame.transform.scale(bomb_img, (BLOCK_SIZE * 3, BLOCK_SIZE))

flag_img = pygame.image.load(consts.FLAG_IMG)
flag_img = pygame.transform.scale(flag_img, (BLOCK_SIZE * 4, BLOCK_SIZE * 3))

soldier_img = pygame.image.load(consts.SOLDIER_IMG)
soldier_img = pygame.transform.scale(soldier_img, (BLOCK_SIZE * 2, BLOCK_SIZE * 4))

soldier_img_night = pygame.image.load(consts.SOLDIER_IMG_NIGHT)
soldier_img_night = pygame.transform.scale(soldier_img_night, (BLOCK_SIZE * 2, BLOCK_SIZE * 4))

guard_img = pygame.image.load(consts.SOLDIER_IMG)
guard_img = pygame.transform.scale(soldier_img, (BLOCK_SIZE * 2, BLOCK_SIZE * 4))


def draw_bushes_screen(grid):
    for row_idx in range(len(grid)):
        col_idx = 0
        while col_idx < len(grid[row_idx]):
            screen_x = col_idx * BLOCK_SIZE
            screen_y = row_idx * BLOCK_SIZE

            if grid[row_idx][col_idx] == consts.BUSH:
                screen.blit(bush_img, (screen_x, screen_y))
                col_idx += 1

            elif grid[row_idx][col_idx] == consts.FLAG:
                if row_idx == 22 and col_idx == 46:
                    screen.blit(flag_img, (screen_x, screen_y))
                col_idx += 1

            elif grid[row_idx][col_idx] == consts.SOLDIER:
                is_left_edge = (col_idx == 0 or grid[row_idx][col_idx - 1] != consts.SOLDIER)
                is_top_edge = (row_idx == 0 or grid[row_idx - 1][col_idx] != consts.SOLDIER)

                if is_left_edge and is_top_edge:
                    screen.blit(soldier_img, (screen_x, screen_y))
                col_idx += 1

            elif grid[row_idx][col_idx] == consts.GUARD:
                is_left_edge = (col_idx == 0 or grid[row_idx][col_idx - 1] != consts.GUARD)
                is_top_edge = (row_idx == 0 or grid[row_idx - 1][col_idx] != consts.GUARD)

                if is_left_edge and is_top_edge:
                    screen.blit(guard_img, (screen_x, screen_y))
                col_idx += 1
            else:
                col_idx += 1


def draw_bombs_screen(grid_bombs, current_soldier_row, current_soldier_col):

    for row_idx in range(len(grid_bombs)):
        col_idx = 0
        while col_idx < len(grid_bombs[row_idx]):
            screen_x = col_idx * BLOCK_SIZE
            screen_y = row_idx * BLOCK_SIZE

            if grid_bombs[row_idx][col_idx] == consts.BOMB:
                if col_idx <= len(grid_bombs[row_idx]) - 3 and \
                        grid_bombs[row_idx][col_idx + 1] == consts.BOMB and \
                        grid_bombs[row_idx][col_idx + 2] == consts.BOMB:

                    screen.blit(bomb_img, (screen_x, screen_y))
                    col_idx += 3
                    continue
                else:
                    single_bomb = pygame.transform.scale(bomb_img, (BLOCK_SIZE, BLOCK_SIZE))
                    screen.blit(single_bomb, (screen_x, screen_y))
                    col_idx += 1

            if grid_bombs[row_idx][col_idx] == consts.TELEPORT:
                if col_idx <= len(grid_bombs[row_idx]) - 3 and \
                        grid_bombs[row_idx][col_idx + 1] == consts.TELEPORT and \
                        grid_bombs[row_idx][col_idx + 2] == consts.TELEPORT:

                    screen.blit(bomb_img, (screen_x, screen_y))
                    col_idx += 3
                    continue
                else:
                    single_bomb = pygame.transform.scale(bomb_img, (BLOCK_SIZE, BLOCK_SIZE))
                    screen.blit(single_bomb, (screen_x, screen_y))
                    col_idx += 1


            elif grid_bombs[row_idx][col_idx] == consts.FLAG:
                if row_idx == 22 and col_idx == 46:
                    screen.blit(flag_img, (screen_x, screen_y))
                col_idx += 1
            else:
                col_idx += 1

    if current_soldier_row != -1 and current_soldier_col != -1:
        screen.blit(soldier_img_night, (current_soldier_col * BLOCK_SIZE, current_soldier_row * BLOCK_SIZE))


def draw_background(color):
    screen.fill(pygame.Color(color))


def drawGrid():
    blockSize = consts.BLOCK_SIZE
    for x in range(0, consts.SCREEN_WIDTH, blockSize):
        for y in range(0, consts.SCREEN_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (0, 160, 0), rect, 1)



def create_message(title,text):
    root = tk.Tk()
    root.title(title)
    root.geometry("400x200")

    text_label = tk.Label(root, text=text, font=("Arial", 16))

    text_label.pack(pady=50)

    root.after(3000, root.destroy)

    root.mainloop()


def get_teleport_loc(matrix_bombs, current_feet_row, current_feet_col):
    while True:
        rnd_place_row = random.randint(0, 25 - 4)
        rnd_place_col = random.randint(0, 50 - 2)

        if matrix_bombs[rnd_place_row][rnd_place_col] == consts.TELEPORT:
            if rnd_place_row != current_feet_row or rnd_place_col != current_feet_col:
                return rnd_place_row, rnd_place_col

def draw_movment(direction, matrix, matrix_bombs, terrain):
    global last_teleport_coords
    current_row = -1
    current_col = -1

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == consts.SOLDIER:
                current_row = r
                current_col = c
                break
        if current_row != -1:
            break

    if current_row == -1:
        return matrix

    new_row = current_row
    new_col = current_col

    if direction == "right":
        if current_col + 2 < 50:
            new_col += 1
    elif direction == "left":
        if current_col - 1 >= 0:
            new_col -= 1
    elif direction == "down":
        if current_row + 4 < 25:
            new_row += 1
    elif direction == "up":
        if current_row - 1 >= 0:
            new_row -= 1

    feet_row = new_row + 3

    if matrix_bombs[feet_row][new_col] == consts.BOMB or \
            matrix_bombs[feet_row][new_col + 1] == consts.BOMB:
        create_message("Lose message", "You lost")
        pygame.quit()
        sys.exit()

    reached_flag = False
    if 22 <= feet_row <= 24:
        if (feet_row == 23 or feet_row == 24) and matrix[feet_row][new_col] == consts.FLAG:
            reached_flag = True
        elif new_col == 45:
            reached_flag = True

    if reached_flag:
        create_message("Win message", "You won!!!!")
        pygame.quit()
        sys.exit()




    if matrix_bombs[feet_row][new_col] == consts.TELEPORT:
        if last_teleport_coords == (feet_row, new_col):
            pass
        else:
            teleport_target_row, teleport_target_col = get_teleport_loc(matrix_bombs, feet_row, new_col)

            new_row = teleport_target_row - 3
            new_col = teleport_target_col

            last_teleport_coords = (teleport_target_row, teleport_target_col)
    else:
        last_teleport_coords = None

    for r in range(current_row, current_row + 4):
        for c in range(current_col, current_col + 2):
            matrix[r][c] = terrain[r][c]

    for r in range(new_row, new_row + 4):
        for c in range(new_col, new_col + 2):
            matrix[r][c] = consts.SOLDIER

    return matrix



def get_soldier_position(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == consts.SOLDIER:
                return r, c
    return -1, -1

def draw_guard_screen(grid):

    for row_idx in range(len(grid)):
        col_idx = 0
        while col_idx < len(grid[row_idx]):
            screen_x = col_idx * BLOCK_SIZE
            screen_y = row_idx * BLOCK_SIZE
            if grid[row_idx][col_idx] == consts.GUARD:
                is_left_edge = (col_idx == 0 or grid[row_idx][col_idx - 1] != consts.GUARD)
                is_top_edge = (row_idx == 0 or grid[row_idx - 1][col_idx] != consts.GUARD)

                if is_left_edge and is_top_edge:
                    screen.blit(guard_img, (screen_x, screen_y))
                col_idx += 1

            else:
                col_idx += 1