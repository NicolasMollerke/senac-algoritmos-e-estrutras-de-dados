'''
Um número é dito perfeito, quando é igual a soma dos seus divisores (exceto com o próprio
número). Ler um número, exibir os seus divisores e informar se ele é ou não perfeito.
'''

numero = int(input("Numero: "))

soma = 0

for n in range(1, numero):
    if numero % n == 0:
        soma += n
        print(n)
    
if soma == numero:
    print(f'{numero} é um numero perfeito')
