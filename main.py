import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, K_r
from sys import exit
from maca import Maca
from cobra import Cobra


# Definição da classe Jogo
class Jogo:
    def __init__(self, largura, altura):
        pygame.init()

        self.largura = largura
        self.altura = altura
        self.pontos = 0
        self.fonte = pygame.font.SysFont("arial", 40, bold=True, italic=True)
        self.tela = pygame.display.set_mode((largura, altura))
        pygame.display.set_caption("Jogo")
        self.relogio = pygame.time.Clock()
        self.cobra = Cobra(largura, altura)
        self.maca = Maca(largura, altura)
        self.morreu = False

    def rodar(self):
        while True:
            self.relogio.tick(30)
            self.tela.fill((255, 255, 255))

            mensagem = f"Points: {self.pontos}"
            texto_formatado = self.fonte.render(mensagem, True, (0, 0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        if self.cobra.x_controle == self.cobra.velocidade:
                            pass
                        else:
                            self.cobra.x_controle = -self.cobra.velocidade
                            self.cobra.y_controle = 0
                    if event.key == K_RIGHT:
                        if self.cobra.x_controle == -self.cobra.velocidade:
                            pass
                        else:
                            self.cobra.x_controle = self.cobra.velocidade
                            self.cobra.y_controle = 0
                    if event.key == K_UP:
                        if self.cobra.y_controle == self.cobra.velocidade:
                            pass
                        else:
                            self.cobra.y_controle = -self.cobra.velocidade
                            self.cobra.x_controle = 0
                    if event.key == K_DOWN:
                        if self.cobra.y_controle == -self.cobra.velocidade:
                            pass
                        else:
                            self.cobra.y_controle = self.cobra.velocidade
                            self.cobra.x_controle = 0

            self.cobra.mover()
            self.cobra.verificar_colisao()

            if pygame.Rect(self.cobra.x, self.cobra.y, 20, 20).colliderect(
                pygame.Rect(self.maca.x, self.maca.y, 20, 20)
            ):
                self.maca = Maca(self.largura, self.altura)
                self.pontos += 1
                self.cobra.comprimento_inicial += 1

            if self.cobra.morreu:
                self.mostrar_mensagem("Game Over! Press R to play again")
                self.reiniciar_jogo()

            self.cobra.aumenta_cobra(self.tela)
            self.maca.desenhar(self.tela)
            self.tela.blit(texto_formatado, (10, 10))

            pygame.display.update()

    def mostrar_mensagem(self, mensagem):
        fonte2 = pygame.font.SysFont("arial", 20, True, True)
        texto_formatado = fonte2.render(mensagem, True, (0, 0, 0))
        ret_texto = texto_formatado.get_rect()
        ret_texto.center = (self.largura // 2, self.altura // 2)
        self.tela.blit(texto_formatado, ret_texto)
        pygame.display.update()

    def reiniciar_jogo(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        self.cobra.reiniciar()
                        self.pontos = 0
                        return


# Inicialização do jogo
if __name__ == "__main__":
    jogo = Jogo(640, 480)
    jogo.rodar()
