import pygame
#Dois retangulos
class Retangulo:
    largura = 20
    def __init__(self,surface, x):
        self.retangulo = pygame.Rect( x, 250, 20, 100)
        self.surface = surface
        pygame.draw.rect(self.surface,(255, 255, 255), self.retangulo)
        self.velocidade = 10

    def ret_move(self, direction):
        #Calcula a nova posicao
        retangulo_y = self.velocidade * direction
        self.retangulo.move_ip(0 , retangulo_y)
        #Caso a posicao esteja fora do limite ele reseta a possicao para logo antes do limite
    
    def draw_rect(self):
        pygame.draw.rect(self.surface,(255, 255, 255), self.retangulo)
