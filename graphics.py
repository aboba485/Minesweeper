import pygame

def counter_of_the_time(start_ticks):
    elapsed_ticks = pygame.time.get_ticks() - start_ticks
    seconds = (elapsed_ticks // 1000) % 60
    minutes = (elapsed_ticks // 1000) // 60
    return f"min: {minutes} sec: {seconds}"

pygame.init()

screen = pygame.display.set_mode((680, 480))
pygame.display.set_caption('MineSweeper')
running = True

white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 36)

start_ticks = pygame.time.get_ticks()

while running:
    screen.fill(white)

    text = font.render(counter_of_the_time(start_ticks), True, black)
    screen.blit(text, (250, 200))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
