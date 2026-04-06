'''Elaborar um programa que leia ‘n’ números, até ser digitado 0. Ao final, exiba quantos números
foram digitados, a soma dos números e qual o maior número digitado.'''

num = int(input("Número: "))
cont = 0
soma = num

maior = num

while num != 0:
    num = int(input("Número: "))
    cont += 1
    soma += num
    if num > maior:
        maior = num

print(cont)
print(soma)
print(maior)