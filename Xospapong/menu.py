import pygame
#Menu Principal
class Menu:
    def __init__(self):
        self.enabled = True
        #Superficie
        self.menu_surface = pygame.Surface((800, 600))
        #Texto Principal
        self.menu_font = pygame.font.Font('freesansbold.ttf',64)
        self.menu_text = self.menu_font.render("XOSPAPONG", True, (255, 255, 255))
        self.menu_surface.blit(self.menu_text,(200, 250))
        #Texto Secundario  
        self.menu_subfont = pygame.font.Font('freesansbold.ttf',32)
        self.menu_subtext = self.menu_subfont.render("Aperta qualquer calango aí", True, (255, 255, 255))
        self.menu_surface.blit(self.menu_subtext,(200, 350))
    def draw_menu(self, screen):
        #Desenha o menu por cima do display
        screen.blit(self.menu_surface, (0, 0))
        #Click to start
    def click_start(self,game_screen):
        if self.enabled:
            game_screen.start_game()
            self.enabled = False


        #Dois retangulos se mexendo no fundo
        pass
#Classe Pessoa, o subtipo seria Asiatico. Mas um objeto seria uma pessoa especifica.
#Porem eh possivel criar um objeto do subtipo Asiatico, que vai ter as caracteristicas do Tipo Pessoa E do subtipo Asiatico.