#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em lista. No final mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

# Lista principal para armazenar os dados de todas as pessoas
pessoas = []
# Variáveis para rastrear o maior e o menor peso
maior_peso = menor_peso = 0

while True:
    nome = input('Nome: ')
    peso = float(input('Peso: '))

    # Adiciona a pessoa à lista principal
    pessoas.append([nome, peso])

    # A lógica para encontrar o maior e menor peso pode ser feita aqui
    if len(pessoas) == 1:
        maior_peso = menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso

    # Pergunta se o usuário deseja continuar
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar in 'N':
        break

print('-=' * 30)
# A) Quantas pessoas foram cadastradas
print(f'A) Ao todo, foram cadastradas {len(pessoas)} pessoas.')

# B) Listagem com as pessoas mais pesadas
print(f'B) O maior peso foi de {maior_peso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior_peso:
        print(f'[{p[0]}] ', end='')
print()

# C) Listagem com as pessoas mais leves
print(f'C) O menor peso foi de {menor_peso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor_peso:
        print(f'[{p[0]}] ', end='')
print()