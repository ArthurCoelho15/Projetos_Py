"""

HackerRank: https://www.hackerrank.com/challenges/birthday-cake-candles/problem?isFullScreen=true

Faça um programa de um bolo de aniversário onde peça a quantidade de velas e o tamanho delas,
o aniversariante deve apagar apenas as maiores velas, imprima a quantidade delas.
    - Ex: Quantidade = 4; tamanhos = [3 2 1 3]
    - Maiores velas = 3 -> Temos 2 velas com o tamanho 3
    - Output: 2

"""

from collections import Counter

size = int(input())

candles = list(map(int, input().split()))

qtd = Counter(candles)
chaves = qtd.values()

print(max(chaves))