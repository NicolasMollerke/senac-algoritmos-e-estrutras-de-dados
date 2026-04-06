'''Uma palavra é dita palíndrome quando pode ser lida nos 2 sentidos. Elabore um programa que leia
uma palavra e informe se ela é ou não palíndrome.'''

palavra = input("Palavra: ")

verif = True
final = len(palavra) -1

for i in range(0, len(palavra) -1):
    if palavra[i] != palavra[final]:
        verif = False
    final -= 1

if verif:
    print("É palíndrome")            
else:
    print("Não é um palíndrome")
        