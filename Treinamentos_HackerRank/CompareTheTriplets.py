"""

HackerRank Link: https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=true

Faça um programa que leia os números fornecidos por alice e por bob, em suas respectivas listas, em seguida compare os valores. Sua saída terá que ser a quantidade de vezes que o número de cada um foi maior
    - Ex:
        alice = [5 6 7]
        bob = [3 6 10]
        alice[0] > bob[0] -> 5 > 3 -> alice ganha 1 ponto (a recíproca é verdadeira)
        Saída = [pontos_aline pontos_bob]

"""

alice = 0
bob = 0

num_alice = list(map(int, input().split()))
num_bob = list(map(int, input().split()))


for i in range(0, len(num_alice)):
    if num_alice[i] == num_bob[i]:
        pass
    elif num_bob[i] > num_alice[i]:
        bob += 1
    else:
        alice += 1

print(alice, bob)