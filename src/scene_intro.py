from src.scene import Scene
import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.parameters import *
from src.ui import *

class SceneIntro(Scene):
    def __init__(self):
        Scene.__init__(self)
        self.next = None
        self.persiana_sube = True
        self.fade = False
        self.changing = False
        self.alpha = 255

        self.music = "assets/music/Phillip_Gross_-_02_-_Neon_Twin.mp3"
        self.background_persiana = load_image("assets/images/scenes/background_menu_2.png")
        self.rect_background_persiana = self.background_persiana.get_rect()

        self.background_blurry = load_image("assets/images/scenes/background_game_blurry.png")
        self.background_clear = load_image("assets/images/scenes/background_game_clear.png")

        self.buttons = [
            ButtonPlay(lambda: self.assign_next_scene())
        ]
        self.mouse_state = 1 # Up




    def load(self, data):
        self.next = None



    def on_event(self, time, event):
        if self.persiana_sube or self.fade:
            return
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
        #import pdb; pdb.set_trace()
        if self.persiana_sube:
            self.rect_background_persiana.y -= time * NEXT_WEEK_SPEED
            if self.rect_background_persiana.y <= -self.rect_background_persiana.height:
                self.persiana_sube = False
                self.fade = True
        
        if self.fade:
            self.alpha -= 4
            if self.alpha <= 0:
                self.fade = False

        if self.changing:
            self.next = "office"


 
    def on_draw(self, screen):
        # Clear the screen
        if self.persiana_sube:
            screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo
            screen.blit(self.background_persiana, self.rect_background_persiana)
            return

        if self.fade:
            screen.blit(self.background_clear, self.background_clear.get_rect())
            jaja = pygame.Surface((self.background_clear.get_rect().width, self.background_clear.get_rect().height))
            jaja.fill((0, 0, 0))
            jaja.set_alpha(self.alpha)
            screen.blit(jaja, (0,0))

            return

        if self.changing:
            screen.blit(self.background_blurry, self.background_blurry.get_rect())
            return

        screen.blit(self.background_clear, self.background_clear.get_rect())
        # Buttons
        for button in self.buttons:
            button.on_draw(screen)




    def finish(self, data):
        tim.sleep(3)

    def assign_next_scene(self):
        self.changing = True