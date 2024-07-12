"""Crie um programa que leia uma lista de números do usuário e exiba a lista ordenada em ordem crescente."""
lista = []

tam = int(input(" Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(" Digite um número: "))
    lista.append(n)

lista.sort()

print(f" A lista ordenada em ordem crescente: ")

for item in lista:
    print(f"{item}")
    