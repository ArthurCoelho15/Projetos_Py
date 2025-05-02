import random
from collections import defaultdict


def repetidos(numeros):
    indices_repetidos = defaultdict(list)

    for i, num in enumerate(numeros):
        indices_repetidos[num].append(i)

    repetidos = {num: indice for num, indice in indices_repetidos.items() if len(indice) > 1}
    return repetidos

numeros = [random.randint(1, 100) for _ in range(50)]

repetidos = repetidos(numeros)

print(len(numeros))
print("Lista:", numeros)
for num, indice in repetidos.items():
    print(f"Número: {num}, índices: {indice}")
