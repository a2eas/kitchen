import pygame
import sys
from ingrediant import *  # Assuming there's an Ingredient class in ingredient module
from ingrediant import ingrediants

# Initialize Pygame
pygame.init()

# Loading images
table = pygame.image.load("images/gui/table.jpg")
icon = pygame.image.load("images/icon.jpg")
menu_button1 = pygame.image.load("images/gui/menu butto.png") 
menu_button2 = pygame.image.load("images/gui/menu button2.png")

menu_button1_rect = menu_button1.get_rect()
menu_button1_rect.topleft = (900, 19)
circle_color = "PINK"  # Corrected variable name
background_image = pygame.image.load("images/gui/background.png")
events = []
button_to_reccomand =  [pygame.image.load("images/gui/button_to_reccomand.png"),pygame.image.load("images/gui/button_to_reccomand1.png")]
class Gui:
    def __init__(self,screen) -> None:
        self.dragging = False
        self.dragging_index = None
        self.index_used = []
        self.ingrediants_used = [] # keeping track of what ingrediant is put on the plat
        self.ingxandy = []
        self.screen = screen
        self.mouse_pos = pygame.mouse.get_pos()
        self.coliide = 0
        self.ing = []
    def main_loop(self, screen, event):
        # Detecting mouse press
        screen.blit(background_image, (1015, 2))
        vertical_distance = 0
        screen.blit(table, (0, -100))

        # Load the circular image
        menu_button_rect = menu_button1.get_rect(topleft=(900, 19))
        circle_radius = 44  # Half of the diameter

        # Get the position of the mouse cursor
        mouse_pos = pygame.mouse.get_pos()

        # Calculate the distance between mouse cursor and center of the circle
        circle_center = (menu_button_rect.x + circle_radius, menu_button_rect.y + circle_radius)
        distance = pygame.math.Vector2(mouse_pos).distance_to(circle_center)

        # Check for collision
        if distance <= circle_radius:
            screen.blit(menu_button2, menu_button1_rect.topleft)
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                mouse_pressed = False

                return clicked
                
        else:
            screen.blit(menu_button1, menu_button1_rect.topleft)

        # Drawing the ingredients
        i = 0
        image_rect_list = []  # Initialize the list outside the loop
        ingrediants_scaled = []
        for ingredient_name in ingrediants_List:  # Corrected variable name
            ingredient = ingrediants(ingredient_name)
    
            x, y = ingredient.cords(vertical_distance)
            circle = pygame.draw.circle(screen, circle_color, (x, y), 30)
            scale_factor = 0.7  # Adjust this value to control the size of the image

            # Calculate the scaled dimensions for the image
            scaled_width = int(ingredient.images_return().get_width() * scale_factor)
            scaled_height = int(ingredient.images_return().get_height() * scale_factor)
            scaled_image = pygame.transform.scale(ingredient.images_return(), (scaled_width, scaled_height))

            # Define the rect for the scaled image
            scaled_rect = scaled_image.get_rect(center=(x, y))
            mouse_x,mouse_y = mouse_pos
            # Draw the image at its original positio
            ingrediants_scaled.append(scaled_rect)
            image_rect_list.append(scaled_image)
            vertical_distance += 70
            screen.blit(scaled_image, scaled_rect)
            # Add the rect to the image_rect_list
        for index, ingredient_scaled in enumerate(ingrediants_scaled):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down = True
                if ingredient_scaled.collidepoint(mouse_x,mouse_y) and not self.dragging:
                    self.dragging = True
                    self.dragging_index = index
            elif event.type == pygame.MOUSEBUTTONUP:
                self.dragging = False
                self.dragging_index = None
                self.mouse_down = False
                
            if self.dragging_index == index:
                    mouse_pos = pygame.mouse.get_pos()
                    scaled_rect.center = mouse_pos
                    screen.blit(image_rect_list[index], scaled_rect)
            # collision with the plate
            plate_center = (492, 416)
            plate_raduis = 295
            distance_2mouse = pygame.math.Vector2(mouse_pos).distance_to(plate_center)
            if distance_2mouse <= plate_raduis and self.dragging_index != None:
                if ingrediants_List[self.dragging_index] in self.ingrediants_used:
                    pass
                else:
                    self.ingrediants_used.append(ingrediants_List[self.dragging_index])
                    self.ing = ingredient.ImageToName(self.ingrediants_used)
                print(self.ing)

                if self.dragging_index == None:
                    pass
                else:
                    if self.index_used in self.ingrediants_used:
                        pass
                    else: 
                        self.index_used += self.ingrediants_used
                self.dragging_index = None
                self.dragging = False
            ing_x = 200
            ing_y = 300
            for ingrediant_used in self.ingrediants_used:
                if ing_x >= 600:
                    ing_y += 120
                    ing_x = 280
                else:    
                    ing_x += 90
                ingrediant_image = pygame.image.load(ingrediant_used)
                screen.blit(ingrediant_image,(ing_x,ing_y))
                if (ing_x,ing_y) in self.ingxandy:
                    pass
                else:
                    self.ingxandy.append((ing_x,ing_y))
                

        pygame.display.flip()
    def remove_ingrediant(self):
        #loading the image and scaling it
        self.remove_button = pygame.image.load("images/gui/minus.png")
        scale_factor = 0.4
        scaled_width = int(self.remove_button.get_width() * scale_factor)
        scaled_height = int(self.remove_button.get_height() * scale_factor)
        scaled_image = pygame.transform.scale(self.remove_button, (scaled_width, scaled_height))
        scaled_rect = []
        for i,ingrediant in enumerate(self.ingrediants_used):
            x,y = self.ingxandy[i]
            x += 40
            y -= 30
            self.screen.blit(scaled_image,(x,y))
            scaled_rect.append(scaled_image.get_rect(topleft=(x,y)))
        for num,collision in enumerate(scaled_rect):
            for event in pygame.event.get():
                if scaled_rect[num].collidepoint(pygame.mouse.get_pos()) and event.type == pygame.MOUSEBUTTONDOWN:
                    self.ingrediants_used.remove(self.ingrediants_used[num])
                    self.ingxandy.remove(self.ingxandy[len(self.ingxandy)-1])
    def main_rec_button(self):
        scale_factor = 0.3
        scaled_image = pygame.transform.scale(button_to_reccomand[self.coliide], (int(button_to_reccomand[self.coliide].get_width() * scale_factor),
                                                                                int(button_to_reccomand[self.coliide].get_height() * scale_factor * 0.3)))
        button_pos = (340, 720)

        # Blit the scaled button image to the screen
        self.screen.blit(scaled_image, button_pos)

        # Get the rect of the scaled image
        button_rect = scaled_image.get_rect(topleft=button_pos)

        # Update the mouse position to get the current position
        self.mouse_pos = pygame.mouse.get_pos()

        # Check for collision with the mouse cursor
        if button_rect.collidepoint(self.mouse_pos):
            self.coliide = 1
        else:
            self.coliide = 0
        