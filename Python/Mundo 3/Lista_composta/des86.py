#Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. 
#No final, mostre a matriz na tela, com formatação correta.
# Cria uma lista vazia para a matriz
matriz = []

# Loop para preencher a matriz 3x3 com valores do teclado
for i in range(3):
    linha = []  # Cria uma lista para a linha atual
    for j in range(3):
        # Solicita um valor e o adiciona à linha
        valor = int(input(f'Digite um valor para a posição [{i}, {j}]: '))
        linha.append(valor)
    matriz.append(linha)  # Adiciona a linha preenchida à matriz

# Exibe a matriz com formatação correta
print('-=' * 15)
for linha in matriz:
    for valor in linha:
        # Usa f-string para alinhar cada valor em um espaço de 5 caracteres
        print(f'[{valor:^5}]', end='')
    print()  # Quebra de linha após cada linha da matriz