import pygame


def draw_a_counter_of_the_time(start_ticks, screen, background_color):
    font_for_clock = pygame.font.Font(None, 36)
    elapsed_ticks = pygame.time.get_ticks() - start_ticks
    seconds = (elapsed_ticks // 1000) % 60
    minutes = (elapsed_ticks // 1000) // 60
    text = font_for_clock.render(f"min: {minutes} sec: {seconds}", True, background_color)
    screen.blit(text, (280, 0))


def draw_a_cube(size, x_coord, y_coord, primary_color, secondary_color, screen):
    pygame.draw.rect(screen, primary_color, pygame.Rect(x_coord, y_coord, size, size))
    pygame.draw.rect(screen, secondary_color, pygame.Rect(x_coord, y_coord, size, size), 4)


def draw_a_board(field, size_of_the_display, start_x, start_y, cells_color_background, cells_boarders_color, font_color,
                 changed_field, screen, banners_font_color, banners_font_size):
    lost = False
    rows = len(field)
    cols = len(field[0])
    size_of_the_cube = size_of_the_display // cols

    for i in range(rows):
        for j in range(cols):
            x = start_x + j * size_of_the_cube
            y = start_y + i * size_of_the_cube

            draw_a_cube(size_of_the_cube, x, y, cells_color_background, cells_boarders_color, screen)

            if changed_field[i][j] != "-":
                if field[i][j] == "b":
                    lost = True

                font_size = int(size_of_the_cube * 0.65)
                number_x = x + (size_of_the_cube / 2) - (font_size / 6)
                number_y = y + (size_of_the_cube / 2) - (font_size / 4.5)

                if changed_field[i][j] != ">":
                    draw_a_number(str(field[i][j]), number_x, number_y, font_color, font_size, screen)
                else:
                    draw_a_number(">", number_x, number_y, font_color, font_size, screen)

    if lost:
        draw_loose_screen(screen, banners_font_color, banners_font_size)


def draw_a_number(number, x, y, color, font_size, screen):
    font = pygame.font.Font(None, font_size)
    text = font.render(number, True, color)
    screen.blit(text, (x, y))


def draw_loose_screen(screen, font_color, font_size):
    font = pygame.font.Font(None, font_size)
    text = font.render("You lost!", True, font_color)
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)