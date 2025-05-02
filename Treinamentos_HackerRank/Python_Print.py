"""

HackerRank: https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

Faça um programa que leia um número e imprima todos os números até chegar nele
    -Ex:
        input = 5
        output = 12345

"""

size = int(input())
lista = []

def contador(size):
    for num in range(1, size + 1):
        lista.append(f'{num}')
    return lista

print(''.join(contador(size)))
