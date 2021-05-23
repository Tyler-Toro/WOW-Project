import pygame
import time
import sys


from pygame_utilities import *
from ETS_main_pygame import *
from ETS_functions_pygame import *
from ETS_intro_pygame import * 
from ETS_rooms_pygame import *
from ETS_battles_pygame import *



first = True
# infinite loop
while True:
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    if first:
        write("Main Page", (X//2, Y//2), (0,0,128), sleep = 1)
        write("Second Page", (0, 5), white)
        first = False
    pygame.event.pump()

    for event in pygame.event.get():
 
        # if event object type is QUIT
        # then quitting the pygame
        # and program both.
        if event.type == pygame.QUIT:
 
            # deactivates the pygame library
            pygame.quit()
 
            # quit the program.
            quit()
        

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                write("You went left")
            if event.key == pygame.K_RIGHT:
                write("Ouch!!", font_size=12)
            if event.key == pygame.K_DOWN:
                first = True
            if event.key == pygame.K_UP:
                text_slowmo(display_surface, text, (5, 5), story_font, color= green)
            if event.key == pygame.K_p:
                write(text)
            if event.key == pygame.K_LALT:
                text_slowmo(display_surface, text, (5, 35), story_font, color= green)
            if event.key == pygame.K_RALT:
                text_slowmo(display_surface, text, (5, 135), story_font, color= green)    
            if event.key == pygame.K_SPACE:
                header()
        # Draws the surface object to the screen.


'''
Refresh screen after event  ||| done with surface.fill()
create pygame rectangle to be text box, center it on x,y  ||| Done, text wrap function and math


create event if policy to navigate "rooms"

Keep ETS structure, with pygame input output use 


'''



        