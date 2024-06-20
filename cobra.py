import pygame

# from pygame.locals import *


class Cobra:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.x = int(largura / 2)
        self.y = int(altura / 2)
        self.velocidade = 10
        self.x_controle = self.velocidade
        self.y_controle = 0
        self.comprimento_inicial = 5
        self.lista_cobra = []
        self.morreu = False

        # Lista de cores para os segmentos da cobra
        self.cores = [(0, 255, 0), (0, 200, 0), (0, 150, 0), (0, 100, 0)]

    def aumenta_cobra(self, tela):
        for i, segmento in enumerate(self.lista_cobra):
            cor = self.cores[i % len(self.cores)]
            pygame.draw.rect(tela, cor, (segmento[0], segmento[1], 20, 20))

    def mover(self):
        self.x += self.x_controle
        self.y += self.y_controle

        if self.x >= self.largura or self.x < 0 or self.y >= self.altura or self.y < 0:

            self.morreu = True

    def verificar_colisao(self):
        cabeca = []
        cabeca.append(self.x)
        cabeca.append(self.y)
        self.lista_cobra.append(cabeca)

        if len(self.lista_cobra) > self.comprimento_inicial:
            del self.lista_cobra[0]

        for segmento in self.lista_cobra[:-1]:
            if segmento == cabeca:
                self.morreu = True

    def reiniciar(self):
        self.x = int(self.largura / 2)
        self.y = int(self.altura / 2)
        self.velocidade = 10
        self.x_controle = self.velocidade
        self.y_controle = 0
        self.lista_cobra = []
        self.comprimento_inicial = 5
        self.morreu = False
