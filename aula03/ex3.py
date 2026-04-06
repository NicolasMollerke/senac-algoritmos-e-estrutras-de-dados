'''Elaborar um programa que leia uma palavra. Exiba a letra inicial (e suas ocorrências) e "_" nas demais
posições, conforme o exemplo.'''

palavra = input("Palavra: ")

ini = palavra[0].upper

for i in range(0, len(palavra)):
    if palavra[i].upper == ini:
        print(f'{palavra[i]}')
    else:
        print("_")


