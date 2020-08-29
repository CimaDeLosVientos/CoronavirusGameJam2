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
 
    def __init__(self, clients):
        self.next = None # no se toca hasta que toca cambiar de escena, entonces el director lo nota y cambia
        self.background = load_image("assets/images/scenes/email_background.png")

        # Email
        self.buttons_emails = self.generate_emails()

        
        self.current_email = None # index

        # Calendar
        self.calendar = Calendar()
        self.current_month = 0



        self.mouse_state = 1 # Up
        self.buttons = [
            ButtonAcceptBooking(lambda: self.accept_booking()),
            ButtonDeclineBooking(lambda: self.remove_email()),
            ButtonNextMonth(lambda: self.remove_email())
            ButtonPreviousMonth(lambda: self.calendar.previous_month())
            ButtonCalendarMarker(lambda: self.calendar.next_month())
            ButtonCalendarMarker("on_click")
            ButtonCalendarMarker("on_click")
            ButtonCalendarMarker("on_click")
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
        #screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo
        screen.blit(self.background, self.background.get_rect())
        # Buttons
        self.current_email.on_draw(screen)
        for button in self.buttons + self.buttons_emails:
            button.on_draw(screen)

    def finish(self, data):
        pass

    def assign_next_scene(self, next_scene):
        self.next = next_scene


    def generate_emails(self):
        buttons = []
        # Ver que pollos quieren reservar
        # if pollo.booking:
        #     email = Email(Texto, texto, texto)
        #     buttons.append(ButtonChangeEmail(index,
        #                   pollo.name,
        #                   pollo.vip,
        #                   lambda: self.change_email(index)),
        self.emails = [
            Email("Quiero LA habitación", "Hannibal", "Pos eso colega, que me des la habitación o lloro"),
            Email("Yo también quiero LA habitación", "Hannibal2", "Pos eso colega, que me des la habitación o te mato")
        ]
        buttons.append(ButtonChangeEmail(0, "Juancho", False, self.emails[0], lambda: self.change_email(0)))
        buttons.append(ButtonChangeEmail(1, "Josefa", True, self.emails[1], lambda: self.change_email(1)))
        return [random.choice(buttons) for i in range(min(len(buttons), MAX_EMAILS))]

    def change_email(self, email_index):
        self.current_email = self.buttons_emails[email_index].email

    def marker_week(self, week):
        self.calendar.bookings[self.current_month][week] = not self.calendar.bookings[self.current_month][week]



    def accept_booking(self):
        # Añadir a los datos esta reserva
        self.remove_email(self.current_email)

    def remove_email(self):
        self.buttons_emails.pop(self.current_email)
        i = 0
        for button_email in self.buttons_emails:
            button_email.index = i
            i += 1
            