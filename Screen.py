import pygame
import consts
import random
import game_field


BLOCK_SIZE = 10
screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

bush_img = pygame.image.load(consts.BUSH_IMG).convert_alpha()
bush_img = pygame.transform.scale(screen, (BLOCK_SIZE,BLOCK_SIZE))

bomb_img = pygame.image.load(consts.EXPLO_IMG).convert_alpha()
bomb_img = pygame.transform.scale(screen, (BLOCK_SIZE, BLOCK_SIZE))



matrix = game_field.get_matrix()

def draw_background(screen):
    screen.fill("green")



def drawGrid():
    blockSize = 10 #Set the size of the grid block
    for x in range(0, consts.WIDTH, blockSize):
        for y in range(0, consts.HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, consts.WHITE, rect, 1)





def drawObjects(grid):
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

            elif grid[row_idx][col_idx] == consts.BUSH:
                screen.blit(bush_img, (screen_x, screen_y))

            col_idx += 1





