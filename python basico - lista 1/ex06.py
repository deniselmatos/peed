"""Crie um programa que leia uma lista de números do usuário e exiba a soma desses números."""
lista = []
soma = 0

tam = int(input(" Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(f" Digite o número {i+1}: "))
    lista.append(n)

for item in lista:
    soma += item

if soma:
    print(f" A soma dos números da lista é: {soma}")
else:
    print(" Valores inválidos/nulos")
    