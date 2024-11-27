import pygame
import main


def counter_of_the_time(start_ticks):
    elapsed_ticks = pygame.time.get_ticks() - start_ticks
    seconds = (elapsed_ticks // 1000) % 60
    minutes = (elapsed_ticks // 1000) // 60
    return f"min: {minutes} sec: {seconds}"


def draw_a_cube(size, x_coord, y_coord, primary_color, secondary_color):
    pygame.draw.rect(SCREEN, primary_color, pygame.Rect(x_coord, y_coord, size, size))
    pygame.draw.rect(SCREEN, secondary_color, pygame.Rect(x_coord, y_coord, size, size), 4)


def draw_a_board(field, size_of_the_display, start_x, start_y, primary_color, secondary_color):
    rows = len(field)
    cols = len(field[0])
    size_of_the_cube = size_of_the_display // cols
    for i in range(rows):
        for j in range(cols):
            x = start_x + j * size_of_the_cube
            y = start_y + i * size_of_the_cube

            if field[i][j].islower():
                draw_a_cube(size_of_the_cube, x, y, primary_color, secondary_color)

            elif field[i][j].isupper():
                draw_a_cube(size_of_the_cube, x, y, WHITE, secondary_color)


pygame.init()
SIZE_OF_THE_DISPLAY = 680
SCREEN = pygame.display.set_mode((SIZE_OF_THE_DISPLAY, SIZE_OF_THE_DISPLAY))
field = main.get_the_field(9, 10)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BACKGROUND_COLOR = (28, 29, 31)
CELLS_COLOR = (31, 31, 31)

font = pygame.font.Font(None, 36)
start_ticks = pygame.time.get_ticks()
pygame.display.set_caption('MineSweeper')

running = True
while running:
    SCREEN.fill(BACKGROUND_COLOR)

    text = font.render(counter_of_the_time(start_ticks), True, BLACK)
    SCREEN.blit(text, (280, 0))

    draw_a_board(field, SIZE_OF_THE_DISPLAY - 100, 50, 50, CELLS_COLOR, BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()