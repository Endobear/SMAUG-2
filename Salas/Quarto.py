import pygame
from Itens.Itens import KeyItem
from Salas.Room import Room
from Itens.Arrows import BackArrow,UpArrow,DiagonalArrow

class Quarto(Room):
    def __init__(self,map):
        super().__init__()
        self.room_name = "Quarto"
        self.image = "graphics/Cenario 1/Quarto_gaveta_fechada.png"
        self.exits = ["Up","Back"]
        self.exitsName = ["QuartoPorta"]
        self.map = map
        
        self.arrows = [BackArrow((420,450))]
        
        self.gaveta = QuartoGaveta(self)
        self.quartoPorta = QuartoPorta(self)
        self.quartoTeto = QuartoTeto(self)

        self.interactives = {"cama": pygame.Rect((505,230),(349,250)), 
                             "armario": pygame.Rect((78,46),(251,417)),
                             "comoda": pygame.Rect((355,327),(129,136))}

        self.id = "Quarto"

        self.tutorial_phase = 0

        

    
    def backLocation(self):
        return self.quartoPorta
    def upLocation(self):
        # if not("comoda" in self.interactives):
        #      self.addRect(pygame.Rect((355,327),(129,136)), "comoda")
        return self.quartoTeto


    def ineractRect(self,rect,player):
        super().ineractRect(rect,player)
        

        if rect == self.interactives["comoda"]: # Cômoda do quarto
            
            if not self.quartoTeto.firstTime:
                player.change_room(self.gaveta)
                self.image = "graphics/Cenario 1/Quarto_gaveta_aberta.png"
                self.quartoTeto.image = "graphics/Cenario 1/Teto_gaveta_aberta.png"
                self.quartoTeto.gaveta_open = True
            else:
                player.dialog_manager.set_dialog("interacao_comoda")

        if rect == self.interactives["cama"]:
            player.dialog_manager.set_dialog("interacao_cama")

        if rect == self.interactives["armario"]:
            player.dialog_manager.set_dialog("interacao_armario")

    def update(self, screen):
        
        if self.tutorial_phase == 0:
            self.map.player.dialog_manager.set_dialog("tutorial_dialog_0", color = (102, 250, 245))
            self.tutorial_phase = 1
        return super().update(screen)


class QuartoGaveta(Room):
    def __init__(self,quarto):
        super().__init__()
        self.room_name = "QuartoGaveta"
        self.exits = ["Back"]
        self.arrows = [BackArrow((42,385))]
        self.quarto = quarto
        self.image = "graphics/Cenario 1/gaveta_gancho.png"
        self.gancho_breakable = False
        self.gancho = True
        
        self.interactives = {"gancho": pygame.Rect((510,157),(147,69))}
        
        

    def backLocation(self):
        return self.quarto


    def ineractRect(self,rect,player):
        super().ineractRect(rect,player)
        if rect == self.interactives["gancho"]: # Porta
            if self.gancho_breakable and self.gancho:
                self.gancho = False
                self.image = "graphics/Cenario 1/gaveta.png"
                self.quarto.quartoTeto.image = "graphics/Cenario 1/Teto_gaveta.png"
                chave = KeyItem();
                chave.set_position((200,200))
                self.quarto.itens.append(chave)
            elif self.gancho:
                player.dialog_manager.set_dialog("interacao_gancho")
                
        
       

    
class QuartoPorta(Room):
    def __init__(self,quarto):
        super().__init__()
        self.room_name = "QuartoPorta"
        self.exits = ["Back","Up"]
        self.image = "graphics/Cenario 1/Quarto_porta_fechada.png"
        self.arrows = [BackArrow((486,431))]
        self.quarto = quarto
        self.door_status = False


        porta_rect = pygame.Rect((409,103),(165,314))
        self.interactives["porta"] = porta_rect
        
    def backLocation(self):
        return self.quarto

    def ineractRect(self,rect,player):
        super().ineractRect(rect,player)
        if rect == self.interactives["porta"]: # Porta
            if not self.door_status:
                player.dialog_manager.set_dialog("interacao_porta")
                if len(self.quarto.arrows) < 2:
                    self.quarto.arrows.append(UpArrow((420,100)))
            else:
                player.change_room(self.quarto.RoomExitClassFromMap(self.quarto.map,self.quarto.exitsName[0]))
              
    def update(self, screen):
    
        if self.quarto.tutorial_phase == 1:
            self.quarto.map.player.dialog_manager.set_dialog("tutorial_dialog_1", color = (102, 250, 245))
            self.quarto.tutorial_phase = 2
        return super().update(screen)

    def useItem(self, rect, player):
        itemHolding = player.itemHolding.sprites()[0]
        if rect in [interactives for interactives in self.interactives.values()]:
            if rect == self.interactives["porta"] and itemHolding.type == KeyItem().type:
                print("abriu")
                player.inventory.remove(itemHolding)
                self.door_status = True
                self.image = "graphics/Cenario 1/Quarto_porta_aberta.png"


class QuartoTeto(Room):
    def __init__(self,quarto):
        super().__init__()
        self.room_name = "QuartoTeto"
        self.exits = ["Back"]
        self.arrows = [DiagonalArrow( (127,425), -90)]
        self.image = "graphics/Cenario 1/Teto_gaveta_fechada.png"
        self.quarto = quarto
        self.firstTime = True
        self.gaveta_open = False
        
        self.interactives = {"gaveta": pygame.Rect((411,29),(112,120))}

    def backLocation(self):
        return self.quarto

    def update(self, screen):
    
        if self.firstTime:
            self.quarto.map.player.dialog_manager.set_dialog("FirstTime_QuartoTeto")
            self.firstTime = False
            
        elif self.quarto.tutorial_phase == 2:
            self.quarto.map.player.dialog_manager.set_dialog("FirstTime_QuartoTeto")
            self.quarto.tutorial_phase = 3
        return super().update(screen)

    def ineractRect(self,rect,player):
        super().ineractRect(rect,player)
        if rect == self.interactives["gaveta"] and self.gaveta_open and self.quarto.gaveta.gancho: 
            self.quarto.map.player.dialog_manager.set_dialog("interacao_gaveta")
            self.quarto.gaveta.gancho_breakable = True
