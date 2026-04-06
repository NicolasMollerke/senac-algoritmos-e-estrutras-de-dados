import os


palavras = []
dicas = []


def incluir_palavras():
    palavra = input("Digite a plavra a ser adicionada: ")
    palavras.append(palavra)
    dica = input("Digite a dica para a palavra: ")
    dicas.append(dica)

def listar():
    for i in range (0, len(palavras)):
        print(f"{i+1}. {palavras[i]} - {dicas[i]} \n")

def alterar_dica():
    listar()
    selec = int(input("Escolha a dica que voce quer alterar: "))
    dicas[selec-1] = input("Altere a dica: ")

def excluir_palavra():
    listar()
    selec = int(input("Escolha a palavra que voce quer excluir: "))
    palavras.pop(selec-1)
    dicas.pop(selec-1)

def ordenar_palavras():
    junto = sorted(zip(palavras, dicas))
    print(junto)

def salvar_arquivo():
    with open("forca.txt", "w") as arq:
        for palavras, dicas in zip (palavras, dicas):
            arq.write(f"{palavras}; {dicas}\n")

def carregar_dados():
    if not os.path.isfile("forca.txt"):
        return
    
    with open("forca.txt", "w") as arq:
        dados = arq.readlines()

        for linha in dados:
            partes = linha.split(";")
            palavras.append(partes[0])
            dicas.append(partes[1])

while True:
    print()
    print("1. Incluir Palavra")
    print("2. Litar Palavras")
    print("3. Alterar Dica")
    print("4. Excluir Palavra")
    print("5. Listar Palavras em Ordem")
    print("6. Incluir Palavra")

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        incluir_palavras()
    if escolha == 2:
        listar()
    if escolha == 3:
        alterar_dica()
    if escolha == 4:
        excluir_palavra()
    if escolha == 5:
        ordenar_palavras()
    if escolha == 6:
        salvar_arquivo()
        break

