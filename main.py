import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *

from src.parameters import *
from src.game_master import GameMaster
from src.scene_office import SceneOffice
from src.scene_pc import ScenePC
from src.scene_email import SceneEmail
from src.main_menu import MainMenu
from src.scene_intro import SceneIntro
from src.scene_credits import SceneCredits
from src.scene_tutorial import SceneTutorial
from src.scene_booking import SceneBooking
from src.scene_upgrades import SceneUpgrades



class Director:
    """Representa el objeto principal del juego.

    El objeto Director mantiene en funcionamiento el juego, se
    encarga de actualizar, dibuja y propagar eventos.

    Tiene que utilizar este objeto en conjunto con objetos
    derivados de Scene."""

    def __init__(self, scenes, data):
        # Display
        self.fullscream = False
        if RESOLUTION_1080:
            self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
            #self.screen = pygame.display.set_mode([WIDTH, HEIGHT], flags = pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode([int(WIDTH / 1.5), int(HEIGHT / 1.5)])
            #self.screen = pygame.display.set_mode([int(WIDTH / 1.5), int(HEIGHT / 1.5)], flags = pygame.FULLSCREEN)

        # Screen name
        pygame.display.set_caption("La Suite")

        # Icon
        #icon = load_image("assets/images/bobi_icon.png")
        #pygame.display.set_icon(icon)
        # Variables
        self.clock = pygame.time.Clock()
        self.quit_flag = False

        #Options
        pygame.key.set_repeat(10)
        pygame.mixer.music.set_volume(MASTER_VOLUMEN)

        self.scenes = scenes
        self.current_scene = self.scenes["init"]
        self.data = data

    def presentation_screen(self, path):
        screen_image = load_image(path)
        self.screen.blit(screen_image, screen_image.get_rect())
        pygame.display.flip()

    def run(self):
        self.current_scene = self.scenes["init"]
        self.current_scene.load(self.data) # Se le manda el diccionario de datos para que se configure.
        while not self.quit_flag:
            time = self.clock.tick(60) # Must be in loop
            # Eventos de Salida
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.quit()
                    if event.key == pygame.K_p:
                        if self.fullscream:
                            if RESOLUTION_1080:
                                self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
                            else:
                                self.screen = pygame.display.set_mode([int(WIDTH / 1.5), int(HEIGHT / 1.5)])

                        else:
                            if RESOLUTION_1080:
                                self.screen = pygame.display.set_mode([WIDTH, HEIGHT], flags = pygame.FULLSCREEN)
                            else:
                                self.screen = pygame.display.set_mode([int(WIDTH / 1.5), int(HEIGHT / 1.5)], flags = pygame.FULLSCREEN)
                        self.fullscream = not self.fullscream

                # detecta eventos
                self.current_scene.on_event(time, event)
            # actualiza la escena
            self.current_scene.on_update(time)

            # dibuja la pantalla
            self.current_scene.on_draw(self.screen)
            pygame.display.flip()

            if self.current_scene.next:
                self.change_scene()

    def change_scene(self):
        self.current_scene.finish(self.data) # Se le manda el diccionario de datos para que lo actualice.
        self.current_scene = self.scenes[self.current_scene.next]
        self.current_scene.load(self.data) # Se le manda el diccionario de datos para que se configure.

    def quit(self):
        self.quit_flag = True

    #s = pygame.Surface((1000,750))  # the size of your rect
    #s.set_alpha(128)                # alpha level
    #s.fill((255,255,255))           # this fills the entire surface
    #screen.blit(s, (0,0))


if __name__ == '__main__':
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.mixer.init()
    pygame.init()

    scenes = {"init" : None}
    data = {}
    director = Director(scenes, data)
    director.presentation_screen("assets/images/presentation_screen.png")
    game_master = GameMaster()

    data = {
    }
    scenes = {
        "init" : MainMenu(),
        "main_menu" : MainMenu(),
        "intro" : SceneIntro(),
        "office" : SceneOffice(game_master),
        "pc" : ScenePC(game_master),
        "email": SceneEmail(game_master),
        "credits" : SceneCredits(),
        "tutorial" : SceneTutorial(),
        "booking" : SceneBooking(game_master),
        "upgrades" : SceneUpgrades(game_master)
    }
    
    director.data = data
    director.scenes = scenes
    director.run()