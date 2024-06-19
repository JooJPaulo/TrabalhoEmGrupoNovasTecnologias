import pygame
from pygame.locals import *

class Cobra(pygame.sprite.Sprite):
    def __init__(self, largura, altura):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (largura / 2, altura / 2)
        self.velocidade = 10
        self.x_controle = self.velocidade
        self.y_controle = 0
        self.comprimento_inicial = 5
        self.lista_cobra = []
        self.morreu = False
        self.largura = largura
        self.altura = altura
        self.x = self.rect.x
        self.y = self.rect.y

    def aumenta_cobra(self, tela):
        for XeY in self.lista_cobra:
            pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

    def mover(self):
        self.x += self.x_controle
        self.y += self.y_controle

        if self.x >= self.largura:
            self.x = 0
        elif self.x < 0:
            self.x = self.largura - 20
        if self.y >= self.altura:
            self.y = 0
        elif self.y < 0:
            self.y = self.altura - 20

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

    def move_left(self):
        if self.x_controle == 0:
            self.x_controle = -self.velocidade
            self.y_controle = 0

    def move_right(self):
        if self.x_controle == 0:
            self.x_controle = self.velocidade
            self.y_controle = 0

    def move_up(self):
        if self.y_controle == 0:
            self.x_controle = 0
            self.y_controle = -self.velocidade

    def move_down(self):
        if self.y_controle == 0:
            self.x_controle = 0
            self.y_controle = self.velocidade
