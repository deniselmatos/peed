"""Crie um programa que leia uma lista de números do usuário e exiba somente os números menores do que 5."""
lista = []
menores_5 = []

tam = int(input("Digite o tamanho da lista de números: "))

for i in range(tam):
    n = float(input(f"Digite o número {i+1}: "))
    lista.append(n)

for item in lista:
    if item < 5:
        menores_5.append(item)

if len(menores_5) != 0:
    print(f"Os números menores do que 5 dentre os informados são: ")
    for i in menores_5:
        print(f"{i}")
else:
    print("Nenhum número menor do que 5 foi informado")
        