'''Elaborar um programa que leia o nome completo de um aluno. Valide o nome para que seja composto.
Exiba apenas o primeiro nome do aluno em letras maiúsculas. '''

nome = input("Nome completo: ")

while nome.find(" ") == -1:
    nome = input("Digite nome completo: ")

partes = nome.split(" ")

print(f'{partes[0].upper()}')