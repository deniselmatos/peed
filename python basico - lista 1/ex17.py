"""Crie um programa que leia uma lista de números do usuário e exiba a soma dos números ímpares."""
lista = []
soma = 0

tam = int(input(" Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(f" Digite o número {i+1}: "))
    lista.append(n)

for item in lista:
    if item % 2 != 0:
       soma += item

if soma:
    print(f" A soma dos números ímpares, dentre os informados é: {soma} ")
else:
    print(" Nenhum número ímpar foi informado")
