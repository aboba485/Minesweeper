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


def draw_a_board(FIELD, size_of_the_display, start_x, start_y, primary_color, secondary_color):
    rows = len(FIELD)
    cols = len(FIELED[0])
    size_of_the_cube = size_of_the_display // cols
    for i in range(rows):
        for j in range(cols):
            x = start_x + j * size_of_the_cube
            y = start_y + i * size_of_the_cube
            if changed_field[i][j] == "-":
                 draw_a_cube(size_of_the_cube, x, y, primary_color, secondary_color)

            else:
                draw_a_cube(size_of_the_cube, x, y, primary_color, secondary_color)
                font_size=size_of_the_cube//1.45
                # x=size_of_the_cube/2+x/1.17
                # y=size_of_the_cube/2+y/1.25
                x=size_of_the_cube/2+x/1.3333
                y=size_of_the_cube/2+y/1.3333
                draw_a_number("0", x, y, WHITE, int(font_size))



def draw_a_number(number, x, y, color, font_size):
    font = pygame.font.Font(None, font_size)
    text = font.render(number, True, color)
    SCREEN.blit(text, (x, y))





pygame.init()
SIZE_OF_THE_DISPLAY = 680
SCREEN = pygame.display.set_mode((SIZE_OF_THE_DISPLAY, SIZE_OF_THE_DISPLAY))
FIELED = main.get_the_field(16, 10)
changed_field= main.get_Field2()
changed_field[0][0] = FIELED[0][0]
print(changed_field)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BACKGROUND_COLOR = (28, 29, 31)
CELLS_COLOR = (31, 31, 31)
NUMBERS_COLOR = (35, 35, 35)

font_for_clock = pygame.font.Font(None, 36)
start_ticks = pygame.time.get_ticks()
pygame.display.set_caption('MineSweeper')

running = True
while running:
    SCREEN.fill(BACKGROUND_COLOR)

    text = font_for_clock.render(counter_of_the_time(start_ticks), True, BLACK)
    SCREEN.blit(text, (280, 0))

    draw_a_board(FIELED, SIZE_OF_THE_DISPLAY - 100, 50, 50, CELLS_COLOR, BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()