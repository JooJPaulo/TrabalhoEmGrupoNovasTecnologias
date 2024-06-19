import pygame
from random import randint

class Maca:
    def __init__(self, tela, largura, altura):
        self.tela = tela
        self.largura = largura
        self.altura = altura
        self.x = randint(40, largura - 40)
        self.y = randint(50, altura - 40)

    def desenhar(self):
        pygame.draw.rect(self.tela, (255, 0, 0), (self.x, self.y, 20, 20))

    def resetar(self):
        self.x = randint(40, self.largura - 40)
        self.y = randint(50, self.altura - 40)
