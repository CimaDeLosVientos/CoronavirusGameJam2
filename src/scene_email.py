from src.scene import Scene
import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *
from src.parameters import *
from src.ui import *

class SceneEmail(Scene):
    """Representa un escena abstracta del videojuego.
 
    Una escena es una parte visible del juego, como una pantalla
    de presentación o menú de opciones. Tiene que crear un objeto
    derivado de esta clase para crear una escena utilizable."""
 
    def __init__(self, game_master):
        self.game_master = game_master
        self.next = None # no se toca hasta que toca cambiar de escena, entonces el director lo nota y cambia
        self.music = "assets/music/music.mp3"
        self.background = load_image("assets/images/scenes/email_background.png")
        self.update_week = -1
        # Email
        self.buttons_emails = self.generate_emails()
        self.buttons_answer_emails = [
            ButtonAcceptBooking(lambda: self.accept_booking()),
            ButtonDeclineBooking(lambda: self.remove_email())
        ]
        
        self.current_email = None # Object
        self.current_email_index = None

        # Calendar
        self.calendar = Calendar()



        self.mouse_state = 1 # Up
        self.buttons = [
            ButtonNextMonth(lambda: self.next_month()),
            ButtonPreviousMonth(lambda: self.previous_month()),
            ButtonClose(LOCATION_BUTTON_CLOSE, lambda: self.assign_next_scene("pc"))
        ]

        self.buttons_calendar_marker = [
            ButtonCalendarMarker(LOCATION_BUTTON_CALENDAR_MARKER_0, lambda: self.marker_week(0)),
            ButtonCalendarMarker(LOCATION_BUTTON_CALENDAR_MARKER_1, lambda: self.marker_week(1)),
            ButtonCalendarMarker(LOCATION_BUTTON_CALENDAR_MARKER_2, lambda: self.marker_week(2)),
            ButtonCalendarMarker(LOCATION_BUTTON_CALENDAR_MARKER_3, lambda: self.marker_week(3))
        ]

    def load(self, data):
        self.next = None
        if not pygame.mixer.music.get_busy():
            load_music(self.music)
            pygame.mixer.music.play(-1) 
        self.current_email_index = None
        self.current_email = None
        self.calendar.set_month = int(self.game_master.week / 4)
        print("jaja",self.calendar.set_month)
        if self.update_week == self.game_master.week:
            return
        self.buttons_emails = self.generate_emails()
        self.update_week = self.game_master.week

    def on_event(self, time, event):
        mouse_press = pygame.mouse.get_pressed()[0]
        mouse_pos = pygame.mouse.get_pos()
        if (mouse_press and self.mouse_state == 1):
            self.mouse_state = 0
        if (not mouse_press and self.mouse_state == 0):
            for button in (self.buttons + self.buttons_answer_emails
                           + self.buttons_calendar_marker):
                if button.rect.collidepoint(mouse_pos):
                    button.on_click()
            for button in self.buttons_emails:
                if button.rect.collidepoint(mouse_pos):
                    self.change_email(button.index)
            self.mouse_state = 1



    def on_update(self, time):
        pass
 
    def on_draw(self, screen):
        # Clear the screen
        #screen.fill((0, 0, 0)) ## Comprobar si lo puedo quitar porque es poner en blanco y en teoria lo voy a pintar todo
        screen.blit(self.background, self.background.get_rect())
        # Buttons
        if self.current_email:
            self.current_email.on_draw(screen)
            self.buttons_answer_emails[0].on_draw(screen)
            self.buttons_answer_emails[1].on_draw(screen)

        for button in self.buttons + self.buttons_emails + self.buttons_calendar_marker:
            button.on_draw(screen)

        self.calendar.on_draw(screen)

    def finish(self, data):
        pass

    def assign_next_scene(self, next_scene):
        self.next = next_scene


    def generate_emails(self):
        buttons = []
        index = 0
        for client, email in self.game_master.client_emails:
            buttons.append(ButtonChangeEmail(index,
                           client,
                           email,
                           None))  # Problems with references
            index += 1

        return buttons

    def change_email(self, email_index):
        self.current_email = self.buttons_emails[email_index].email
        self.current_email_index = email_index

    def marker_week(self, week):
        self.calendar.bookings[self.calendar.current_month][week] = not self.calendar.bookings[self.calendar.current_month][week]
        self.buttons_calendar_marker[week].switch()


    def update_calendar_marker_buttons(self):
        for i in range(4):
            state = self.calendar.bookings[self.calendar.current_month][i]
            self.buttons_calendar_marker[i].switch(state)

    def next_month(self):
        self.calendar.next_month()
        self.update_calendar_marker_buttons()
    
    def previous_month(self):
        self.calendar.previous_month()
        self.update_calendar_marker_buttons()

    def accept_booking(self):
        self.game_master.accept_booking(self.buttons_emails[self.current_email_index].client)
        self.remove_email()

    def remove_email(self):
        self.buttons_emails.pop(self.current_email_index)
        i = 0
        for button_email in self.buttons_emails:
            button_email.index = i
            i += 1
        self.current_email = None
            