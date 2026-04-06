import random
import time

nome = input("Nome do apostador: ")
valor = float(input("Valor da Aposta R$: "))

input("Pressione Enter para iniciar")

figuras = "🍇🍓🥝"

jogo = ""

print("Suas Apostas: ", end="")

for i in range(3):
    num = random.randint(0, 2) # gera numero entre 0 e 2
    print(figuras[num], end="", flush=True) # flush força o printf a ser exibido
    time.sleep(1) # espera 1 sec
    jogo = jogo + figuras[num]

print()

conjunto = set(jogo)

if len(conjunto) == 1:
    premio = valor * 5
    print(f"Parabén {nome}! Voce ganhou R$ {premio:.2f}")
elif len(conjunto) == 2:
    print("Continue jogando")
else: 
    print("Não desista")
