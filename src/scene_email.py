from src.scene import Scene
import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.parameters import *
from src.ui import ButtonChangeEmail, ButtonAcceptBooking, ButtonDeclineBooking, Email, Calendar, Marker, ButtonCalendarMarker

class SceneEmail(Scene):
    """Representa un escena abstracta del videojuego.
 
    Una escena es una parte visible del juego, como una pantalla
    de presentación o menú de opciones. Tiene que crear un objeto
    derivado de esta clase para crear una escena utilizable."""
 
    def __init__(self):
        self.next = None # no se toca hasta que toca cambiar de escena, entonces el director lo nota y cambia
        self.background = load_image("assets/images/scenes/email_background.png")
        # Email
        self.emails = [
            Email("Quiero LA habitación", "Hannibal", "Pos eso colega, que me des la habitación o lloro"),
            Email("Yo también quiero LA habitación", "Hannibal2", "Pos eso colega, que me des la habitación o te mato")
        ]
        
        self.current_email = self.emails[0]
        self.mouse_state = 1 # Up
        self.buttons = [
            ButtonChangeEmail(LOCATION_BUTTON_CHANGE_EMAIL_1, "Juancho", False, self.emails[0], lambda: self.change_email(0)),
            #ButtonChangeEmail(LOCATION_BUTTON_CHANGE_EMAIL_2, "Josefa", True, self.emails[1], lambda: self.change_email(1)),
            ButtonAcceptBooking(LOCATION_BUTTON_ACCEPT_BOOKING, "jaja"),
            ButtonDeclineBooking(LOCATION_BUTTON_DECLINE_BOOKING, "jwejwe")
        ]

        # Calendar
        self.calendar = Calendar(LOCATION_CALENDAR)
        self.current_month = 0

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
        #screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo
        screen.blit(self.background, self.background.get_rect())
        # Buttons
        for button in self.buttons:
            button.on_draw(screen)
        self.current_email.on_draw(screen)

    def finish(self, data):
        pass

    def assign_next_scene(self, next_scene):
        self.next = next_scene

    def change_email(self, index):
        self.current_email = self.emails[index]

    def book(self, week):
        self.calendar.bookings[self.current_month][week] = not self.calendar.bookings[self.current_month][week]