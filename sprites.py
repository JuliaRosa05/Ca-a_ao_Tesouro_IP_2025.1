import pygame
from settings import *
import random

class Tile:
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        self.x, self.y = x * TAMANHO_QUADRADO, y * TAMANHO_QUADRADO
        self.image = image
        self.type = type
        self.revealed = revealed
        self.flagged = flagged

    def draw(self,board_surface):
        if self.flagged and not self.revealed:
            board_surface.blit(tile_flag, (self.x, self.y))
        elif not self.revealed:
            board_surface.blit(tile_unknown, (self.x, self.y))
        else:
            board_surface.blit(self.image, (self.x,self.y))

    def __repr__(self):
        return self.type

class Board:
    def __init__(self):
        self.board_surface = pygame.Surface((LARGURA, ALTURA_TABULEIRO))
        self.board_list = [
            [Tile(col, row, tile_empty, ".") for col in range(COLUNAS)]for row in range(LINHAS)
            ]
        self.place_tesouros()
        self.place_buracos()
        self.place_dicas()
        self.cavado = []

    def place_tesouros(self):
        for _ in range(QUANTIDADE_TESOUROS):
            while True:
                x = random.randint(0, COLUNAS - 1)
                y = random.randint(0, LINHAS - 1)

                if self.board_list[y][x].type ==".":
                    self.board_list[y][x].image = tile_treasure
                    self.board_list[y][x].type = "T"
                    break


    def place_buracos(self):
        for _ in range(QUANTIDADE_BURACOS):
            while True:
                x = random.randint(0, COLUNAS - 1)
                y = random.randint(0, LINHAS -1)

                if self.board_list[y][x].type == ".":
                    self.board_list[y][x].image = tile_mine
                    self.board_list[y][x].type = "B"
                    break

    def place_dicas(self):
        for y in range(LINHAS):
            for x in range(COLUNAS):
                if self.board_list[y][x].type not in ["T","B"]:
                    total_tesouros = self. checa_vizinhos(y,x, target_type="T")
                    if total_tesouros > 0:
                        self.board_list[y][x].image = tile_numbers[total_tesouros-1]
                        self.board_list[y][x].type = "C"


    @staticmethod
    def esta_dentro(y,x):
        return 0<= y < LINHAS and 0 <= x < COLUNAS

    def checa_vizinhos(self, y, x, target_type="T"):
        total_items = 0
        for y_deslocado in range(-1, 2):
            for x_deslocado in range(-1,2):
                vizinho_y = y + y_deslocado
                vizinho_x = x + x_deslocado
                if self.esta_dentro(vizinho_y, vizinho_x) and self.board_list[vizinho_y] [vizinho_x].type == target_type: total_items += 1
        return total_items


    def draw(self,screen, pos=(0, 0)):
        self.board_surface.fill(LIGHTGREY)
        for row in self.board_list:
            for tile in row:
                tile.draw(self.board_surface)
        screen.blit(self.board_surface, pos)


    def cava(self, y, x):
        if (y, x) in self.cavado:
            return self.board_list[y][x].type
        
        self.cavado.append((y, x))
        cell_type = self.board_list[y][x].type

        self.board_list[y][x].revealed = True

        if cell_type =="B":
            self.board_list[y][x].image = tile_exploded
            return cell_type
        elif cell_type == "T":
            return cell_type
        elif cell_type == "C":
            return cell_type
        for vizinho_y in range(max(0, y - 1), min(LINHAS, y + 2)):
            for vizinho_x in range(max(0, x - 1), min(COLUNAS, x + 2)):
                if (vizinho_y, vizinho_x) != (y, x) and (vizinho_y, vizinho_x) not in self.cavado:
                    self.cava(vizinho_y, vizinho_x)
        return cell_type




    def display_board(self):
        for row in self.board_list:
            print(row)
