from pygame import sprite, transform
from pygame.locals import *
from .helpers import *
from .parameters import *

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
            image = transform.scale(load_image("assets/images/sprites/beer.png"), OBJECT_SURFACE),
            hover = None,
            position = position,
            on_click = on_click)
        

class ButtonReview(Button):
    def __init__(self, position, on_click):
        super(ButtonReview, self).__init__(
            image = transform.scale(load_image("assets/images/sprites/beer.png"), OBJECT_SURFACE),
            hover = None,
            position = position,
            on_click = on_click)
        


class ButtonBooking(Button):
    def __init__(self, position, on_click):
        super(ButtonBooking, self).__init__(
            image = transform.scale(load_image("assets/images/sprites/beer.png"), OBJECT_SURFACE),
            hover = None,
            position = position,
            on_click = on_click)
        


class ButtonX(Button):
    def __init__(self, position, on_click):
        super(ButtonX, self).__init__(
            image = transform.scale(load_image("assets/images/sprites/beer.png"), OBJECT_SURFACE),
            hover = None,
            position = position,
            on_click = on_click)


# Email Scene

class ButtonChangeEmail(Button):
    def __init__(self, position, on_click):
        super(ButtonChangeEmail, self).__init__(
            image = transform.scale(load_image("assets/images/sprites/beer.png"), OBJECT_SURFACE),
            hover = None,
            position = position,
            on_click = on_click)


class Email():
    def __init__(self, position):
        self.image = transform.scale(load_image("assets/images/sprites/beer.png"), OBJECT_SURFACE)
        self.x = position[0]
        self.y = position[1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def on_draw(self, screen):
        screen.blit(self.image, self.rect)
        # Aqui hay que poner los textos usando posiciones relativas al objeto

class Email2():
    def __init__(self, position):
        self.image = transform.scale(load_image("assets/images/sprites/steak.png"), OBJECT_SURFACE)
        self.x = position[0]
        self.y = position[1]
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def on_draw(self, screen):
        screen.blit(self.image, self.rect)
        # Aqui hay que poner los textos usando posiciones relativas al objeto