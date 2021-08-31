import pygame

class UpArrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/Setas/Cima.png").convert_alpha()
        self.rect = self.image.get_rect()
    
class FrontArrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/Setas/Frente.png").convert_alpha()
        self.rect = self.image.get_rect()

class BackArrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("graphics/Setas/Volta.png").convert_alpha()
        self.rect = self.image.get_rect()
    