'''Elabore um programa de implemente um
jogo de Craps, conforme descrição a seguir: O
jogador lança um par de dados (2 números
aleatórios entre 1 e 6), obtendo um valor entre
2 e 12. Se, na primeira jogada, você tirar 7 ou
11, você tirou um "natural" e ganhou. Se você
tirar 2, 3 ou 12 na primeira jogada, isto é
chamado de "Craps" e você perdeu. Se, na
primeira jogada, você fizer um 4, 5, 6, 8, 9 ou
10, este é o seu "Ponto". Seu objetivo agora é
continuar jogando os dados até tirar este
número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este "Ponto" novamente.'''

import random
import time

d1 = random.randint(1, 6)
d2 = random.randint(1, 6)

print(f'Dado 1: {d1} \n')
print(f'Dado 2: {d2} \n')

soma = d1 + d2

print(f"Soma: {soma} \n")

time.sleep(1)

if soma == 7 or soma == 11:
    print("Voce ganhou")
elif soma == 2 or soma == 3 or soma == 12:
    print("Voce perdeu")
else:
    input("Pressione enter para continuar")
    ponto = soma
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    soma = d1 + d2
    print(f'Dado 1: {d1} \n')
    print(f'Dado 2: {d2} \n')
    print(f"Soma: {soma} \n")
    time.sleep(1)
    while soma != ponto:
        input("Pressione enter para continuar")
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        soma = d1 + d2
        print(f'Dado 1: {d1} \n')
        print(f'Dado 2: {d2} \n')
        print(f"Soma: {soma} \n")
        time.sleep(1)
        if soma == 7:
            print("Voce perdeu")
            break
    if soma == ponto:
         print("Voce venceu")
    
