"""Crie um programa que leia uma lista de palavras do usuário e exiba somente as palavras que começam com a letra "a"."""
lista = []
inicial_a = []

tam = int(input("Digite o tamanho da lista de palavras: "))

for i in range(tam):
    palavra = str(input(f"Digite a palavra {i+1}: "))
    lista.append(palavra)

for item in lista:
    if item[0] == "A" or item[0] == "a":
        inicial_a.append(item)

if len(inicial_a) != 0:
    print(f" As palavras que começam com a letra \"a\", dentre as informadas:")
    for i in inicial_a:
        print(f"{i}")
else:
    print(f"Nenhuma palavra que começa com a letra \"a\" foi informada")
