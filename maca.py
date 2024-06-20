import pygame
from random import randint


class Maca:

    def __init__(self, largura, altura):
        self.x = randint(40, largura - 40)
        self.y = randint(50, altura - 50)

    def desenhar(self, tela):
        pygame.draw.rect(tela, (255, 0, 0), (self.x, self.y, 20, 20))
