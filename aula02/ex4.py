'''
Digamos que o número de chinchilas de uma fazenda triplica a cada ano, após o primeiro ano.
Elaborar um programa que leia o número inicial de chinchilas e anos e informe ano a ano o número
médio previsto de chinchilas da fazenda. O número inicial de chinchilas deve ser maior ou igual a 2
(um casal). 
'''

numero = int(input("Numero de chinchilas: "))

while numero < 2:
    numero = int(input("Numero de chinchilas: "))

ano = int(input("Número de anos: "))

for i in range(0, ano):
    print(numero)
    numero = numero * 3