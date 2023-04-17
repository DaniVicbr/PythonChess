import pygame
import os
os.environ['SDL_VIDEO_CENTERED'] = '1'


pygame.init()
x = 600 
y = 600
screen = pygame.display.set_mode((x, y))
tamanho_casa = x // 8
clock = pygame.time.Clock()
running = True
pygame.display.set_caption("Noob Chess")
#image = pygame.image.load("C:/Users/VICTOR/Desktop/projects/tabuleiro.png")
#imager = pygame.transform.scale(image, (x,y))

pecas = { 
         "B_w": pygame.image.load("C:/Users/YourPc/B_w.png"),
         "K_w": pygame.image.load("C:/Users/YourPc/K_w.png"),
         "N_w": pygame.image.load("C:/Users/YourPc/N_w.png"),
         "P_w": pygame.image.load("C:/Users/YourPc/pieces/P_w.png"),
         "Q_w": pygame.image.load("C:/Users/YourPc/pieces/Q_w.png"),
         "R_w": pygame.image.load("C:/Users/YourPc/pieces/R_w.png"),
         "b": pygame.image.load("C:/Users/YourPc/pieces/b_w.png"),
         "k": pygame.image.load("C:/Users/YourPc/pieces/k_w.png"),
         "n": pygame.image.load("C:/Users/YourPc/pieces/n_w.png"),
         "p": pygame.image.load("C:/Users/YourPc/pieces/p_w.png"),
         "q": pygame.image.load("C:/Users/YourPc/pieces/q_w.png"),
         "r": pygame.image.load("C:/Users/YourPc/pieces/r_w.png"),

        }

for peca_nome in pecas.keys():
    pecas[peca_nome] = pygame.transform.scale(pecas[peca_nome], (tamanho_casa, tamanho_casa))

tabuleiro = [

        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p","p","p","p","p","p","p","p"],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["P_w","P_w","P_w","P_w","P_w","P_w","P_w","P_w"],
        ["R_w", "N_w", "B_w", "Q_w", "K_w", "B_w", "N_w", "R_w"],

        ]

def desenhar_tabuleiro():
    cor1 = (240, 217, 181)
    cor2 = (181, 136, 99)

    for linha in range(8):
        for coluna in range(8):
            cor = cor1 if (linha + coluna) % 2 == 0 else cor2
            pygame.draw.rect(screen, cor, (coluna*tamanho_casa, linha*tamanho_casa, tamanho_casa, tamanho_casa)) 
def desenhar_pecas():
    for linha in range(8):
        for coluna in range(8):
            peca = tabuleiro[linha][coluna]
            if peca != "":
                screen.blit(pecas[peca], (coluna*tamanho_casa, linha*tamanho_casa))

def atualizar_tela():
    desenhar_tabuleiro()
    desenhar_pecas()
    pygame.display.update()



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

     
        elif event.type == pygame.MOUSEBUTTONDOWN:
            coluna_clicada = event.pos[0] // tamanho_casa
            linha_clicada = event.pos[1] // tamanho_casa
            if tabuleiro[linha_clicada][coluna_clicada] != "":
                peca_selecionada = tabuleiro[linha_clicada][coluna_clicada]
                posicao_selecionada = (linha_clicada, coluna_clicada)
        elif event.type == pygame.MOUSEBUTTONUP:
            coluna_soltada = event.pos[0] // tamanho_casa
            linha_soltada = event.pos[1] // tamanho_casa
            if peca_selecionada != None and posicao_selecionada != None:
                tabuleiro[linha_soltada][coluna_soltada] = peca_selecionada
                tabuleiro[posicao_selecionada[0]][posicao_selecionada[1]] = ""
                peca_selecionada = None
                posicao_selecionada = None
 


    atualizar_tela()

    #screen.blit()
    
    pygame.display.update() 
    clock.tick(60)

pygame.quit()





