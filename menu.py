import pygame
import os
from pygame.locals import *
from sys import exit

menu_selecao = 1
WIDTH = 800
HEIGHT = 500
FPS = 30

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
botao_enter = False


def eventos():
    global menu_selecao, botao_enter

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_s:
                menu_selecao += 1
            if event.key == K_w:
                menu_selecao -= 1
            if event.key == K_ESCAPE:
                menu_selecao += 10


def selecao():
    global menu_selecao, botao_enter

    if menu_selecao == 1:
        screen.fill((0, 0, 0))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        novo_jogo = fonte.render('>> Novo jogo <<', True, (80, 80, 80))
        screen.blit(novo_jogo, ((WIDTH / 2) - 55, (HEIGHT / 2)))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        carregar_jogo = fonte.render(' Carregar jogo ', True, (80, 80, 80))
        screen.blit(carregar_jogo, ((WIDTH / 2) - 50, (HEIGHT / 2) + 22))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        configuracoes = fonte.render(' Configurações ', True, (80, 80, 80))
        screen.blit(configuracoes, ((WIDTH / 2) - 50, (HEIGHT / 2) + 44))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        sair = fonte.render(' Sair ', True, (80, 80, 80))
        screen.blit(sair, ((WIDTH / 2) - 15, (HEIGHT / 2) + 88))

    if menu_selecao == 2:
        screen.fill([0, 0, 0])

        fonte = pygame.font.SysFont('arial', 20, False, False)
        novo_jogo = fonte.render(' Novo jogo ', True, (80, 80, 80))
        screen.blit(novo_jogo, ((WIDTH / 2) - 55, (HEIGHT / 2)))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        carregar_jogo = fonte.render('>> Carregar jogo <<', True, (80, 80, 80))
        screen.blit(carregar_jogo, ((WIDTH / 2) - 50, (HEIGHT / 2) + 22))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        configuracoes = fonte.render(' Configurações ', True, (80, 80, 80))
        screen.blit(configuracoes, ((WIDTH / 2) - 50, (HEIGHT / 2) + 44))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        sair = fonte.render(' Sair ', True, (80, 80, 80))
        screen.blit(sair, ((WIDTH / 2) - 15, (HEIGHT / 2) + 88))

    if menu_selecao == 3:
        screen.fill([0, 0, 0])

        fonte = pygame.font.SysFont('arial', 20, False, False)
        novo_jogo = fonte.render(' Novo jogo ', True, (80, 80, 80))
        screen.blit(novo_jogo, ((WIDTH / 2) - 55, (HEIGHT / 2)))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        carregar_jogo = fonte.render(' Carregar jogo ', True, (80, 80, 80))
        screen.blit(carregar_jogo, ((WIDTH / 2) - 50, (HEIGHT / 2) + 22))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        configuracoes = fonte.render('>> Configurações <<', True, (80, 80, 80))
        screen.blit(configuracoes, ((WIDTH / 2) - 50, (HEIGHT / 2) + 44))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        sair = fonte.render(' Sair ', True, (80, 80, 80))
        screen.blit(sair, ((WIDTH / 2) - 15, (HEIGHT / 2) + 88))

    if menu_selecao == 4:
        screen.fill([0, 0, 0])

        fonte = pygame.font.SysFont('arial', 20, False, False)
        novo_jogo = fonte.render(' Novo jogo ', True, (80, 80, 80))
        screen.blit(novo_jogo, ((WIDTH / 2) - 55, (HEIGHT / 2)))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        carregar_jogo = fonte.render(' Carregar jogo ', True, (80, 80, 80))
        screen.blit(carregar_jogo, ((WIDTH / 2) - 50, (HEIGHT / 2) + 22))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        configuracoes = fonte.render(' Configurações ', True, (80, 80, 80))
        screen.blit(configuracoes, ((WIDTH / 2) - 50, (HEIGHT / 2) + 44))

        fonte = pygame.font.SysFont('arial', 20, False, False)
        sair = fonte.render('>> Sair <<', True, (80, 80, 80))
        screen.blit(sair, ((WIDTH / 2) - 15, (HEIGHT / 2) + 88))

    if menu_selecao == 5:
        menu_selecao = 4

    if menu_selecao == 0:
        menu_selecao = 1

    if menu_selecao == 14:
        pygame.quit()
        exit()

while True:
    clock.tick(FPS)
    eventos()
    selecao()
    print(botao_enter)
    print(menu_selecao)

    pygame.display.update()
