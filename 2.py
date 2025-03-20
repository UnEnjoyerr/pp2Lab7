import pygame
import os
pygame.init()
pygame.mixer.init()

music_tracks = ['Anosognosia.mp3', 'Clockwork birds.mp3', 'Murmurations.mp3']
current_track_index = 0

pygame.mixer.music.load(music_tracks[current_track_index])


screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Simple Music Player")

play_button = pygame.image.load('play.png')
stop_button = pygame.image.load('stop.png')
next_button = pygame.image.load('next.png')
previous_button = pygame.image.load('previous.png')

button_width = 100
button_height = 50

def draw_button(image, x, y):
    screen.blit(image, (x, y))

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_tracks)
    pygame.mixer.music.load(music_tracks[current_track_index])
    play_music()

def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_tracks)
    pygame.mixer.music.load(music_tracks[current_track_index])
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False

        # keyboard controlls
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_p]:
                play_music()
        if pressed[pygame.K_s]:
                stop_music()
        if pressed[pygame.K_n]:
                next_track()
        if pressed[pygame.K_b]:
                previous_track()
        # Check for mouse clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            
            if play_button.get_rect(topleft=(50, 50)).collidepoint(mouse_pos):
                play_music()
            if stop_button.get_rect(topleft=(200, 50)).collidepoint(mouse_pos):
                stop_music()
            if next_button.get_rect(topleft=(50, 150)).collidepoint(mouse_pos):
                next_track()
            if previous_button.get_rect(topleft=(200, 150)).collidepoint(mouse_pos):
                previous_track()

    screen.fill((0, 0, 0))  

    # Draw buttons
    draw_button(play_button, 50, 50)
    draw_button(stop_button, 200, 50)
    draw_button(next_button, 50, 150)
    draw_button(previous_button, 200, 150)
    pygame.display.flip()
pygame.quit()