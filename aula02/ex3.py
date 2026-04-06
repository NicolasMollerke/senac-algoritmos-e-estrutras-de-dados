'''
Elaborar um programa que leia o nome de um produto e o número de etiquetas a serem
impressas desse produto. Exiba as etiquetas com o nome do produto, com no máximo 2 etiquetas
por linha, conforme exemplo de execução do programa, demonstrado a seguir
'''

produto = input("Nome do produto: ")
etiquetas = int(input("Número de etiquetas: "))
cont = 0

for i in range(0, etiquetas):
    print(f'{produto}', end="    ")
    cont += 1
    if cont % 2 == 0:
        print("\n")
