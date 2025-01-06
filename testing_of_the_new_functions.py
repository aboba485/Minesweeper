import pygame

pygame.init()

# Define colors
white = (255, 255, 255)
green = (0, 255, 0)

# Screen dimensions
X = 800
Y = 400

# Create display surface
display_surface = pygame.display.set_mode((X, Y))

# Set window caption
pygame.display.set_caption('Show Text')

# Function to draw the timer
def draw_a_counter_of_the_time(minutes, seconds, screen, text_color):
    font_for_clock = pygame.font.Font(None, 36)
    text = font_for_clock.render(f"min: {minutes} sec: {seconds}", True, text_color)
    screen.blit(text, (280, 0))

# Get the starting tick count
start_ticks = pygame.time.get_ticks()
running = True  # Variable to track if the timer is running
elapsed_time = 0  # Store the total elapsed time

# Main game loop
while True:
    display_surface.fill(white)  # Clear the screen

    # Calculate the elapsed time only if the timer is running
    if running:
        current_ticks = pygame.time.get_ticks() - start_ticks
        elapsed_time = current_ticks // 1000
        seconds = elapsed_time % 60
        minutes = elapsed_time // 60
    else:
        # Keep the last calculated time
        seconds = elapsed_time % 60
        minutes = elapsed_time // 60

    # Draw the timer
    draw_a_counter_of_the_time(minutes, seconds, display_surface, green)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                running = not running  # Toggle the running state

    # Update the display
    pygame.display.update()
