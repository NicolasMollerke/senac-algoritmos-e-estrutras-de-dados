import random
import time
import os
from colorama import init, Fore

init(autoreset=True) #inicializa o colorama

jogo = []
apostas = []
pontos = 0

def preenche_matriz():
    for i in range(9):
        jogo.append([])
        apostas.append([])
        for _ in range(9):
            jogo[i].append("🟢")
            apostas[i].append("❌")
    
    bombas = 0
    while bombas < 10:
        linha = random.randint(0, 8)
        coluna = random.randint(0, 8)

        if jogo[linha][coluna] != "💣":
            jogo[linha][coluna] = "💣"
            bombas += 1

preenche_matriz()
# print(jogo)
# print(apostas)

def mostra_apostas():
    print("   1   2   3   4   5   6   7   8   9")
    for i in range(9):
        print(i+1, end="")
        for j in range(9):
            print(f" {apostas[i][j]} ", end="")
        print("\n")

# mostra_apostas()

def faz_aposta():
    while True:
        mostra_apostas()
        posicao = input(f"Coordenada (linha e coluna): ")
        if len(posicao) != 2:
            print("Informe 2 digitos")
            time.sleep(3)
            continue
        x = int(posicao[0])-1
        y = int(posicao[1])-1
        try:
            if apostas[x][y] == "❌":
                cont = verifica_vizinhos(x, y)
                print(f"{cont} cont")
                if cont == 0:
                    revela_vizinhos(x, y)
                    apostas[x][y] = f" {cont}" #tive que colocar um espaço do lado do numero para não distorcer o tabuleiro
                else: 
                    apostas[x][y] = f" {cont}"
            else:
                print("Coordenada já foi utilizada")
                time.sleep(2)
        except IndexError:
            print("Coordenada inválida. Repita")
            time.sleep(2)
        
        return x, y

bombas = 10
cont = 0

def verifica_vizinhos(x, y):
    cont = 0

    for l in range(-1, 2): #-1 até 1
        for c in range(-1, 2):
            v_x = x + l
            v_y = y + c
            if l == 0 and c == 0: #coordenada que o jogador passou
                continue
            if 0 <= v_x < 9 and 0 <= v_y < 9: #faz com que o a linha 9 não seja considerada vizinha da 1
                if jogo[v_x][v_y] == "💣":
                    cont += 1

    return cont

def revela_vizinhos(x, y):
    for l in range(-1, 2): #-1 até 1
        for c in range(-1, 2):
            v_x = x + l
            v_y = y + c
            if 0 <= v_x < 9 and 0 <= v_y < 9: #faz com que o a linha 9 não seja considerada vizinha da 1
                apostas[v_x][v_y] = jogo[v_x][v_y]


while True:
    x, y = faz_aposta()
    mostra_apostas()

    if jogo[x][y] != "💣":
        pontos += 10
        os.system("cls")
        print("Parabéns, nenhuma bomba explodia!")
        print(f"Restam {bombas} bombas")
    else: 
        bombas -= 1
        os.system("cls")
        print("Opa... Você explodiu uma bomba!")

        if bombas == 0:
            print("Todas as bombas estouradas, seu jogo acabou")
            break

        
        