import random
import time
import sys

naipes = "♠♥♦♣"
extras = "JQKA"

baralho = []

def monta_baralho():
    #cartas de 2 a 10
    for i in range(2, 11):
        for naipe in naipes:
            #append: adicionar elemnetos à lista
            baralho.append(str(i)+naipe)

    #para as cartas com JQKA
    for extra in extras:
        for naipe in naipes:
            baralho.append(extra+naipe)

#chama a função monta_baralho
monta_baralho()
#print(baralho)

def verifica_pontos(carta):
    if len(carta) == 3: #10♠
        num = 10
    elif carta[0].isdigit(): #é um número
        num = int(carta[0])
    elif  carta[0] == "A":
        num = 11
    else:
        num = 10
    return num

contador = 0
pontos_jogador = 0

while True:
    #gera um numero aleatorio entre 0 e tam.baralho-1
    num = random.randint(0, len(baralho)-1)
    #pop(): para remover uma carta do baralho
    carta = baralho.pop(num)

    contador += 1
    print(f"Sua {contador} carta é: {carta}")
    time.sleep(2)

    pontos_jogador += verifica_pontos(carta)

    if pontos_jogador >= 21:
        break

    if contador >= 2:
        outra = input("Outra Carta (S/N)? ").upper()
        if outra == "N":
            break

print()
print("="*40)
print(f"==> Toal de Pontos do Jogador: {pontos_jogador}")
print("="*40)
print()

if pontos_jogador > 21:
    print("Bah... Voce perdeu. Tente outra vez")
    sys.exit()

##################### Jogada do Computador
contador = 0
pontos_pc = 0

while True:
    #gera um numero aleatorio entre 0 e tam.baralho-1
    num = random.randint(0, len(baralho)-1)
    #pop(): para remover uma carta do baralho
    carta = baralho.pop(num)

    contador += 1
    print(f"A {contador} Carta do Computador é: {carta}")
    time.sleep(2)

    pontos_pc += verifica_pontos(carta)

    if pontos_pc >= pontos_jogador or pontos_pc > 21:
        break

print()
print("="*40)
print(f"==> Toal de Pontos do Compitador: {pontos_pc}")
print("="*40)
print()

if pontos_pc > 21:
    print("Parabens! Voce Venceu!")
elif pontos_pc == pontos_jogador:
    print("Xi... Deu Empate!")
else:
    print("Voce Perdeu!")

