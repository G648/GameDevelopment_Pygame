import pygame
import random

pygame.init()

#Configuração da janela do jogo
LARGURA_TELA = 800
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Acerte o alvo")

#Configuração das cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)

#Fluxo principal básico
relogio = pygame.time.Clock()
rodando = True

#Configuração do alvo
TAMANHO_ALVO = 50
alvo_rect = pygame.Rect(375, 275,  TAMANHO_ALVO, TAMANHO_ALVO) # (x, y, largura, altura)

#Configuração da fonte de exibição
pontos = 0
fonte = pygame.font.SysFont("bahnschrift", 35)

while rodando:
    #Capturar um evento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        
        #2. Criação da lógica
        #Verifica se o evento foi um clique do mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            #event.pos -> coordenada (x, y) do mouse
            #collidepoint verifica se o ponto está dentro do rect
            if alvo_rect.collidepoint(event.pos):
                #Calcula a nova posição X aleatória
                alvo_rect.x = random.randrange(0, LARGURA_TELA - TAMANHO_ALVO)
                #Calcula a nova posição Y aleatória
                alvo_rect.y = random.randrange(0, ALTURA_TELA - TAMANHO_ALVO)
                
                pontos += 1
    
    
    #3. Desenho
    tela.fill(PRETO)
    
    #NOVO
    pygame.draw.rect(tela, VERMELHO, alvo_rect)
    
    #Renderizar o texto dentro da tela 
    texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))
    
    #4. Atualizações
    pygame.display.flip()
    relogio.tick(60)

pygame.quit()