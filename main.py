import pygame
from pygame.locals import *
from sys import exit
from cobra import Cobra
from maca import Maca

# Definição da classe Jogo
class Jogo:
    def __init__(self, largura, altura):
        pygame.init()

        self.largura = largura
        self.altura = altura
        self.pontos = 0
        self.fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption('Jogo')
        self.relogio = pygame.time.Clock()
        self.cobra = Cobra(largura, altura)
        self.maca = Maca(largura, altura)
        self.texto_formatado = self.fonte.render(f'Pontos: {self.pontos}', True, (0, 0, 0))

        self.key_mapping = {
            K_a: self.cobra.move_left,
            K_LEFT: self.cobra.move_left,
            K_d: self.cobra.move_right,
            K_RIGHT: self.cobra.move_right,
            K_w: self.cobra.move_up,
            K_UP: self.cobra.move_up,
            K_s: self.cobra.move_down,
            K_DOWN: self.cobra.move_down,
        }

    def rodar(self):
        while True:
            self.relogio.tick(30)
            pygame.event.pump()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    action = self.key_mapping.get(event.key)
                    if action:
                        action()

            self.cobra.mover()
            self.cobra.verificar_colisao()

            if pygame.sprite.collide_rect(self.cobra, self.maca):
                self.maca = Maca(self.largura, self.altura)
                self.pontos += 1
                self.cobra.comprimento_inicial += 1
                self.texto_formatado = self.fonte.render(f'Pontos: {self.pontos}', True, (0, 0, 0))

            if self.cobra.morreu:
                self.mostrar_mensagem('Game Over! Pressione R para jogar novamente')
                self.reiniciar_jogo()

            self.tela.fill((255, 255, 255))  # Clear the screen
            self.cobra.aumenta_cobra(self.tela)
            self.maca.desenhar(self.tela)
            self.tela.blit(self.texto_formatado, (450, 40))

            pygame.display.update()

    def mostrar_mensagem(self, mensagem):
        texto = self.fonte.render(mensagem, True, (0, 0, 0))
        rect = texto.get_rect(center=(self.largura / 2, self.altura / 2))
        self.tela.blit(texto, rect)
        pygame.display.update()

    def reiniciar_jogo(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN and event.key == K_r:
                    self.cobra.reiniciar()
                    self.pontos = 0
                    self.texto_formatado = self.fonte.render(f'Pontos: {self.pontos}', True, (0, 0, 0))
                    return
                
if __name__ == "__main__":
    jogo = Jogo(800, 600)
    jogo.rodar()