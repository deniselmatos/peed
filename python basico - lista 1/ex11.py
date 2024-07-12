"""Crie um programa que leia uma lista de números do usuário e exiba somente os números pares."""
lista = []
pares = []

tam = int(input(" Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(f" Digite o número {i+1}: "))
    lista.append(n)

for item in lista:
    if item % 2 == 0:
        pares.append(item)

if len(pares) != 0:
    print(f"\nOs números pares da lista são: ")
    for i in pares:
        print(f"{i}")
else:
    print("\nNenhum número par foi informado")
        