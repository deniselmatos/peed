"""Crie um programa que leia uma lista de números do usuário e exiba o menor número dessa lista."""
lista = []

tam = int(input(" Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(f" Digite o número {i+1}: "))
    lista.append(n)

menor = min(lista)

print(f" O menor número da lista é: {menor}")
