from dataclasses import Field

import pygame
import logic
import graphics

pygame.init()

SIZE_OF_THE_DISPLAY = 680
SIZE_OF_THE_FIELD = 5
NUMBER_OF_BOMBS = 15


SCREEN = pygame.display.set_mode((SIZE_OF_THE_DISPLAY, SIZE_OF_THE_DISPLAY))
BANNERS_FONT_SIZE = 100
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BACKGROUND_COLOR = (28, 29, 31)
CELLS_COLOR = (31, 31, 31)
NUMBERS_COLOR = (35, 35, 35)
START_X = 50
START_Y = 50
SIZE_OF_THE_CUBE = (SIZE_OF_THE_DISPLAY - START_X - START_X) // SIZE_OF_THE_FIELD
first=True

changed_field = logic.get_field2(SIZE_OF_THE_FIELD)
start_ticks = pygame.time.get_ticks()
pygame.display.set_caption('MineSweeper')

running = True
game_active = True

while running:

    SCREEN.fill(BACKGROUND_COLOR)
    if first:
        FIELD = logic.get_empty_field(SIZE_OF_THE_FIELD)
    game_active = graphics.draw_a_board(
        FIELD, SIZE_OF_THE_DISPLAY - 100, START_X, START_Y, BLUE, WHITE, RED,
        changed_field, SCREEN, BLACK, BANNERS_FONT_SIZE, NUMBER_OF_BOMBS, SIZE_OF_THE_FIELD, )

    if game_active:
        elapsed_time = graphics.draw_a_counter_of_the_time(start_ticks, SCREEN, WHITE)
    else:
        graphics.draw_a_counter_of_the_time(start_ticks, SCREEN, WHITE, freeze_timer=True)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_active and event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if START_X < x < SIZE_OF_THE_DISPLAY - START_X and START_Y < y < SIZE_OF_THE_DISPLAY - START_Y:
                if pygame.mouse.get_pressed()[0]:
                    if first:
                        first = False
                        FIELD = logic.get_the_field(FIELD, SIZE_OF_THE_FIELD, NUMBER_OF_BOMBS, START_X, START_Y, x, y, SIZE_OF_THE_CUBE, SIZE_OF_THE_DISPLAY)
                    changed_field = logic.define_coordinate(
                        START_X, START_Y, x, y, SIZE_OF_THE_DISPLAY, SIZE_OF_THE_CUBE, changed_field, FIELD,
                        SIZE_OF_THE_FIELD
                    )
                elif pygame.mouse.get_pressed()[2]:
                    changed_field = logic.place_flag(
                        START_X, START_Y, x, y, SIZE_OF_THE_DISPLAY, SIZE_OF_THE_CUBE, changed_field
                        , NUMBER_OF_BOMBS, SIZE_OF_THE_FIELD)

    pygame.display.flip()

pygame.quit()
