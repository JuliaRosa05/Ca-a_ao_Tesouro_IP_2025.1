import pygame
import os

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (102, 0, 204)
VIBRANTGREEN = (50, 255, 50)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
DARKGREEN = (0, 200, 0)
BLUE = (140, 209, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BGCOLOUR = BLUE

LARGURA_JANELA = 1280
ALTURA_JANELA = 720

TAMANHO_QUADRADO = 96
LINHAS = 4
COLUNAS = 4
ALTURA_PAINEL = 50
QUANTIDADE_TESOUROS = 6
QUANTIDADE_BURACOS = 3

LARGURA_TABULEIRO = TAMANHO_QUADRADO * COLUNAS
ALTURA_TABULEIRO = TAMANHO_QUADRADO * LINHAS
LARGURA = LARGURA_JANELA
ALTURA = ALTURA_JANELA
FPS = 60
TITULO = "Caça ao tesouro-CDIA 2025.1 - Julia Rosa"

tile_numbers = []
for i in range(1,9):
    tile_numbers.append(pygame.transform.scale(pygame.image.load(os.path.join("assets", f"Tile{i}.png")), (TAMANHO_QUADRADO, TAMANHO_QUADRADO)))

tile_empty = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileEmpty.png")), (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
tile_exploded = pygame.transform.scale(pygame.image.load(os.path.join("assets", "TileExploded.png")), (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
tile_flag = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileFlag.png")), (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
tile_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileMine.png")), (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
tile_unknown = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileUnknown.png")), (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
tile_not_mine = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileNotMine.png")), (TAMANHO_QUADRADO, TAMANHO_QUADRADO))
tile_treasure = pygame.transform.scale(pygame.image.load(os.path.join("assets", f"TileTreasure.png")), (TAMANHO_QUADRADO, TAMANHO_QUADRADO))