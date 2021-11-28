from os import write
import pygame
import json

class Dialog_manager():
    def __init__(self):
        self.dialog_text = [""]
        self.dialog_key = ""
        self.current_line = 0
        self.color = (255,255,255)
        font = pygame.font.match_font("arial")
        self.font = pygame.font.Font(font,20)
        self.surface = self.font.render(self.dialog_text[self.current_line],False,(255,255,255))
        self.rect = self.surface.get_rect()

        

    def show_dialogue(self):
        pass

    def set_dialog(self, dialogKey, **karg):
        
        if self.dialog_key == "" or "overwrite" in karg:
            file = open("Dialogues/"+ dialogKey +".json", mode="r", encoding="utf-8")
        

            texto = json.load(file)
            texto = texto["text"] #transformando dicioário em uma lista para ordernar as linhas de diálogo.

            file.close()

            print(texto)
            print(len(texto))

            self.dialog_key = dialogKey
            self.dialog_text = texto
            self.current_line = 0
            
            if "color" in karg: 
                self.color = karg["color"] 
            self.surface = self.font.render(self.dialog_text[self.current_line],False,self.color)
            self.rect = self.surface.get_rect(center = (427,240))

       
    def next_line(self):
        
       
        
        if self.current_line+1 < len(self.dialog_text):
            self.current_line += 1
            self.surface = self.font.render(self.dialog_text[self.current_line],False,self.color)
            self.rect = self.surface.get_rect(center = (427,240))

        else:
            self.clear_dialog()

    def clear_dialog(self):
        self.dialog_text = [""]
        self.dialog_key = ""
        self.current_line = 0
        self.color = (255,255,255)
        self.surface = self.font.render(self.dialog_text[self.current_line],False,self.color)
        self.rect = self.surface.get_rect(center = (427,240))