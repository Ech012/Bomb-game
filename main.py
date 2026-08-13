from Screen import *

import pygame

import game_field

matrix_with_bombs, matrix_bushes, game_matrix = game_field.return_matricx()






def main():
    global matrix_bushes
    pygame.init()
    pygame.font.init()
    my_font = pygame.font.SysFont('Comic Sans MS', 45)
    text_surface = my_font.render('Welcome to the flag game', False, (255, 255, 255))
    text_surface2 = my_font.render('Have Fun!', False, (255, 255, 255))

    pygame.display.set_caption("Grid Game")

    running = True
    while running:


        draw_background("green")
        draw_bushes_screen(matrix_bushes)
        screen.blit(text_surface, (50, 0))
        screen.blit(text_surface2, (50, 30))
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
                    matrix_bushes = draw_movment("right", matrix_bushes, matrix_with_bombs, game_matrix)
                elif event.key == pygame.K_LEFT:
                    matrix_bushes = draw_movment("left", matrix_bushes, matrix_with_bombs, game_matrix)
                elif event.key == pygame.K_UP:
                    matrix_bushes = draw_movment("up", matrix_bushes, matrix_with_bombs, game_matrix)
                elif event.key == pygame.K_DOWN:
                    matrix_bushes = draw_movment("down", matrix_bushes, matrix_with_bombs, game_matrix)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
