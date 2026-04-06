'''Elaborar um programa que leia uma senha e informe se ela é válida ou não. Para ser válida a senha
deve conter letras maiúsculas, minúsculas e números. Além disso, a senha deve possuir entre 8 e 12
caracteres.'''

senha = input("Digite a senha: ")

if len(senha) < 8 and len(senha) > 12:
    print("Senha inválida")

num = False
min = False
mais = False

for i in range (0, len(senha)):
    if senha[i].isdigit():
        num = True
    if senha[i].islower():
        min = True
    if senha[i].isupper():
        mais = True

if num and min and mais:
    print("Senha válida")
else:
    print("Senha invalida")
    
