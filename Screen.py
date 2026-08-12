import pygame
import consts
import random
import game_field

screen = pygame.display.set_mode((consts.SCREEN_WIDTH, consts.SCREEN_HEIGHT))

bush_img = pygame.image.load(consts.BUSH_IMG).convert_alpha()
bush_img = pygame.transform.scale(screen, (50, 50))

matrix = game_field.get_matrix()

def draw_background(screen):
    screen.fill("green")


def draw_bushes():
    x = random.randint(0,consts.SCREEN_WIDTH)
    y = random.randint(0,consts.SCREEN_HEIGHT)

    screen.blit(bush_img, (x, y))









