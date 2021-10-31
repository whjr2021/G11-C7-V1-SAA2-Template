# Import and initialize pygame library
import pygame
pygame.init() 

# RGB color combinations
DARKBLUE = (36,90,190)
WHITE = (255,255,255)

# Create a screen of size (400, 200) and assign to variable "screen"


# While loop
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            carryOn = False
    screen.fill(DARKBLUE)
    
    # Code to display text "First Name: John" at location (20,10)
    
    
    
    
    # Code to display text "Country: India" at location (20,40)
    
    
    
    # Code to display text "State: Bengal" at location (20,70)



    pygame.display.flip() 
pygame.quit()
    