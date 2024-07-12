"""Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem decrescente."""
lista = []

tam = int(input(" Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(f" Digite o número {i+1}: "))
    lista.append(n)

lista.sort(reverse=True)

print(f" A lista ordenada em ordem decrescente: ")

for item in lista:
    print(f"{item}")
    