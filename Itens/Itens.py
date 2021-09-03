import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("graphics/key.png").convert_alpha()
        self.rect = self.image.get_rect()

class KeyItem(Item):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("graphics/key.png").convert_alpha()
        self.rect = self.image.get_rect()