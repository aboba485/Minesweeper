import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)

X = 400
Y = 400

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('Show Text')


def draw_loose_screen(display, x, y, font_color):
    font_size = int((x + y) / 2 * 0.2)
    font = pygame.font.Font(None, font_size)
    text = font.render("You lost!", True, font_color)
    text_rect = text.get_rect(center=(x // 2, y // 2))
    display.blit(text, text_rect)


while True:
    display_surface.fill(white)

    draw_loose_screen(X, Y)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
