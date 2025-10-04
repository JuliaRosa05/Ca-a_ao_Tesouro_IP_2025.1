import pygame
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO)
        self.clock = pygame.time.Clock()

        self.pontuação = 0
        self.vez_jogador = 1
        self.vitoria = False
        self.font = pygame.font.SysFont("arial", 20)
        self.tabuleiro_x = (LARGURA - LARGURA_TABULEIRO) // 2
        self.tabuleiro_y = (ALTURA - ALTURA_TABULEIRO) // 2


    def new(self):
        self.board = Board()
        self.board.display_board()
        self.pontuação = 0
        self.vez_jogador = 1

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.draw()
        else: 
            self.end_screen()

    def draw(self):
        self.screen.fill(BGCOLOUR)
        self.board.draw(self.screen, (self.tabuleiro_x, self.tabuleiro_y))
        y_pos_texto = self.tabuleiro_y +  ALTURA_TABULEIRO + 15
        x_pos_texto = self.tabuleiro_x
        texto_status = f"Jogador {self.vez_jogador} | Pontuação: {self.pontuação}"
        texto_superficie = self.font.render(texto_status, True, WHITE)
        self.screen.blit(texto_superficie, (x_pos_texto, y_pos_texto))

        pygame.display.flip()

    def checa_vitoria(self):
        for linha in self.board.board_list:
            for quadrado in linha:
                if not quadrado.revealed:
                    return False
        return True


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
    
            if event.type == pygame.MOUSEBUTTONDOWN:    
                mx, my = pygame.mouse.get_pos()
                mx_tab = mx - self.tabuleiro_x
                my_tab = my - self.tabuleiro_y
                mx_tile = mx_tab // TAMANHO_QUADRADO
                my_tile = my_tab // TAMANHO_QUADRADO

                if 0 <= mx_tile < COLUNAS and 0 <= my_tile < LINHAS:
                    quadrado_clicado = self.board.board_list[my_tile][mx_tile]

                if event.button == 1:
                    if not quadrado_clicado.flagged and not quadrado_clicado.revealed:         
                        tipo_celula = self.board.cava(my_tile,mx_tile)
                        if tipo_celula =="T":
                            self.pontuação += 100
                        elif tipo_celula =="B":
                            self.pontuação = max(0,self.pontuação - 50)

                        self.vez_jogador = 3 - self.vez_jogador
        
                if event.button == 3:
                    if not self.board.board_list[my_tile][mx_tile].revealed:
                        self.board.board_list[my_tile][mx_tile].flagged = not self.board.board_list[my_tile][mx_tile].flagged

                if self.checa_vitoria():
                    self.vitoria = True
                    self.playing = False
                    for linha in self.board.board_list:
                        for quadrado in linha:
                            if not quadrado.revealed:
                                quadrado.flagged = True

    def end_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit(0)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    return

game = Game()
game.running = True 
while game.running:
    game.new()
    game.run()

pygame.quit()
quit(0)
