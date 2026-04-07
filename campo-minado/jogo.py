import random
import time
import os
from colorama import init, Fore

init(autoreset=True) #inicializa o colorama

jogo = []
apostas = []
pontos = 0

def preenche_matriz():
    for i in range(5):
        jogo.append([])
        apostas.append([])
        for _ in range(5):
            jogo[i].append("🟢")
            apostas[i].append("❌")
    
    bombas = 0
    while bombas < 3:
        linha = random.randint(0, 4)
        coluna = random.randint(0, 4)

        if jogo[linha][coluna] != "💣":
            jogo[linha][coluna] = "💣"
            bombas += 1

preenche_matriz()
# print(jogo)
# print(apostas)

def mostra_apostas():
    print("   1   2   3   4   5")
    for i in range(5):
        print(i+1, end="")
        for j in range(5):
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
                apostas[x][y] = jogo[x][y]
                break
            else:
                print("Coordenada já foi utilizada")
                time.sleep(2)
        except IndexError:
            print("Coordenada inválida. Repita")
            time.sleep(2)
    return x, y

bombas = 3

while True:
    x, y = faz_aposta()
    mostra_apostas()

    if jogo[x][y] == "🟢":
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

        
        