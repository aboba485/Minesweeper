import pygame
import logic
import graphics

pygame.init()

SIZE_OF_THE_DISPLAY = 680
SIZE_OF_THE_FIELD = 9
NUMBER_OF_BOMBS = 10

SCREEN = pygame.display.set_mode((SIZE_OF_THE_DISPLAY, SIZE_OF_THE_DISPLAY))
FIELD = logic.get_the_field(SIZE_OF_THE_FIELD, NUMBER_OF_BOMBS)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BACKGROUND_COLOR = (28, 29, 31)
CELLS_COLOR = (31, 31, 31)
NUMBERS_COLOR = (35, 35, 35)
changed_field = logic.get_field2(SIZE_OF_THE_FIELD)
changed_field[0][0] = FIELD[0][0]
start_ticks = pygame.time.get_ticks()
pygame.display.set_caption('MineSweeper')

running = True
while running:
    SCREEN.fill(BACKGROUND_COLOR)

    graphics.draw_a_counter_of_the_time(start_ticks, SCREEN, WHITE)
    graphics.draw_a_board(FIELD, SIZE_OF_THE_DISPLAY - 100, 50, 50, CELLS_COLOR, BACKGROUND_COLOR, WHITE,
                          changed_field, SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
