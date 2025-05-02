"""

HackerRank Link: https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true
HackerRank Link: https://www.hackerrank.com/challenges/a-very-big-sum/problem?isFullScreen=true

Faça um programa que leia uma entrada de numeros espaçados em um único input e imprima a sua soma
    Ex:
        = entrada: 1 2 3 4 5
        - programa: 1 + 2 + 3 + 4 + 5
        - saida: 15

"""


def soma(numeros):
    return sum(numeros)

size = int(input())

numeros = list(map(int, input().split()))

print(soma(numeros))
