import time
import copy
import pygame
import consts
import random
import game_field

matrix = game_field.return_matricx()

BLOCK_SIZE = 10
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))


bush_img = pygame.image.load(consts.BUSH_IMG)
bush_img = pygame.transform.scale(bush_img, (BLOCK_SIZE,BLOCK_SIZE))

bomb_img = pygame.image.load(consts.MINE_IMG)
bomb_img = pygame.transform.scale(bomb_img, (30, BLOCK_SIZE))

flag_img = pygame.image.load(consts.FLAG_IMG)
flag_img = pygame.transform.scale(flag_img, (BLOCK_SIZE, BLOCK_SIZE))





def draw_grid_screen(grid):
    for row_idx in range(len(grid)):
        col_idx = 0
        while col_idx < len(grid[row_idx]):

            screen_x = col_idx * BLOCK_SIZE
            screen_y = row_idx * BLOCK_SIZE

            if col_idx <= len(grid[row_idx]) - 3 and \
                    grid[row_idx][col_idx] == consts.BOMB and \
                    grid[row_idx][col_idx + 1] == consts.BOMB and \
                    grid[row_idx][col_idx + 2] == consts.BOMB:

                screen.blit(bomb_img, (screen_x, screen_y))


                col_idx += 3
                continue

            if grid[row_idx][col_idx] == consts.BUSH:
                screen.blit(bush_img, (screen_x, screen_y))

            elif grid[row_idx][col_idx] == consts.FLAG:
                screen.blit(flag_img, (screen_x, screen_y))

            col_idx += 1





def draw_background(color):
    screen.fill(color)



def drawGrid():
    blockSize = 10 #Set the size of the grid block
    for x in range(0, consts.SCREEN_WIDTH, blockSize):
        for y in range(0, consts.SCREEN_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, consts.WHITE, rect, 1)





def draw_game_screen(grid):
    for row_idx in range(len(grid)):
        col_idx = 0
        while col_idx < len(grid[row_idx]):

            screen_x = col_idx * BLOCK_SIZE
            screen_y = row_idx * BLOCK_SIZE

            # if col_idx <= len(grid[row_idx]) - 3 and \
            #         grid[row_idx][col_idx] == consts.BOMB and \
            #         grid[row_idx][col_idx + 1] == consts.BOMB and \
            #         grid[row_idx][col_idx + 2] == consts.BOMB:
            #
            #     screen.blit(bomb_img, (screen_x, screen_y))
            #
            #
            #     col_idx += 3
            #     continue

            if grid[row_idx][col_idx] == consts.BUSH:
                screen.blit(bush_img, (screen_x, screen_y))

            elif grid[row_idx][col_idx] == consts.FLAG:
                screen.blit(flag_img, (screen_x, screen_y))

            col_idx += 1





def draw_screen_for_a_second(grid):

    grid_backup = copy.deepcopy(grid)
    for row_idx in range(len(grid)):
        col_idx = 0
        while col_idx < len(grid[row_idx]):

            screen_x = col_idx * BLOCK_SIZE
            screen_y = row_idx * BLOCK_SIZE

            if col_idx <= len(grid[row_idx]) - 3 and \
                    grid[row_idx][col_idx] == consts.BOMB and \
                    grid[row_idx][col_idx + 1] == consts.BOMB and \
                    grid[row_idx][col_idx + 2] == consts.BOMB:




                col_idx += 3
            elif grid[row_idx][col_idx] == consts.BUSH:
                grid[row_idx][col_idx] = consts.EMPTY_BLOCK
            else:
                col_idx += 1
    return grid_backup



def put_back_bushes(grid_backup, grid):


    grid_with_bobms = copy.deepcopy(grid_backup)
    for i in range(len(grid_backup)):
        for j in range(len(grid_backup[i])):
            if grid_backup[i][j] == consts.BUSH:
                grid[i][j] = consts.BUSH

    # for row_idx in range(len(grid)):
    #     col_idx = 0
    #     while col_idx < len(grid[row_idx]):
    #
    #         screen_x = col_idx * BLOCK_SIZE
    #         screen_y = row_idx * BLOCK_SIZE
    #
    #
    #         if grid[row_idx][col_idx] == consts.BUSH:
    #             screen.blit(bush_img, (screen_x, screen_y))
    #
    #         elif grid[row_idx][col_idx] == consts.FLAG:
    #             screen.blit(flag_img, (screen_x, screen_y))
    #
    #
    #
    #         col_idx += 1





def create_matrixes():
    draw_background("black")
    drawGrid()
    backup_grid = draw_screen_for_a_second(matrix)
    draw_grid_screen(matrix)
    pygame.display.flip()
    pygame.time.wait(3000)
    put_back_bushes(backup_grid, matrix)



def main():


    pygame.init()

    draw_background("green")
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    draw_background("black")
                    drawGrid()
                    backup_grid = draw_screen_for_a_second(matrix)
                    draw_grid_screen(matrix)
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    put_back_bushes(backup_grid, matrix)

                    draw_grid_screen(matrix)

                    print("asdasdasdasd")


        draw_game_screen(matrix)

        pygame.display.flip()

    pygame.quit()

main()




