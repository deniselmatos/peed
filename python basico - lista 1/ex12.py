"""Crie um programa que leia uma lista de números do usuário e exiba somente os números ímpares."""
lista = []
impares = []

tam = int(input(" Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(f" Digite o número {i+1}: "))
    lista.append(n)

for item in lista:
    if item % 2 != 0:
        impares.append(item)

if len(impares) != 0:
    print(f"\nOs números ímpares da lista são: ")
    for i in impares:
        print(f"{i}")
else:
    print("\nNenhum número ímpar foi informado")
