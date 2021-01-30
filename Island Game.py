import pygame
import random
import math
from pygame import mixer
#initialize
pygame.init()
mixer.init()
#create the game screen
screen = pygame.display.set_mode((800,600))

class Menu:
    def __init__(self):
        self.enabled = True
        #Superficie
        self.menu_surface = pygame.Surface((800, 600))
        #Texto Principal
        self.menu_font = pygame.font.Font('freesansbold.ttf',64)
        self.menu_text = self.menu_font.render("Island Game", True, (255, 255, 255))
        self.menu_surface.blit(self.menu_text,(200, 150))
        #Texto Secundario  
        self.menu_subfont = pygame.font.Font('freesansbold.ttf',32)
        self.menu_subtext = self.menu_subfont.render("The game that happens on an island", True, (255, 255, 255))
        self.menu_surface.blit(self.menu_subtext,(120, 350))
        #Texto The Third
        self.menu_subfont = pygame.font.Font('freesansbold.ttf',32)
        self.menu_subtext = self.menu_subfont.render("(Don't play outside islands)", True, (255, 255, 255))
        self.menu_surface.blit(self.menu_subtext,(180, 400))
    def draw_menu(self, screen):
        #Desenha o menu por cima do display
        screen.blit(self.menu_surface, (0, 0))
        #Click to start
    def click_start(self,game_screen):
        if self.enabled:
            game_screen.start_game()
            self.enabled = False

#Variables
running = True
main_menu = Menu()
main_menu.draw_menu(screen)

#Running
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    #Desenha o menu por cima do display
    #Click to start


