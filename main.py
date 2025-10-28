import pygame
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO)
        self.clock = pygame.time.Clock()

        self.pontuacoes = {1: 0, 2: 0}
        self.vez_jogador = 1        
        self.vitoria = False
        self.font = pygame.font.SysFont("arial", 20)
        self.tabuleiro_x = (LARGURA - LARGURA_TABULEIRO) // 2
        self.tabuleiro_y = (ALTURA - ALTURA_TABULEIRO) // 2


    def new(self):
        self.board = Board()
        self.board.display_board()
        self.pontuacoes = {1: 0, 2: 0}
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
        pos_tabuleiro = (self.tabuleiro_x, self.tabuleiro_y)
        self.board.draw(self.screen, pos_tabuleiro)
        x_pos_instr = 20
        y_pos_instr = 15
        instrucoes = [
            "CAÇA AO TESOURO:",
            "  - Tesouro (100pts), buraco (-50pts, nunca fica negativo).",
            "  - Números são a dica de quantos tesouros estão ao redor.",
            "  - Botão direito para colocar/remover bandeira.",
            "  - Ao revelar todos os quadrados, clique em qualquer quadrado para reiniciar o jogo"
        ]

        for linha in instrucoes:
            texto_superficie = self.font.render(linha, True, BLACK)
            self.screen.blit(texto_superficie, (x_pos_instr, y_pos_instr))
            y_pos_instr += 25
        
        y_pos_score = y_pos_instr + 15
        texto_j1 = f"JOGADOR 1: {self.pontuacoes[1]} Pontos {'<-- SUA VEZ' if self.vez_jogador == 1 else ''}"
        texto_j2 = f"JOGADOR 2: {self.pontuacoes[2]} Pontos {'<-- SUA VEZ' if self.vez_jogador == 2 else ''}"
        
        superficie_j1 = self.font.render(texto_j1, True, PURPLE if self.vez_jogador == 1 else BLACK)
        superficie_j2 = self.font.render(texto_j2, True, PURPLE if self.vez_jogador == 2 else BLACK)

        self.screen.blit(superficie_j1, (x_pos_instr, y_pos_score))
        self.screen.blit(superficie_j2, (x_pos_instr, y_pos_score + 25))

        pygame.display.flip()

    def checa_vitoria(self):
        tesouros_encontrados = 0
        total_tesouros = 0
        for linha in self.board.board_list:
            for quadrado in linha: 
                if quadrado.type == "T":
                    total_tesouros += 1
                    if quadrado.revealed:
                        tesouros_encontrados += 1
        return tesouros_encontrados == total_tesouros and total_tesouros > 0


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
                        pontuacao_atual = self.pontuacoes[self.vez_jogador]
                        
                        if tipo_celula =="T":
                            pontuacao_atual += 100
                        elif tipo_celula =="B":
                            pontuacao_atual = max(0, pontuacao_atual - 50)
                            
                        self.pontuacoes[self.vez_jogador] = pontuacao_atual 
                    
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
                                 quadrado.revealed = True
                                 quadrado.flagged = False

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
