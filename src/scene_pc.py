from src.scene import Scene
import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.parameters import *
from src.ui import ButtonEmail, ButtonReview ,ButtonBooking, ButtonUpgrades, ButtonClose

class ScenePC(Scene):
    """Representa un escena abstracta del videojuego.
 
    Una escena es una parte visible del juego, como una pantalla
    de presentación o menú de opciones. Tiene que crear un objeto
    derivado de esta clase para crear una escena utilizable."""
 
    def __init__(self, game_master):
        self.game_master = game_master
        self.next = None # no se toca hasta que toca cambiar de escena, entonces el director lo nota y cambia
        self.music = "assets/music/music.mp3"
        #self.title
        self.sound_notification = load_sound("assets/sounds/notification.wav")
        self.background = load_image("assets/images/scenes/pc_background.png")
        self.mouse_state = 1 # Up
        self.buttons = [
            ButtonEmail(LOCATION_BUTTON_EMAIL, lambda: self.assign_next_scene("email")),
            ButtonReview(LOCATION_BUTTON_REVIEW, lambda: self.sound_notification.play()),
            ButtonBooking(LOCATION_BUTTON_BOOKING, lambda: self.assign_next_scene("booking")),
            ButtonUpgrades(LOCATION_BUTTON_UPGRADES, lambda: self.assign_next_scene("upgrades")),
            ButtonClose(LOCATION_BUTTON_CLOSE_2, lambda: self.assign_next_scene("office"))
        ]

    def load(self, data):
        if not pygame.mixer.music.get_busy():
            load_music(self.music)
            pygame.mixer.music.play(-1) 
        self.next = None

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
        #screen.blit(self.button_email.image, self.button_email.rect)
        #screen.blit(self.button_review.image, self.button_review.rect)
        #screen.blit(self.button_booking.image, self.button_booking.rect)
        #screen.blit(self.button_x.image, self.button_x.rect)

    def finish(self, data):
        pass

    def assign_next_scene(self, next_scene):
        self.next = next_scene