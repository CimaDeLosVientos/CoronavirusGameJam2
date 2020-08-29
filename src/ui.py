from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *


class Icon(sprite.Sprite):
    def __init__(self, image, position):
        sprite.Sprite.__init__(self)
        self.image = image
        self.x = position[0]
        self.y = position[1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def on_draw(self, screen):
        screen.blit(self.image, self.rect)

class Button(sprite.Sprite):
    def __init__(self, image, hover, position, on_click):
        sprite.Sprite.__init__(self)
        self.image = image
        self.hover = hover
        self.x = position[0]
        self.y = position[1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.on_click = on_click

    def on_draw(self, screen):
        screen.blit(self.image, self.rect)




class ButtonEmail(Button):
    def __init__(self, position, on_click):
        super(ButtonEmail, self).__init__(
            image = load_image("assets/images/buttons/button_email.png"),
            hover = None,
            position = position,
            on_click = on_click)
        

class ButtonReview(Button):
    def __init__(self, position, on_click):
        super(ButtonReview, self).__init__(
            image = load_image("assets/images/buttons/button_review.png"),
            hover = None,
            position = position,
            on_click = on_click)
        


class ButtonBooking(Button):
    def __init__(self, position, on_click):
        super(ButtonBooking, self).__init__(
            image = load_image("assets/images/buttons/button_booking.png"),
            hover = None,
            position = position,
            on_click = on_click)
        


class ButtonUpgrades(Button):
    def __init__(self, position, on_click):
        super(ButtonUpgrades, self).__init__(
            image = load_image("assets/images/buttons/button_upgrades.png"),
            hover = None,
            position = position,
            on_click = on_click)


# Email Scene

class ButtonChangeEmail(Button):
    def __init__(self, position, user_name, vip, email, on_click):
        super(ButtonChangeEmail, self).__init__(
            image = load_image("assets/images/buttons/button_change_email_vip.png") if vip else load_image("assets/images/buttons/button_change_email.png"),
            hover = None,
            position = position,
            on_click = on_click)
        self.user_name = user_name
        self.email = email

    def on_draw(self, screen):
        super().on_draw(screen)
        position = (self.x + DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL[0],
                    self.y + DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL[1])
        image, rect = draw_text(self.user_name, position, size = 25, color = (0, 0, 255))
        screen.blit(image, rect)


class ButtonAcceptBooking(Button):
    def __init__(self, position, on_click):
        super(ButtonAcceptBooking, self).__init__(
            image = load_image("assets/images/buttons/button_accept_booking.png"),
            hover = None,
            position = position,
            on_click = on_click)

class ButtonDeclineBooking(Button):
    def __init__(self, position, on_click):
        super(ButtonDeclineBooking, self).__init__(
            image = load_image("assets/images/buttons/button_decline_booking.png"),
            hover = None,
            position = position,
            on_click = on_click)




class Email(sprite.Sprite):
    def __init__(self, text_subject, text_sender, text_body):
        self.image = load_image("assets/images/sprites/email_content.png")
        self.x = LOCATION_EMAIL_CONTENT[0]
        self.y = LOCATION_EMAIL_CONTENT[1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.text_subject = text_subject
        self.text_sender = text_sender
        self.text_body = text_body

    def on_draw(self, screen):
        screen.blit(self.image, self.rect)
        position_text_subject = (LOCATION_EMAIL_TEXT_SUBJECT[0],
                                 LOCATION_EMAIL_TEXT_SUBJECT[1])
        position_text_sender  = (LOCATION_EMAIL_TEXT_SENDER[0],
                                 LOCATION_EMAIL_TEXT_SENDER[1])
        position_text_body    = (LOCATION_EMAIL_TEXT_BODY[0],
                                 LOCATION_EMAIL_TEXT_BODY[1])
        image, rect = draw_text(self.text_subject, position_text_subject, size = 25, color = (0, 0, 255))
        screen.blit(image, rect)
        image, rect = draw_text(self.text_sender, position_text_sender, size = 25, color = (0, 0, 255))
        screen.blit(image, rect)
        image, rect = draw_text(self.text_body, position_text_body, size = 25, color = (0, 0, 255))
        screen.blit(image, rect)


## Calendar
class Marker(Icon):
    def __init__(self, position):
        super(Marker, self).__init__(
            image = load_image("assets/images/sprites/marker.png"),
            position = position)


class Calendar(sprite.Sprite):
    def __init__(self, position):
        self.image = load_image("assets/images/buttons/beer.png")
        self.x = position[0]
        self.y = position[1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.bookings = [[False]*4]*12
        self.current_month = 0
        self.markeds = [
            Marker((self.x + DISPLACEMENT_CALENDAR_MARKER_0[0],
                    self.y + DISPLACEMENT_CALENDAR_MARKER_0[1])),
            Marker((self.x + DISPLACEMENT_CALENDAR_MARKER_1[0],
                    self.y + DISPLACEMENT_CALENDAR_MARKER_1[1])),
            Marker((self.x + DISPLACEMENT_CALENDAR_MARKER_2[0],
                    self.y + DISPLACEMENT_CALENDAR_MARKER_2[1])),
            Marker((self.x + DISPLACEMENT_CALENDAR_MARKER_3[0],
                    self.y + DISPLACEMENT_CALENDAR_MARKER_3[1])),
        ]

    def previous_month(self):
        self.current_month = (self.current_month + 1) % 12

    def next_month(self):
        self.current_month = (self.current_month - 1) % 12

    def on_draw(self, screen):
        screen.blit(self.image, self.rect)
        for mount in self.bookings:
            for i in range(4):
                if mount[i]:
                    self.markeds[i].on_draw(screen)

        image, rect = draw_text(self.user_name, position, size = 25, color = (0, 0, 255))
        screen.blit(image, rect)
        image, rect = draw_text(self.user_name, position, size = 25, color = (0, 0, 255))
        screen.blit(image, rect)


class ButtonCalendarMarker(Button):
    def __init__(self, position, on_click):
        super(ButtonCalendarMarker, self).__init__(
            image = load_image("assets/images/sprites/marker.png"),
            hover = None,
            position = position,
            on_click = on_click)

    def switch(self):
        self.image = load_image("assets/images/buttons/beer.png")

