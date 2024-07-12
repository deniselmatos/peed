"""Crie um programa que leia uma lista de números do usuário e exiba somente os números maiores do que 10."""
lista = []
maiores_10 = []

tam = int(input("Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(f"Digite o número {i+1}: "))
    lista.append(n)

for item in lista:
    if item > 10:
        maiores_10.append(item)

if len(maiores_10) != 0:
    print(f"Os números maiores do que 10 dentre os informados são: ")
    for i in maiores_10:
        print(f"{i}")
else:
    print("Nenhum número maior do que 10 foi informado")
        
