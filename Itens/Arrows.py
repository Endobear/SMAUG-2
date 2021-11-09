import pygame

class UpArrow(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.image = pygame.image.load("graphics/Setas/Cima.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()/6,self.image.get_height()/6))
        self.image.set_alpha(128)
        self.rect = self.image.get_rect(center = position)
        self.locationName = "Up"
    
class FrontArrow(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.image = pygame.image.load("graphics/Setas/Frente.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()/6,self.image.get_height()/6))
        self.image.set_alpha(128)
        self.rect = self.image.get_rect(center = position)
        self.locationName = "Front"

class BackArrow(pygame.sprite.Sprite):
    def __init__(self,position):
        super().__init__()
        self.image = pygame.image.load("graphics/Setas/Volta.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()/6,self.image.get_height()/6))
        self.image.set_alpha(128)
        self.rect = self.image.get_rect(center = position)
        self.locationName = "Back"

class DiagonalArrow(pygame.sprite.Sprite):
    def __init__(self,position,angle):
        super().__init__()
        self.image = pygame.image.load("graphics/Setas/Diagonal.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(self.image.get_width()/6,self.image.get_height()/6))
        self.image = pygame.transform.rotate(self.image,angle)
        self.image.set_alpha(128)
        self.rect = self.image.get_rect(center = position)
        self.locationName = "Back"

