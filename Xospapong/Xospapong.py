import pygame
from menu import Menu
from jogo import Jogo
pygame.init()
#create the game screen
screen = pygame.display.set_mode((800,600))

#title and icon
pygame.display.set_caption("Xospapong")
icon = pygame.image.load("C:/Users/Gabriel/Desktop/Computação/Python/Xospaquest/sapo/test.png")
pygame.display.set_icon(icon)

#game loop

running = True
main_menu = Menu()
game_screen = Jogo(screen)
main_menu.draw_menu(screen)
relogio = pygame.time.Clock()




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
            elif main_menu.enabled:
                print("TU TEM Q TAR NO MENU AGORA")
                main_menu.click_start(game_screen)
            elif game_screen.game_over:
                print("ELE SABE QUE O JOGO ACABOU E QUE VOCE CLICOU EM ALGO")
                game_screen.start_game()
        
                
        elif event.type == pygame.USEREVENT+1:
            pygame.time.set_timer(pygame.USEREVENT+1, 0)
            game_screen.bola.ball_speed()
            

    if game_screen.game_enable == True:
        teclas_pressionadas = pygame.key.get_pressed()
        if teclas_pressionadas[pygame.K_UP] == True:
            game_screen.player1.human_movement(-1)
        if teclas_pressionadas[pygame.K_DOWN] == True:
            game_screen.player1.human_movement(1)
        #Roda o jogo
        game_screen.update_frame()
        if game_screen.game_over == False:
            game_screen.draw_game()
        
    pygame.display.update()
    relogio.tick(60)