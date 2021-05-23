import pygame
import time

pygame.init()


white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

X = 600
Y = 600

display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.SysFont('calibri', 32)

def write(text, location = (0, Y//2), color=(255,255,255), sleep = 0, font_size = 28):
    font = pygame.font.SysFont('calibri', font_size)
    display_surface.fill(black)
    display_surface.blit(font.render(text,True,color),location)
    pygame.display.update()
    pygame.event.pump()
    time.sleep(sleep)
    pygame.event.pump()



def ask(screen, question):
    current_string = ""
    write(question)
    while 1:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    current_string = current_string[0:-1]
                elif event.key == pygame.K_RETURN:
                    return current_string
                else:
                    current_string += pygame.key.name(event.key)
                print(current_string)
                write(question + ": " + current_string)

user_name = ""

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
 
            quit()
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                user_name= ask(display_surface, "What is your name")
                write("You have entered: " + user_name)
            if event.key == pygame.K_DOWN:
                write(f"{user_name} , you have died! Sorry {user_name}")
            
        # Draws the surface object to the screen.

