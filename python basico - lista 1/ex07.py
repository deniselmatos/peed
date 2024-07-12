"""Crie um programa que leia uma lista de palavras do usuário e exiba a palavra mais longa."""
lista = []

tam = int(input(" Digite o tamanho da lista de palavras: "))

for i in range(tam):
    palavra = str(input(f" Digite a palavra {i+1}: "))
    lista.append(palavra)

maior = ""

for item in lista:
    if len(item) > len(maior):
        maior = item
   
print(f" A maior palavra da lista é: {maior}")
