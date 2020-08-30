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

# Office
class ButtonPC(Button):
    def __init__(self, on_click):
        super(ButtonPC, self).__init__(
            image = load_image("assets/images/buttons/button_pc.png"),
            hover = None,
            position = LOCATION_BUTTON_PC,
            on_click = on_click)


class ButtonNextWeek(Button):
    def __init__(self, on_click):
        super(ButtonBlind, self).__init__(
            image = load_image("assets/images/buttons/button_next_week.png"),
            hover = None,
            position = LOCATION_BUTTON_NEXT_DAY,
            on_click = on_click)





# PC
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
    def __init__(self, index, user_name, vip, email, on_click):
        super(ButtonChangeEmail, self).__init__(
            image = load_image("assets/images/buttons/button_change_email_vip.png") if vip else load_image("assets/images/buttons/button_change_email.png"),
            hover = None,
            position = LOCATION_BUTTON_CHANGE_EMAIL,
            on_click = on_click)
        self.index = index
        self.change_index(self.index)
        self.user_name = user_name
        self.email = email

    def change_index(self, new_index):
        self.index = new_index
        self.y = LOCATION_BUTTON_CHANGE_EMAIL[1] + self.index * DISPLACEMENT_BUTTON_CHANGE_EMAIL[1]
        self.rect.center = (self.x, self.y)

    def on_draw(self, screen):
        super().on_draw(screen)
        position = (self.x + DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL[0],
                    self.y + DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL[1])
        image, rect = draw_text(self.user_name, position, size = SIZE_TEXT_USER_NAME, color = (0, 0, 0))
        screen.blit(image, rect)


class ButtonAcceptBooking(Button):
    def __init__(self, on_click):
        super(ButtonAcceptBooking, self).__init__(
            image = load_image("assets/images/buttons/button_accept_booking.png"),
            hover = None,
            position = LOCATION_BUTTON_ACCEPT_BOOKING,
            on_click = on_click)

class ButtonDeclineBooking(Button):
    def __init__(self, on_click):
        super(ButtonDeclineBooking, self).__init__(
            image = load_image("assets/images/buttons/button_decline_booking.png"),
            hover = None,
            position = LOCATION_BUTTON_DECLINE_BOOKING,
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
        
        image, rect = draw_text(
            self.text_subject,
            LOCATION_EMAIL_TEXT_SUBJECT,
            size = SIZE_TEXT_SUBJECT,
            color = (0, 0, 0))
        screen.blit(image, rect)

        
        image, rect = draw_text(
            self.text_sender,
            LOCATION_EMAIL_TEXT_SENDER,
            size = SIZE_TEXT_SENDER,
            color = (0, 0, 0))
        screen.blit(image, rect)

        image, rect = draw_text(
            self.text_body,
            LOCATION_EMAIL_TEXT_BODY,
            size = SIZE_TEXT_BODY,
            color = (0, 0, 0))
        screen.blit(image, rect)


## Calendar
class Marker(Icon):
    def __init__(self, position):
        super(Marker, self).__init__(
            image = load_image("assets/images/sprites/marker.png"),
            position = position)


class Calendar(sprite.Sprite):
    def __init__(self):
        self.images = [load_image(
                        "assets/images/sprites/calendar_month_{}.png".format(
                            i + 1)) for i in range(12)]
        self.image = self.images[0]
        self.x = LOCATION_CALENDAR[0]
        self.y = LOCATION_CALENDAR[1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.bookings = [[False for i in range(4)] for ii in range(12)]
        self.current_month = 0
        self.markeds = [
            Marker(LOCATION_CALENDAR_MARKER_0),
            Marker(LOCATION_CALENDAR_MARKER_1),
            Marker(LOCATION_CALENDAR_MARKER_2),
            Marker(LOCATION_CALENDAR_MARKER_3)
        ]

    def previous_month(self):
        self.current_month = (self.current_month - 1) % 12
        self.image = self.images[self.current_month]

    def next_month(self):
        self.current_month = (self.current_month + 1) % 12
        self.image = self.images[self.current_month]

    def on_draw(self, screen):
        screen.blit(self.image, self.rect)
        for i in range(4):
            if self.bookings[self.current_month][i]:
                self.markeds[i].on_draw(screen)


class ButtonNextMonth(Button):
    def __init__(self, on_click):
        super(ButtonNextMonth, self).__init__(
            image = load_image("assets/images/buttons/button_next_calendar.png"),
            hover = None,
            position = LOCATION_BUTTON_NEXT_MONTH,
            on_click = on_click)


class ButtonPreviousMonth(Button):
    def __init__(self, on_click):
        super(ButtonPreviousMonth, self).__init__(
            image = load_image("assets/images/buttons/button_previous_calendar.png"),
            hover = None,
            position = LOCATION_BUTTON_PREVIOUS_MONTH,
            on_click = on_click)



class ButtonCalendarMarker(Button):
    def __init__(self, position, on_click):
        super(ButtonCalendarMarker, self).__init__(
            image = load_image("assets/images/buttons/button_calendar_marker_off.png"),
            hover = None,
            position = position,
            on_click = on_click)
        self.images = [self.image,
                       load_image("assets/images/buttons/button_calendar_marker_on.png")]
        self.state = False

    def switch(self, target = None):
        self.state = not self.state if target is None else target
        self.image = self.images[1] if self.state else self.images[0]

