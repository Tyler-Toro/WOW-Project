import pygame
import time
from pygame.locals import *

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
cyan = (0, 255, 255)
magenta = (255, 0, 255)
orange = (255, 128, 0)

pygame.init()

X = 600
Y = 600

display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.SysFont('calibri', 32)
story_font = pygame.font.SysFont('calibri', 18)



def write(text, location = (50, Y//2), color= green, sleep = 0, font_size = 20):
    font = pygame.font.SysFont('calibri', font_size)
    display_surface.fill(black)
    display_surface.blit(font.render(text,True,color),location)
    pygame.display.update()
    pygame.event.pump()
    time.sleep(sleep)
    pygame.event.pump()

def text_wrap(text, pos, surface=display_surface, font_size=18, color= green, fill = True, box = False, sleep = 0):
    font = pygame.font.SysFont('calibri', font_size)
    if fill is True:
        surface.fill(black)
    words = [word.split(' ') for word in text.splitlines()]  
    space = font.size(' ')[0]  
    max_width, max_height = surface.get_size()
    x, y = pos
    num_rows = 1
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                num_rows += 1
                x = pos[0]  
                y += word_height  
            surface.blit(word_surface, (x, y))
            x += word_width + space   
        x = pos[0]  
        y += word_height  
    if box:
        story_rect = pygame.Rect((pos[0]-2), (pos[1]-2), X-x, (num_rows*word_height+3))      #Makes the rect same size of text 
        pygame.draw.rect(surface, green, story_rect, 1)    
    pygame.display.update()
    pygame.event.pump()
    time.sleep(sleep)
    





def text_slowmo(text, pos, color= green, font_size=18, box = False, fill = True, sleep = 1, speed = .01):
        for i in range(1, len(text)):
            text_wrap(text[0:i], pos, color=color, font_size = font_size, fill = fill, box = box)
            time.sleep(speed)
        time.sleep(sleep)



def ask(question, pos = (10, 200), fill = True, box = False):
    current_string = ""
    text_wrap(question, pos, fill = fill, box = box)
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
                text_wrap(question + ": " + current_string, pos, fill = fill, box = box)


def pause():
    pausing = ask("press <enter> to continue...", (300, 570), fill = False)
    text_wrap("press <enter> to continue...", (300, 570), color = black, fill = False)