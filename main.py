import pygame
import logic
import graphics

pygame.init()

FIELD = []
SIZE_OF_THE_DISPLAY = 680
SCREEN = pygame.display.set_mode((SIZE_OF_THE_DISPLAY, SIZE_OF_THE_DISPLAY))
pygame.display.set_caption("MineSweeper")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BACKGROUND_COLOR = (28, 29, 31)
CELLS_COLOR = (31, 31, 31)
NUMBERS_COLOR = (35, 35, 35)

difficulty = graphics.show_menu(SCREEN, SIZE_OF_THE_DISPLAY, BACKGROUND_COLOR, WHITE, BLACK)
SIZE_OF_THE_FIELD = difficulty["field_size"]
NUMBER_OF_BOMBS = difficulty["bombs"]

SIZE_OF_THE_CUBE = (SIZE_OF_THE_DISPLAY - 100) // SIZE_OF_THE_FIELD
START_Y = 50
START_X = 50
changed_field = logic.get_field2(SIZE_OF_THE_FIELD)
first = True
start_ticks = pygame.time.get_ticks()

running = True
game_active = True
while running:
    SCREEN.fill(BACKGROUND_COLOR)
    if first:
        FIELD = logic.get_empty_field(SIZE_OF_THE_FIELD)

    game_active = graphics.draw_a_board(FIELD, SIZE_OF_THE_DISPLAY - 100, START_X, START_Y, CELLS_COLOR, BACKGROUND_COLOR, NUMBERS_COLOR,
        changed_field, SCREEN, BLACK,100, NUMBER_OF_BOMBS, SIZE_OF_THE_FIELD,)

    if game_active:
        graphics.draw_a_counter_of_the_time(start_ticks, SCREEN, WHITE)
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
                        FIELD = logic.get_the_field(FIELD, SIZE_OF_THE_FIELD, NUMBER_OF_BOMBS,START_X,START_Y, x, y, SIZE_OF_THE_CUBE, SIZE_OF_THE_DISPLAY,)
                    changed_field = logic.define_coordinate(START_Y, START_Y, x, y, SIZE_OF_THE_DISPLAY, SIZE_OF_THE_CUBE, changed_field, FIELD, SIZE_OF_THE_FIELD,)
                elif pygame.mouse.get_pressed()[2]:
                    changed_field = logic.place_flag(START_X, START_Y, x, y, SIZE_OF_THE_DISPLAY, SIZE_OF_THE_CUBE, changed_field, NUMBER_OF_BOMBS, SIZE_OF_THE_FIELD,)

    pygame.display.flip()

pygame.quit()
