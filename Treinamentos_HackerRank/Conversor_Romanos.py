lista = []
resultado = []

size = int(input("Digite o tamanho da sua lista de números: "))

dict = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII",
        8: "VIII", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C",
        400: "CD", 500: "D", 900: "CM", 1000: "M" }

def roman(lista):
    for romanos in range(0, len(lista)):
        num = lista[romanos]
        if lista[romanos] not in dict:
            romano_numeral = ""
            for valor in sorted(dict.keys(), reverse=True):
                while num >= valor:
                    romano_numeral += dict[valor]
                    num -= valor
            lista[romanos] = romano_numeral
        else:
            lista[romanos] = dict.get(lista[romanos])
        print(f'O numero romano correspondente de {resultado[romanos]} é: {lista[romanos]}')
        #print(lista[romanos])

for i in range(0, size):
    n = int(input())
    lista.append(n)
    resultado = lista.copy()

roman(lista)
