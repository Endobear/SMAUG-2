import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("graphics/key.png").convert_alpha()
        self.icon = self.image
        self.rect = self.image.get_rect()
        self.type = "NONE"

        

class KeyItem(Item):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("graphics/key.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.type = "Door_Key"

class Screwdriver(Item):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load("graphics/chave_de_fenda.png").convert_alpha()
        self.icon = pygame.transform.scale(self.image, (40, 44))
        self.rect = self.image.get_rect()
        self.type = "Screwdriver"