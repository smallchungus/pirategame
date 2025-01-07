from settings import *
from sprites import Sprite

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.all_sprites = pygame.sprite.Group()

        self.setup(tmx_map)

    def setup(self, tmx_map):
        for x, y, surf in tmx_map.get_layer_by_name('Terrain').tiles():
            print(x)
            print(y)
            print(surf)

    def run(self):
        self.display_surface.fill('red')

