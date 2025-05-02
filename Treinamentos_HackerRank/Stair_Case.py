"""

HackerRank: https://www.hackerrank.com/challenges/staircase/problem?isFullScreen=true

Faça um código que crie uma escada com a quantidade de degraus inseridos pelo usuário
    - Ex: input = 6
        - Output: (os '-' devem ser espaços)
            -----#
            ----##
            ---###
            --####
            -#####
            ######
"""

size = int(input())

def stairs(size):
    for i in range(0, size):
        print(" "*(size-1-i) + "#" * (i + 1))

stairs(size)