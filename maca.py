# maca.py
import pygame
from random import randint

class Maca(pygame.sprite.Sprite):
    def __init__(self, largura, altura):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (randint(40, largura - 40), randint(50, altura - 50))

    def desenhar(self, tela):
        tela.blit(self.image, self.rect)
