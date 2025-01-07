import pygame
import logic

def draw_a_counter_of_the_time(start_ticks, screen, background_color, freeze_timer=False):
    font_for_clock = pygame.font.Font(None, 36)

    if not hasattr(draw_a_counter_of_the_time, "frozen_time"):
        draw_a_counter_of_the_time.frozen_time = 0

    if freeze_timer:
        elapsed_ticks = draw_a_counter_of_the_time.frozen_time
    else:
        elapsed_ticks = pygame.time.get_ticks() - start_ticks
        draw_a_counter_of_the_time.frozen_time = elapsed_ticks

    seconds = (elapsed_ticks // 1000) % 60
    minutes = (elapsed_ticks // 1000) // 60
    text = font_for_clock.render(f"min: {minutes} sec: {seconds}", True, background_color)
    screen.blit(text, (280, 0))

def draw_a_cube(size, x_coord, y_coord, primary_color, secondary_color, screen):
    pygame.draw.rect(screen, primary_color, pygame.Rect(x_coord, y_coord, size, size))
    pygame.draw.rect(screen, secondary_color, pygame.Rect(x_coord, y_coord, size, size), 4)


def draw_a_board(field, size_of_the_display, start_x, start_y, cells_color_background, cells_boarders_color, font_color,
                 changed_field, screen, banners_font_color, banners_font_size, number_of_bombs, size_of_the_field):
    lost = False
    won = False
    rows = len(field)
    cols = len(field[0])
    size_of_the_cube = size_of_the_display // cols

    for i in range(rows):
        for j in range(cols):
            x = start_x + j * size_of_the_cube
            y = start_y + i * size_of_the_cube

            draw_a_cube(size_of_the_cube, x, y, cells_color_background, cells_boarders_color, screen)

            if changed_field[i][j] != "-":
                if field[i][j] == "b" and changed_field[i][j] != ">":
                    lost = True

                font_size = int(size_of_the_cube * 0.65)
                number_x = x + (size_of_the_cube / 2) - (font_size / 6)
                number_y = y + (size_of_the_cube / 2) - (font_size / 4.5)

                if changed_field[i][j] != ">":
                    draw_a_number(str(field[i][j]), number_x, number_y, font_color, font_size, screen)
                elif changed_field[i][j] == ">":
                    draw_a_number(">", number_x, number_y, font_color, font_size, screen)

    if logic.count_correct_flags(field, changed_field, size_of_the_field) == number_of_bombs:
        won = True
        draw_win_screen(screen, banners_font_color, banners_font_size)

    if lost:
        draw_loose_screen(screen, banners_font_color, banners_font_size)

    return not (lost or won)


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


def draw_win_screen(screen, font_color, font_size):
    font = pygame.font.Font(None, font_size)
    text = font.render("You won!", True, font_color)
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(text, text_rect)


DIFFICULTY = {
    "Easy": {"field_size": 5, "bombs": 1},
    "Medium": {"field_size": 10, "bombs": 1},
    "Hard": {"field_size": 15, "bombs": 1},
}


def show_menu(screen, display_size, background_color, text_color, button_text_color):
    font = pygame.font.Font(None, 70)
    small_font = pygame.font.Font(None, 50)

    while True:
        screen.fill(background_color)

        title_text = font.render("Choose Difficulty", True, text_color)
        screen.blit(
            title_text,
            (display_size // 2 - title_text.get_width() // 2, 50),
        )

        button_y = 150
        for idx, level in enumerate(DIFFICULTY.keys()):
            button_text = small_font.render(level, True, button_text_color)
            button_rect = pygame.Rect(
                display_size // 2 - 100, button_y + idx * 100, 200, 50
            )
            pygame.draw.rect(screen, text_color, button_rect)
            screen.blit(
                button_text,
                (
                    button_rect.x + (button_rect.width - button_text.get_width()) // 2,
                    button_rect.y + (button_rect.height - button_text.get_height()) // 2,
                ),
            )

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                button_y = 150
                for idx, level in enumerate(DIFFICULTY.keys()):
                    button_rect = pygame.Rect(
                        display_size // 2 - 100, button_y + idx * 100, 200, 50
                    )
                    if button_rect.collidepoint(x, y):
                        return DIFFICULTY[level]