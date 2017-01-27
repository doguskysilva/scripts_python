# 5 hidroavioes de 1
# 4 submarinos de 2
# 3 cruzadoes de 3
# 2 encouraçados 4
# 1 porta-avioes 5

#tabuleiro 15 por 15

#3 jogadas por vez

from random import randint
import random
tamanho = 10

#navios = {1 : 5, 2 : 4, 3 : 3, 2 : 4, 5 : 1}
navios = {1 : 5, 2 : 4}
tamanho_navio = 0
quantidades_navio = 0
count = 0
pos_x = 0
pos_y = 0

rumo = []
rumo_escolhido = ''

tabuleiro = tamanho*[tamanho*[0]] # iniciando tabuleiro com 0 onde serão marcados numeros vazios
board = []

for x in range(tamanho):
    board.append([0] * tamanho)

def verificaposicao(x, y):
    return ;

def printTabuleiro(board):
    for show in board:
        print(show)
    return;


for navio in navios:
    count = count + 1
    tamanho_navio = navios[navio]
    quantidades_navio = navio
    print("-------------Navio de Tamanho %d------------------\n" % (tamanho_navio))

    for x in range(quantidades_navio):

        pos_x = 0
        pos_y = 0

        rumo = []
        rumo_escolhido = ''

        for y in range(tamanho_navio):
            #print("Parte => %d Navio =>  %d" % (y+1, x + 1))
            if y == 0:
                pos_x = randint(0, tamanho-1)
                pos_y = randint(0,tamanho-1)

                solta_ponto = False

                if(count == 1):
                    board[pos_y][pos_x] = tamanho_navio
                else:
                    while(solta_ponto == False):
                        if(board[pos_y][pos_x] == 0):


                            solta_ponto = True
                            board[pos_y][pos_x] = tamanho_navio




                print("Cabeca do Navio(%d, %d)" %(pos_x, pos_y))

                #verifica possibilidades de rumo
                if (0 + pos_x) >= (tamanho_navio-1):
                    rumo.append('E')
                if ((tamanho-1) - pos_x >= tamanho_navio-1): #defini verdade para cima
                    rumo.append("D")

                if (0 + pos_y) >= (tamanho_navio-1):
                    rumo.append("C")
                if ((tamanho-1) - pos_y >= tamanho_navio-1): #defini verdade para cima
                    rumo.append("B")
                #final do rumo

                #sorteio do rumo se necessário
                rumo_escolhido = random.choice(rumo)
                print("Rumos possiveis ",rumo)
                print("Rumo Escolhido",rumo_escolhido)
                print("")

            if y != 0:
                if rumo_escolhido == "C":
                    board[pos_y - 1][pos_x] = tamanho_navio
                    pos_y = pos_y - 1
                elif rumo_escolhido == "D":
                    board[pos_y][pos_x + 1] = tamanho_navio
                    pos_x = pos_x + 1
                elif rumo_escolhido == "B":
                    board[pos_y + 1][pos_x] = tamanho_navio
                    pos_y = pos_y + 1
                elif rumo_escolhido == "E":
                    board[pos_y][pos_x-1] = tamanho_navio
                    pos_x = pos_x - 1

            #verificaposicao(pos_x, pos_y)

printTabuleiro(board)
#print (rumo)