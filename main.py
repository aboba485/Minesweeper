import pygame
import logic
import graphics

pygame.init()

SIZE_OF_THE_DISPLAY = 680
SIZE_OF_THE_FIELD = 10
NUMBER_OF_BOMBS = 15

SCREEN = pygame.display.set_mode((SIZE_OF_THE_DISPLAY, SIZE_OF_THE_DISPLAY))
FIELD = logic.get_the_field(SIZE_OF_THE_FIELD, NUMBER_OF_BOMBS)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BACKGROUND_COLOR = (28, 29, 31)
CELLS_COLOR = (31, 31, 31)
NUMBERS_COLOR = (35, 35, 35)
START_X = 50
START_Y = 50
counter = 0
SIZE_OF_THE_CUBE = (SIZE_OF_THE_DISPLAY - START_X - START_X) // SIZE_OF_THE_FIELD
changed_field = logic.get_field2(SIZE_OF_THE_FIELD)
start_ticks = pygame.time.get_ticks()
pygame.display.set_caption('MineSweeper')


running = True
while running:
    SCREEN.fill(BACKGROUND_COLOR)

    graphics.draw_a_counter_of_the_time(start_ticks, SCREEN, WHITE)
    graphics.draw_a_board(FIELD, SIZE_OF_THE_DISPLAY - 100, START_X, START_Y, BLUE, WHITE, RED,
                          changed_field, SCREEN)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if START_X < x < SIZE_OF_THE_DISPLAY - START_X and START_Y < y < SIZE_OF_THE_DISPLAY - START_Y:
                if pygame.mouse.get_pressed()[0]:
                    changed_field = logic.define_coordinate(START_X, START_Y, x, y, SIZE_OF_THE_DISPLAY, SIZE_OF_THE_CUBE, changed_field, FIELD, SIZE_OF_THE_FIELD)
                elif pygame.mouse.get_pressed()[2]:
                    counter2 = logic.count_flags(changed_field, SIZE_OF_THE_FIELD)
                    if counter2 < NUMBER_OF_BOMBS:
                        changed_field = logic.place_flag(START_X, START_Y, x, y, SIZE_OF_THE_DISPLAY, SIZE_OF_THE_CUBE, changed_field)
        counter = 0
        counter = logic.count_correct_flags(FIELD, changed_field, SIZE_OF_THE_FIELD)
        if counter == NUMBER_OF_BOMBS:
            running = False

    pygame.display.flip()

pygame.quit()
