"""

HackerRank: https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true

Faça um programa que lê uma lista de 5 números e imprima o valor minimo da soma entre eles e o valor máximo.
    - Ex: 1 2 3 4 5
        - lista máxima: 2 3 4 5 (exclui o primeiro valor) -> 2 + 3 + 4 + 5 = 14
        - lista mínima: 1 2 3 4 (exclui o último valor) -> 1 + 2 + 3 + 4 = 10
        Output: [min max] -> 10 14
"""


n = list(map(int, input().split()))
n.sort()
m = n.copy()

def max(n):
    n.pop(0)
    return sum(n)


def min(m):
    m.pop(4)
    return sum(m)

print(f'{min(m)} {max(n)}')
