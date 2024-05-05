import pygame
import sys
from Gui import *
from llm import matching_ing
from popup import show_popup
# Initialize Pygame
pygame.init()

# Load images
table = pygame.image.load("images/gui/table.jpg")
icon = pygame.image.load("images/icon.jpg")

# Define screen size and create a display surface
screen_width = 1000
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_icon(icon)
# Set the title and icon
pygame.display.set_caption("Your Game")

gui = Gui(screen) 
# Initialize variables
clicked_once = False
 # Assuming Gui class is defined and handles the GUI elements

# Main loop
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        screen.fill((132,132,132))
        
        # Pass the event to the GUI for handling
        button_clicked = gui.main_loop(screen=screen,event= event)
        if gui.coliide and event.type == pygame.MOUSEBUTTONDOWN:
           text = matching_ing(gui.ing)
           clicked = True
           show_popup(text,screen,clicked)
        if button_clicked and not clicked_once:
            # Change screen size and background once when button is clicked
            screen = pygame.display.set_mode((1100, screen_height))
            clicked_once = True

        elif clicked_once and button_clicked:
            # Revert changes when the button is clicked again
            screen = pygame.display.set_mode((1000, screen_height))
            clicked_once = False
        gui.remove_ingrediant()
        gui.main_rec_button()

        #first postion (492, 416)
        #second postion (787, 416)
        #raduis = 295d

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame properly
pygame.quit()
sys.exit()


