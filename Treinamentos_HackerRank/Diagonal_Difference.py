"""
HackerRank Link: https://www.hackerrank.com/challenges/diagonal-difference/problem?isFullScreen=true

- Faça um programa que peça ao usuário a quantidade de linhas e colunas para uma matriz quadrada (linha = coluna),
em seguinda calcule a diferença, em módulo, da soma da diagonal principal e da soma da diagonal secundária.


"""

size = int(input())

linha = []
matriz = []
diag_principal = []
diag_secundaria = []

for i in range(0, size):
    linha = list(map(int, input().split()))
    matriz.append(linha)

for i in range(0, size):
    for j in range(0,size):
        if i == j:
            diag_principal.append(matriz[i][j])
        #else:
        diag_secundaria.append(matriz[j][size-(j+1)])

print(abs(sum(diag_principal[0:size]) - sum(diag_secundaria[0:size])))





