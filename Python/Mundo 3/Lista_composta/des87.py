#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) a maior valor da segunda linha.

matriz = []
soma_pares = 0
soma_terceira_coluna = 0
maior_segunda_linha = 0

# 1. Preenche a matriz e calcula a soma dos pares
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite um valor para a posição [{i}, {j}]: '))
        linha.append(valor)
        
        # A) Calcula a soma dos valores pares
        if valor % 2 == 0:
            soma_pares += valor
    matriz.append(linha)

# 2. Exibe a matriz formatada
print('-=' * 15)
for linha in matriz:
    for valor in linha:
        print(f'[{valor:^5}]', end='')
    print()

# 3. Processa os resultados
# B) Soma dos valores da terceira coluna
# A terceira coluna é o índice 2 em cada linha
for i in range(3):
    soma_terceira_coluna += matriz[i][2]

# C) O maior valor da segunda linha
# A segunda linha é o índice 1 na matriz
maior_segunda_linha = max(matriz[1])

# 4. Exibe os resultados finais
print('-=' * 15)
print(f'A) A soma de todos os valores pares digitados é: {soma_pares}')
print(f'B) A soma dos valores da terceira coluna é: {soma_terceira_coluna}')
print(f'C) O maior valor da segunda linha é: {maior_segunda_linha}')