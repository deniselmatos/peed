"""Crie um programa que leia um número do usuário e determine se esse número é par ou ímpar."""
n = float(input(" Digite um número: "))
if n % 2 == 0:
    print(f" {n} é par")
else:
    print(f" {n} é ímpar")