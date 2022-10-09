'''
Simple shape game for one user to interact with
'''

import pygame
#from network import Network
#import pickle
pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Player")


def main():
  run = True
  clock = pygame.time.Clock()
  while run:
    #pygame.draw.rect(win. (255,255,255), 100, 100, width, height)
    clock.tick(60)
    win.fill((128,128,128))
    font = pygame.font.SysFont("comicsans", 60)
    text = font.render("HAM BURGER CHEESE BRUGER BIG MAC WHOPPER ", 1, (255,0,0))
    win.blit(text, (50,100))

    pygame.display.update()

main()





