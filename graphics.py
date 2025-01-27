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

def draw_a_cube(size, x_coord, y_coord, primary_color, secondary_color, screen, border_thickness=4):
    pygame.draw.rect(screen, primary_color, pygame.Rect(x_coord, y_coord, size, size))
    pygame.draw.rect(screen, secondary_color, pygame.Rect(x_coord, y_coord, size, size), border_thickness)


def draw_loose_screen(screen, font_color, font_size):
    font = pygame.font.Font(None, font_size)
    small_font = pygame.font.Font(None, font_size // 2)

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    panel_width = 300
    panel_height = 200
    panel_x = screen_width // 2 - panel_width // 2
    panel_y = screen_height // 2 - panel_height // 2

    panel = pygame.Surface((panel_width, panel_height))
    panel.fill((50, 50, 50))

    text = font.render("You lost!", True, font_color)
    text_rect = text.get_rect(center=(panel_width // 2, 50))
    panel.blit(text, text_rect)

    button_width = 200
    button_height = 40
    button_x = panel_width // 2 - button_width // 2

    play_again_button = pygame.Rect(button_x, 90, button_width, button_height)
    pygame.draw.rect(panel, (70, 70, 70), play_again_button)
    play_text = small_font.render("Play Again", True, font_color)
    play_text_rect = play_text.get_rect(center=play_again_button.center)
    panel.blit(play_text, play_text_rect)

    menu_button = pygame.Rect(button_x, 140, button_width, button_height)
    pygame.draw.rect(panel, (70, 70, 70), menu_button)
    menu_text = small_font.render("Main Menu", True, font_color)
    menu_text_rect = menu_text.get_rect(center=menu_button.center)
    panel.blit(menu_text, menu_text_rect)

    screen.blit(panel, (panel_x, panel_y))

    return (
        pygame.Rect(panel_x + button_x, panel_y + 90, button_width, button_height),
        pygame.Rect(panel_x + button_x, panel_y + 140, button_width, button_height)
    )


def draw_win_screen(screen, font_color, font_size):
    font = pygame.font.Font(None, font_size)
    small_font = pygame.font.Font(None, font_size // 2)

    screen_width = screen.get_width()
    screen_height = screen.get_height()

    panel_width = 300
    panel_height = 200
    panel_x = screen_width // 2 - panel_width // 2
    panel_y = screen_height // 2 - panel_height // 2

    panel = pygame.Surface((panel_width, panel_height))
    panel.fill((50, 50, 50))

    text = font.render("You won!", True, font_color)
    text_rect = text.get_rect(center=(panel_width // 2, 50))
    panel.blit(text, text_rect)

    button_width = 200
    button_height = 40
    button_x = panel_width // 2 - button_width // 2

    play_again_button = pygame.Rect(button_x, 90, button_width, button_height)
    pygame.draw.rect(panel, (70, 70, 70), play_again_button)
    play_text = small_font.render("Play Again", True, font_color)
    play_text_rect = play_text.get_rect(center=play_again_button.center)
    panel.blit(play_text, play_text_rect)

    menu_button = pygame.Rect(button_x, 140, button_width, button_height)
    pygame.draw.rect(panel, (70, 70, 70), menu_button)
    menu_text = small_font.render("Main Menu", True, font_color)
    menu_text_rect = menu_text.get_rect(center=menu_button.center)
    panel.blit(menu_text, menu_text_rect)

    screen.blit(panel, (panel_x, panel_y))

    return (
        pygame.Rect(panel_x + button_x, panel_y + 90, button_width, button_height),
        pygame.draw.rect(screen, (70, 70, 70),
                         pygame.Rect(panel_x + button_x, panel_y + 140, button_width, button_height))
    )


def draw_bomb(x, y, size, screen):
    bomb_color = (0, 0, 0)
    center_x = x + size // 2
    center_y = y + size // 2
    radius = size // 4
    pygame.draw.circle(screen, bomb_color, (center_x, center_y), radius)


def draw_a_board(field, size_of_the_display, start_x, start_y, closed_color, opened_color, border_color,
                 changed_field, screen, banners_font_color, banners_font_size, number_of_bombs, size_of_the_field):
    lost = False
    won = False
    buttons = None
    rows = len(field)
    cols = len(field[0])
    size_of_the_cube = size_of_the_display // cols

    #короче, тут если не будет работать,я не знаю, я писал это с чатом гпт
    bomb_clicked = any(changed_field[r][c] not in ["-", ">"] and field[r][c] == "b"
                       for r in range(rows) for c in range(cols))
    #за эти строчки (130 - 133) я не отвечаю!!!

    for i in range(rows):
        for j in range(cols):
            x = start_x + j * size_of_the_cube
            y = start_y + i * size_of_the_cube

            if changed_field[i][j] != "-" or (field[i][j] == "b" and bomb_clicked):
                draw_a_cube(size_of_the_cube, x, y, opened_color, border_color, screen)
            else:
                draw_a_cube(size_of_the_cube, x, y, closed_color, border_color, screen)

            if field[i][j] == "b" and bomb_clicked:
                draw_bomb(x, y, size_of_the_cube, screen)

            if changed_field[i][j] == ">":
                draw_flag_icon(x, y, size_of_the_cube, screen)
            elif changed_field[i][j] != "-":
                if field[i][j] == "b":
                    lost = True
                elif field[i][j] != 0:
                    font_size = int(size_of_the_cube * 0.65)
                    number_x = x + (size_of_the_cube / 2) - (font_size / 6)
                    number_y = y + (size_of_the_cube / 2) - (font_size / 4.5)
                    draw_a_number(str(field[i][j]), number_x, number_y, font_size, screen)

    if logic.count_correct_flags(field, changed_field, size_of_the_field) == number_of_bombs:
        won = True
        buttons = draw_win_screen(screen, banners_font_color, banners_font_size)

    if lost:
        buttons = draw_loose_screen(screen, banners_font_color, banners_font_size)

    return (not (lost or won)), buttons


def draw_flag_icon(x, y, size, screen):

    flag_color = (255, 0, 0)
    pole_color = (128, 128, 128)

    pole_width = size // 10
    pole_height = size // 2
    pole_x = x + size // 2 - pole_width // 2
    pole_y = y + size // 4
    pygame.draw.rect(screen, pole_color, pygame.Rect(pole_x, pole_y, pole_width, pole_height))

    flag_width = size // 3
    flag_height = size // 5
    flag_x = pole_x
    flag_y = pole_y
    pygame.draw.polygon(screen, flag_color, [(flag_x, flag_y), (flag_x + flag_width, flag_y + flag_height // 2), (flag_x, flag_y + flag_height)])



def draw_a_number(number, x, y, font_size, screen):
    number_colors = {
        "1": (0, 128, 255),
        "2": (0, 255, 0),
        "3": (255, 0, 0),
        "4": (138, 43, 226),
        "5": (255, 165, 0),
        "6": (64, 224, 208),
        "7": (255, 20, 147),
        "8": (128, 128, 128)
    }

    color = number_colors.get(number, (255, 255, 255))

    font = pygame.font.Font(None, font_size)
    text = font.render(number, True, color)
    screen.blit(text, (x, y))


DIFFICULTY = {
    "Easy": {"field_size": 5, "bombs": 5},
    "Medium": {"field_size": 10, "bombs": 15},
    "Hard": {"field_size": 15, "bombs": 35},
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