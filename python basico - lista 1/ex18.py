"""Crie um programa que leia uma lista de números do usuário e exiba o produto desses números."""
lista = []
prod = 1

tam = int(input(" Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(f" Digite o número {i+1}: "))
    lista.append(n)

for item in lista:
    prod *= item

print(f" O produto dos números informados é: {prod} ")
