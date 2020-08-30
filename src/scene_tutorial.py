from src.scene import Scene
import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.parameters import *
from src.ui import *

class SceneTutorial(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.next = None
        self.music = "assets/music/Phillip_Gross_-_02_-_Neon_Twin.mp3"
        self.background_1 = load_image("assets/images/scenes/background_menu_1.png")

        self.buttons = [
            ButtonPlay(lambda: self.assign_next_scene("main_menu"))
        ]


        self.mouse_state = 1 # Up


    def load(self, data):
        pass


    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        if (mouse_press and self.mouse_state == 1):
            self.mouse_state = 0
        if (not mouse_press and self.mouse_state == 0):
            for button in self.buttons:
                if button.rect.collidepoint(mouse_pos):
                    button.on_click()
            self.mouse_state = 1

    def on_update(self, time):
        pass
 
    def on_draw(self, screen):
        # Clear the screen
        screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo
        screen.blit(self.background_1, self.background_1.get_rect())
        # Buttons
        for button in self.buttons:
            button.on_draw(screen)


    def finish(self, data):
        pass

    def assign_next_scene(self, next_scene):
        self.next = next_scene