from src.scene import Scene
import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.parameters import *
from src.ui import ButtonEmail, ButtonReview ,ButtonBooking, ButtonUpgrades

class SceneOffice(Scene):
    """Representa un escena abstracta del videojuego.
 
    Una escena es una parte visible del juego, como una pantalla
    de presentación o menú de opciones. Tiene que crear un objeto
    derivado de esta clase para crear una escena utilizable."""
 
    def __init__(self):
        self.next = None # no se toca hasta que toca cambiar de escena, entonces el director lo nota y cambia
        #self.title
        self.sound_notification = load_sound("assets/sounds/notification.wav")
        self.background = load_image("assets/images/scenes/pc_background.png")
        self.mouse_state = 1 # Up
        self.buttons = [
            ButtonPC(LOCATION_BUTTON_PC, lambda: self.assign_next_scene("pc")),
            ButtonBlind(LOCATION_BUTTON_NEXT_DAY, lambda: self.end_week())
        ]

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
        screen.blit(self.background, self.background.get_rect())
        # Buttons
        for button in self.buttons:
            button.on_draw(screen)


    def finish(self, data):
        pass

    def assign_next_scene(self, next_scene):
        self.next = next_scene

    def end_week(self):
        # Bajar persiana
        # Actualizar variables del master
        # Subir persiana