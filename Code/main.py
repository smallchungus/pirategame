from settings import *
from level import Level
from pytmx.util_pygame import load_pygame
from os.path import join


class Game:
    def __init__(self):
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT ))
        pygame.display.set_caption('Super Pirate World')

        self.tmx_maps = {0: load_pygame(join('..', 'data', 'levels', 'omni.tmx'))}

        self.current_stage = Level(self.tmx_maps[0])

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.current_stage.run()
            pygame.display.update()

if __name__ == '__main__':
    game = Game()
    game.run()

