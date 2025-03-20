import pygame

def do_nice_outlines(surface):
    color = (0, 255, 0)  # green
    # draw a rectangle
    pygame.draw.rect(surface, color, pygame.Rect(0, -9, 600, 10))
    pygame.draw.rect(surface, color, pygame.Rect(-9, 1, 10, 600))
    pygame.draw.rect(surface, color, pygame.Rect(599, 1, 10, 599))
    pygame.draw.rect(surface, color, pygame.Rect(0, 599, 600, 10))

pygame.init()
screen = pygame.display.set_mode((600, 600))  # resolution
done = False  # for while loop in game
x = 300  # starting position on x/y axis
y = 300

clock = pygame.time.Clock()  # store ticks
radius = 25  # radius of the ball

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Exiting
            done = True

    pressed = pygame.key.get_pressed()  # Movement
    if pressed[pygame.K_UP] and y - radius > 0:  # Check upper boundary
        y -= 20
    if pressed[pygame.K_DOWN] and y + radius < 600:  # Check lower boundary
        y += 20
    if pressed[pygame.K_LEFT] and x - radius > 0:  # Check left boundary
        x -= 20
    if pressed[pygame.K_RIGHT] and x + radius < 600:  # Check right boundary
        x += 20

    screen.fill((255, 255, 255))  # filling white
    color = (255, 0, 0)  # red color
    pygame.draw.circle(screen, color, (x, y), radius)  # Draw the ball
    do_nice_outlines(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()