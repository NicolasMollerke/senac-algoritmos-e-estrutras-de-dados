'''Elabore um programa que leia um e-mail de um aluno. Informe se o e-mail está em um formato válido
ou não. Para ser válido, o e-mail deve possuir um sinal de “@”, um ou mais pontos após o “@” e não
deve possuir espaços. E-mail: anamaria@senacrs.com.br Ok! E-mail em formato válido.
'''

email = input("Email: ")

arroba = email.find("@")
ponto = False
espaco = email.find(" ")

for i in range(arroba, len(email)):
    if email[i] == ".":
        ponto = True

if arroba != -1 and ponto and espaco == -1:
    print("Email valido")
else:
    print("Email invalido")
