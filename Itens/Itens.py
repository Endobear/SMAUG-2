import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, **kword) -> None:
        super().__init__()
        self.image = pygame.image.load("graphics/key.png").convert_alpha()
        self.icon = self.image
        self.rect = self.image.get_rect()
        self.type = "NONE"
        self.dialog = ""
        if "dialog" in kword:
            self.dialog = kword["dialog"]

        self.dialog_color = (255,255,255)
        if "dialog_color" in kword:
            self.dialog_color = kword["dialog_color"]


    def set_position(self,position):
        self.rect = self.image.get_rect(center = position)

        

class KeyItem(Item):

    def __init__(self, **kword) -> None:
        super().__init__(**kword)
        self.image = pygame.transform.scale(pygame.image.load("graphics/Key_Item.png").convert_alpha(), (47, 27))
        self.icon = self.image
        self.rect = self.image.get_rect()
        self.type = "Door_Key"

class Screwdriver(Item):
    def __init__(self, **kword) -> None:
        super().__init__(**kword)
        self.image = pygame.image.load("graphics/chave_de_fenda.png").convert_alpha()
        self.icon = pygame.transform.scale(self.image, (40, 44))
        self.rect = self.image.get_rect()
        self.type = "Screwdriver"