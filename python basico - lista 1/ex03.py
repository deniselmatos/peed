"""Crie um programa que leia um número do usuário e exiba a sua raiz quadrada."""
from math import sqrt

n = float(input(" Digite um número para calcular sua raiz quadrada: "))
raiz = sqrt(n)
print(f" A raiz de {n} é: {raiz}")
