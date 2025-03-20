import pygame
import os

pygame.init()
pygame.mixer.init()

music_tracks = ['Anosognosia.mp3', 'Clockwork birds.mp3', 'Murmurations.mp3']
current_track_index = 0

pygame.mixer.music.load(music_tracks[current_track_index])

# Set up the display
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Simple Music Player")

# Function to play music
def play_music():
    pygame.mixer.music.play()

# Function to stop music
def stop_music():
    pygame.mixer.music.stop()

# Function to play the next track
def next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(music_tracks)
    pygame.mixer.music.load(music_tracks[current_track_index])
    play_music()

# Function to play the previous track
def previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(music_tracks)
    pygame.mixer.music.load(music_tracks[current_track_index])
    play_music()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard controls
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                play_music()
            elif event.key == pygame.K_s:  # Stop
                stop_music()
            elif event.key == pygame.K_n:  # Next
                next_track()
            elif event.key == pygame.K_b:  # Previous
                previous_track()

    # Clear the screen
    screen.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render("Controls: P=Play, S=Stop, N=Next, B=Previous", True, (0, 0, 0))
    screen.blit(text, (20, 80))

    pygame.display.flip()

pygame.quit()