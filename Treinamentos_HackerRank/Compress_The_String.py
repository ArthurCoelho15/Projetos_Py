"""

HackerRank: https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true

Faça um programa que leia uma string e agrupe-a mostrando a quantidade de termos agrupados, utilize o groupby importando o intertools
    - Ex:
        input -> 11122311444       ->      (111 22 3 11 444) <- [para ficar melhor visualmente para entender, o agrupamento é esse]
        output -> (3, 1) (2, 2) (1, 3) (2, 1) (3, 4)
"""

from itertools import groupby

nome = str(input())
agrupado = groupby(nome)

for num, grupo in agrupado:
    print(f'({len(list(grupo))}, {num}) ', end='')
