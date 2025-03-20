import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 700))
clock = pygame.time.Clock()
Larm = pygame.image.load('leftarm.png')
Rarm = pygame.image.load("rightarm.png")
Clockvar = pygame.image.load("clock.png")

def blitRotate(surf, image, pos, angle):
    w, h = image.get_size()
    originPos = w / 2, h / 2
    image_rect = image.get_rect(center=pos)
    rotated_image = pygame.transform.rotate(image, angle)
    rotated_image_rect = rotated_image.get_rect(center=image_rect.center)
    surf.blit(rotated_image, rotated_image_rect)

angle1 = 0  # seconds hand
angle2 = 0  # minutes hand
done = False
start_time = time.time()

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Get current time
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    # Calculate angles
    angle1 = -6 * seconds 
    angle2 = -6 * minutes 

    pos = (screen.get_width() / 2, screen.get_height() / 2)

    screen.fill((255, 255, 255))  # Fill the screen with white
    screen.blit(Clockvar, (pos[0] - Clockvar.get_width() / 2, pos[1] - Clockvar.get_height() / 2))  # Draw clock face
    blitRotate(screen, Larm, pos, angle1)  # Draw seconds hand
    blitRotate(screen, Rarm, pos, angle2)  # Draw minutes hand

    pygame.display.flip()

pygame.quit()
exit()