nome = input("Nome do Aluno: ")
idade = int(input("Idade: "))
salario = float(input("Salário R$: "))

print("---------- Dados do Aluno ----------")
print(f"NOme do Aluno: {nome}")
print(f"Idade: {idade} anos")
print(f"Salário R$: {salario:9.2f}")

if idade < 18:
    print("Categoria: Juvenil")
    bonus = 300
elif idade < 60:
    print("Categoria: Adulto")
    bonus = 500
else:
    print("Categoria: Senior")
    bonus = 700

print(f"Você recebera um bonus de R$: {bonus:.2f}")

if idade >= 20 and idade <= 30:
    print("Haverá premiação especial para esta categoria")

