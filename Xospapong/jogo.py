import pygame
import bot
import bola
import human
#Jogo
class Jogo:
    def __init__(self, screen):
        self.display = screen
        self.game_area = pygame.Rect(100, 100, 600, 400)
        self.game_enable = False
        self.game_surface = pygame.Surface((800, 600))
        self.game_over = False
        self.bola = bola.Bola(self.game_surface)
        self.player1 = human.Human(self.game_surface, self.game_area)
        self.player2 = bot.Bot(self.game_surface, self.game_area)
        #Texto Pontuacao
        self.game_font = pygame.font.Font('freesansbold.ttf',32)
        self.game_textscore = self.game_font.render("Player 1 Score:" + str(self.player1.score), True, (255, 255, 255))
        self.game_textscore2 = self.game_font.render("Player 2 Score:" + str(self.player2.score), True, (255, 255, 255))
        
        
    
    def draw_game(self):
        #Desenha o jogo por cima do display
        size = self.game_font.size("Player 1 score: 00")
        length = size[0]
        self.game_surface.fill((0, 0, 0))
        self.player1.player_rect.draw_rect()
        self.player2.player_rect.draw_rect()
        self.bola.draw_ball()
        self.game_surface.blit(self.game_textscore,(20, 20))
        self.game_surface.blit(self.game_textscore2,(780 - length, 20))
        pontos = (
            (self.game_area.left-1, self.game_area.top-1),
            (self.game_area.right+1, self.game_area.top-1),
            (self.game_area.right+1, self.game_area.bottom+1),
            (self.game_area.left-1, self.game_area.bottom+1)
        )
        pygame.draw.polygon(self.game_surface, (255, 255, 255), pontos, 1)
        self.display.blit(self.game_surface, (0, 0))
        

    def update_frame(self):
        self.bola.ball_movement()
        self.player2.bot_movement(self.bola.bola.y)
        self.player_collision()
        self.ball_collision()
        self.point()
        #Vai atualizar o jogo pro proximo frame
    
    def start_game(self):
        print("TA ENTRANDO START GAME")
        self.game_enable = True
        self.player1.score = 0
        self.player2.score = 0
        self.reset()
        self.game_over = False
        self.game_textscore = self.game_font.render("Player 1 Score:" + str(self.player1.score), True, (255, 255, 255))
        self.game_textscore2 = self.game_font.render("Player 2 Score:" + str(self.player2.score), True, (255, 255, 255))


    def end_game(self):
        self.game_enable = False
        self.game_over = True
        self.game_over_text0 = self.game_font.render("GAME OVER", True, (255, 255, 255))
        self.game_over_text1 = self.game_font.render("Player 1 Score:" + str(self.player1.score), True, (255, 255, 255))
        self.game_over_text2 = self.game_font.render("Player 2 Score:" + str(self.player2.score), True, (255, 255, 255))
        self.game_over_text3 = self.game_font.render("Aperte um calango para jogar mais!", True, (255, 255, 255))
        self.display.fill((0, 0, 0))
        self.display.blit(self.game_over_text0,(200, 40))
        self.display.blit(self.game_over_text1,(200, 200))
        self.display.blit(self.game_over_text2,(200, 250))
        self.display.blit(self.game_over_text3,(200, 500))
        print("ELE DESENHOU AS COISA DE GAME OVER")

    def reset(self):       
        pygame.time.set_timer(pygame.USEREVENT+1, 2000)
        self.bola.bola = pygame.Rect(400, 300, 10, 10)
        self.bola.velocidade["x"] = 0
        self.bola.velocidade["y"] = 0
        self.player1.player_rect.retangulo = pygame.Rect( 120, 250, 20, 100)
        self.player2.player_rect.retangulo = pygame.Rect( 660, 250, 20, 100)
    
    def ball_collision(self):
        if not self.game_area.contains(self.bola.bola):
            if self.bola.bola.top <= self.game_area.top:
                self.bola.bola.move_ip(0, (2*(self.game_area.top - self.bola.bola.top)))
                self.bola.velocidade["y"] *= -1
            elif self.bola.bola.bottom > self.game_area.bottom:
                self.bola.bola.move_ip(0, (2*(self.game_area.bottom - self.bola.bola.bottom)))
                self.bola.velocidade["y"] *= -1

        if self.player1.player_rect.retangulo.colliderect(self.bola.bola):
                self.bola.bola.move_ip(((self.player1.player_rect.retangulo.right - self.bola.bola.left)*2), 0)
                self.bola.velocidade["x"] *= -1
                diferenca = self.bola.bola.centery - self.player1.player_rect.retangulo.centery
                diferenca /= self.player1.player_rect.retangulo.height/2
                self.bola.velocidade["y"] += diferenca * 8

        
        if self.player2.player_rect.retangulo.colliderect(self.bola.bola):
                self.bola.bola.move_ip(((self.player2.player_rect.retangulo.left - self.bola.bola.right)*2), 0)
                self.bola.velocidade["x"] *= -1
                if self.bola.velocidade["x"] > 0:
                    self.bola.velocidade["x"] += 1
                else:
                    self.bola.velocidade["x"] -= 1

                diferenca = self.bola.bola.centery - self.player2.player_rect.retangulo.centery
                diferenca /= self.player2.player_rect.retangulo.height/2
                self.bola.velocidade["y"] += diferenca * 4
        

    
    def player_collision(self):
        if not self.game_area.contains(self.player1.player_rect.retangulo):
            if self.player1.player_rect.retangulo.top < self.game_area.top:
                self.player1.player_rect.retangulo.move_ip(0, self.game_area.top - self.player1.player_rect.retangulo.top)
            elif  self.player1.player_rect.retangulo.bottom > self.game_area.bottom:
                self.player1.player_rect.retangulo.move_ip(0, self.game_area.bottom - self.player1.player_rect.retangulo.bottom)
        if not self.game_area.contains(self.player2.player_rect.retangulo):
            if self.player2.player_rect.retangulo.top < self.game_area.top:
                self.player2.player_rect.retangulo.move_ip(0, self.game_area.top - self.player2.player_rect.retangulo.top)
            elif  self.player2.player_rect.retangulo.bottom > self.game_area.bottom:
                self.player2.player_rect.retangulo.move_ip(0, self.game_area.bottom - self.player2.player_rect.retangulo.bottom)


            

        

    def point(self):
        if self.bola.bola.left < self.game_area.left:
            player_point = self.player2
        elif self.bola.bola.right > self.game_area.right:
            player_point = self.player1
        else:
            player_point = None
        if player_point is not None:
            player_point.score += 1
            if player_point.score >= 10:
                self.end_game()
            else:
                self.game_textscore = self.game_font.render("Player 1 Score:" + str(self.player1.score), True, (255, 255, 255))
                self.game_textscore2 = self.game_font.render("Player 2 Score:" + str(self.player2.score), True, (255, 255, 255))
                self.reset()

        
            

                




        
