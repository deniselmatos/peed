"""Crie um programa que leia uma lista de números do usuário e exiba a média desses números."""
lista = []

tam = int(input(" Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(f" Digite o número {i+1}: "))
    lista.append(n)

media = sum(lista) / tam

print(f" A média dos números da lista é: {media:.2f}")
