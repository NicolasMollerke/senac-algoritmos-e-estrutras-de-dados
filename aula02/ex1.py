'''
A entrada para um clube de pesca custa R$ 20,00 por pessoa e cada pessoa tem direito a levar um
peixe. Peixes extras custam 12,00. Elabore um programa que leia o número de pessoas de uma
família que foram ao clube e o número de peixes obtidos na pescaria. Informe o valor a pagar.
'''

pessoas = int(input("Número de pessoas: "))
peixes = int(input("Numero de peixes: "))

valor = 0

if peixes <= pessoas:
    valor = 20 * peixes
else:
    valor = (pessoas * 20) + ((peixes - pessoas) * 12)

print(f'Valor R$: {valor:.2f}')

