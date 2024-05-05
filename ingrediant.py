import pygame
import pandas as pd
ingrediants_List = ["images/gui/potato.png","images/gui/egg.png","images/gui/onion.png","images/gui/cheese.png","images/gui/fish.png","images/gui/chicken.png","images/gui/meat.png","images/gui/pasta.png","images/gui/rice.png","images/gui/tomato.png"]
ingrediants_name = ["potato","eggs","onion","cheese","fish","chicken","meat","pasta","rice","tomato"]
class ingrediants:
    def __init__(self,image):
        self.image = image
        self.ingrediant = []
        self.loaded_image = pygame.image.load(self.image)
    def collision(self):
        collision = pygame.Rect.collidepoint(self.loaded_image)
        return collision
    def cords(self,going_down):
        self.center_circle = 1060, 45 + going_down
        return self.center_circle
    def images_return(self):
        return self.loaded_image
    def ImageToName(self,ingrediant_used):
        for number,ingrediant in enumerate(ingrediants_List):
            if ingrediant in ingrediant_used:
                self.ingrediant.append(ingrediants_name[number])
        return self.ingrediant
   