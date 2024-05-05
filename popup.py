import Gui
import pygame
# Function to display a pop-up screen
screen_width = 1000
screen_height = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
gray = (128,128,128)
def show_popup(message,screen,clicked):
    if message != None or clicked:
        name,instruction = message 
        popup_width, popup_height = 400, 200
        popup_x, popup_y = (screen_width - popup_width) // 2, (screen_height - popup_height) // 2
        popup_surface = pygame.Surface((popup_width, popup_height))
        popup_surface.fill(gray)
        [popup_surface.blit(pygame.font.Font(None, 18).render(line, True, BLACK), (popup_width // 2, 10 + i * 40)) for i, line in enumerate(str(name).split("\n"))]
        for i, line in enumerate(str(instruction).split("\n")):
            popup_surface.blit(pygame.font.Font(None, 18).render(line, True, BLACK), (2, 10 + i * 40+40))
            if popup_width<=  10 + i * 40+40:
                popup_y =+ 20
                i = 1
        pygame.draw.rect(popup_surface, BLACK, popup_surface.get_rect(), 10)
        screen.blit(popup_surface, (popup_x, popup_y))
        pygame.display.flip()
    # Update the display
    pygame.display.flip()

