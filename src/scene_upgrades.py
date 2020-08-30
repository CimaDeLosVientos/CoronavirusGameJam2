from src.scene import Scene
import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.parameters import *
from src.ui import *

class SceneUpgrades(Scene):
    """Representa un escena abstracta del videojuego.
 
    Una escena es una parte visible del juego, como una pantalla
    de presentación o menú de opciones. Tiene que crear un objeto
    derivado de esta clase para crear una escena utilizable."""
 
    def __init__(self, game_master):
        self.game_master = game_master
        self.next = None # no se toca hasta que toca cambiar de escena, entonces el director lo nota y cambia
        self.music = "assets/music/music.mp3"
        self.background = load_image("assets/images/scenes/background_upgrades2.png")

        self.buttons = [
            ButtonClose(LOCATION_BUTTON_CLOSE, lambda: self.assign_next_scene("pc")),
            ButtonClose(LOCATION_BUTTON_CLOSE, lambda: self.assign_next_scene("pc")),
        ]
        self.mouse_state = 1 # Up


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
            for button in (self.buttons):
                if button.rect.collidepoint(mouse_pos):
                    button.on_click()
            self.mouse_state = 1



    def on_update(self, time):
        pass
 
    def on_draw(self, screen):
        # Clear the screen
        #screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo
        screen.blit(self.background, self.background.get_rect())
        # Buttons


        for button in self.buttons:
            button.on_draw(screen)


    def finish(self, data):
        pass

    def assign_next_scene(self, next_scene):
        self.next = next_scene
