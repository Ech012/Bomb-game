import time
import copy
import pygame
import consts
import random
import game_field
import sys
import tkinter as tk

matrix_with_bombs, matrix_bushes, empty_matrix, game_matrix = game_field.return_matricx()

BLOCK_SIZE = 10
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

bush_img = pygame.image.load(consts.BUSH_IMG)
bush_img = pygame.transform.scale(bush_img, (BLOCK_SIZE, BLOCK_SIZE))

bomb_img = pygame.image.load(consts.MINE_IMG)
bomb_img = pygame.transform.scale(bomb_img, (BLOCK_SIZE * 3, BLOCK_SIZE))

flag_img = pygame.image.load(consts.FLAG_IMG)
flag_img = pygame.transform.scale(flag_img, (BLOCK_SIZE * 4, BLOCK_SIZE * 3))

soldier_img = pygame.image.load(consts.SOLDIER_IMG)
soldier_img = pygame.transform.scale(soldier_img, (BLOCK_SIZE * 2, BLOCK_SIZE * 6))

soldier_img_night = pygame.image.load(consts.SOLDIER_IMG_NIGHT)
soldier_img_night = pygame.transform.scale(soldier_img_night, (BLOCK_SIZE * 2, BLOCK_SIZE * 6))


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
    blockSize = 10
    for x in range(0, consts.SCREEN_WIDTH, blockSize):
        for y in range(0, consts.SCREEN_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)


def draw_movment(direction, matrix, matrix_bombs):
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
        if current_row + 6 < 25:
            new_row += 1
    elif direction == "up":
        if current_row - 1 >= 0:
            new_row -= 1

    next_bottom_row = new_row + 5
    if matrix_bombs[next_bottom_row][new_col] == consts.BOMB or \
            matrix_bombs[next_bottom_row][new_col + 1] == consts.BOMB:
        root = tk.Tk()
        root.title("Lose message")
        root.geometry("400x200")

        text_label = tk.Label(root, text="You lost!", font=("Arial", 16))

        text_label.pack(pady=50)

        root.mainloop()

        sys.exit()


    reached_flag = False
    for r in range(new_row, new_row + 6):
        for c in range(new_col, new_col + 2):
            if matrix[r][c] == consts.FLAG:
                reached_flag = True
                break
        if reached_flag:
            break

    if reached_flag:
        print("kdfksjdfksjdfksjdfksjdf")

    for r in range(current_row, current_row + 6):
        for c in range(current_col, current_col + 2):
            matrix[r][c] = consts.EMPTY_BLOCK

    for r in range(new_row, new_row + 6):
        for c in range(new_col, new_col + 2):
            matrix[r][c] = consts.SOLDIER

    return matrix


def get_soldier_position(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == consts.SOLDIER:
                return r, c
    return -1, -1


def main():
    global matrix_bushes
    pygame.init()
    pygame.display.set_caption("Grid Game")

    running = True
    while running:
        draw_background("green")
        draw_bushes_screen(matrix_bushes)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    s_row, s_col = get_soldier_position(matrix_bushes)
                    draw_background("black")
                    drawGrid()
                    draw_bombs_screen(matrix_with_bombs, s_row, s_col)
                    pygame.display.flip()
                    pygame.time.wait(1000)

                elif event.key == pygame.K_RIGHT:
                    matrix_bushes = draw_movment("right", matrix_bushes, matrix_with_bombs)
                elif event.key == pygame.K_LEFT:
                    matrix_bushes = draw_movment("left", matrix_bushes, matrix_with_bombs)
                elif event.key == pygame.K_UP:
                    matrix_bushes = draw_movment("up", matrix_bushes, matrix_with_bombs)
                elif event.key == pygame.K_DOWN:
                    matrix_bushes = draw_movment("down", matrix_bushes, matrix_with_bombs)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
