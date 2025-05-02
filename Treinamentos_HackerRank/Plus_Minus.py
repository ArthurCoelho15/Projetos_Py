"""

HackerRank: https://www.hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

Faça um código que peça ao usuário a quantidade de itens para uma lista, após isso peça para digitar números,
em seguida imprima a razão da quantidade de números positivos, negativos e zeros da lista, imprima-os com 6 digitos após a vírgula (ponto).
    - Ex: quantidade = 5, numeros digitados: 1 1 0 -1 -1
        - Output:
                0.400000
                0.400000
                0.200000

"""

pos = 0
neg = 0
zero = 0

size = int(input())

n = list(map(int, input().split()))
out = []

def arredondar(out, n):
    for i in range(0, 3):
        print('{:.6f}'.format(out[i]/len(n)))


for question in range(0, size):
    out = []
    if n[question] > 0:
        pos += 1
    elif n[question] < 0:
        neg += 1
    else:
        zero += 1

out = [pos, neg, zero]

arredondar(out, n)
