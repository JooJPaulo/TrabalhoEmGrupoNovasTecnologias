import pygame

class Cobra:
    def __init__(self, tela, largura, altura, velocidade):
        self.tela = tela
        self.largura = largura
        self.altura = altura
        self.velocidade = velocidade

        self.x = int(largura / 2)
        self.y = int(altura / 2)
        self.x_controle = velocidade
        self.y_controle = 0

        self.lista_cobra = []
        self.comprimento_inicial = 5

    def mudar_direcao(self, x, y):
        if self.x_controle != -x or self.y_controle != -y:
            self.x_controle = x
            self.y_controle = y

    def atualizar(self):
        self.x += self.x_controle
        self.y += self.y_controle

        self.desenhar()

    def desenhar(self):
        for XeY in self.lista_cobra:
            pygame.draw.rect(self.tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))

        self.lista_cabeca = []
        self.lista_cabeca.append(self.x)
        self.lista_cabeca.append(self.y)
        
        self.lista_cobra.append(self.lista_cabeca)

        if len(self.lista_cobra) > self.comprimento_inicial:
            del self.lista_cobra[0]

    def aumentar(self):
        self.comprimento_inicial += 1

    def colisao_maca(self, maca):
        return pygame.Rect(self.x, self.y, 20, 20).colliderect(pygame.Rect(maca.x, maca.y, 20, 20))

    def verificar_colisao(self):
        cabeca = pygame.Rect(self.x, self.y, 20, 20)
        for segmento in self.lista_cobra[:-1]:
            if cabeca.colliderect(pygame.Rect(segmento[0], segmento[1], 20, 20)):
                return True
        if self.x > self.largura or self.x < 0 or self.y > self.altura or self.y < 0:
            return True
        return False

    def reiniciar(self):
        self.x = int(self.largura / 2)
        self.y = int(self.altura / 2)
        self.lista_cobra = []
        self.comprimento_inicial = 5
