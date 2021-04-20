#the goal is to use pygame to run the game
# this code will create a display, while, for, and if statements
#list of functions and code that will be use for pytest


import pygame
import random

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Escaping Toro Sanctum")

BLUE = (0, 0, 150)

FPS = 60

def draw_window():
    WIN.fill(BLUE)
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()



#lever_direct = ["left", "right", "up", "down"]
    
#get_lever_direct = random.choice(lever_direct)
#print(get_lever_direct)