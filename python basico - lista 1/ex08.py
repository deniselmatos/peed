"""Crie um programa que leia uma lista de números do usuário e exiba o maior número dessa lista."""
lista = []

tam = int(input(" Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(f" Digite o número {i+1}: "))
    lista.append(n)

maior = max(lista)

print(f" O maior número da lista é: {maior}")
