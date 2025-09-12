# Crie um programa que vai gerar cinco numeros aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de numeros gerados e tambem o menor e o maior valor que estão na tupla.

from random import randint

numeros = tuple(randint(1,20) for n in range(0,5))
print('\n')
print(f'Lista dos numeros:')
print(sorted(numeros))

semrep = sorted(tuple(set(numeros)))
# Imprime a lista sem números repetidos
print('\nLista sem números repetidos:')
print(semrep)

print('\n')
print(f'Lista sem números repetidos:\n')
print(f'O maior valor foi: {max(numeros)}')

print('\n')
print(f'Lista sem números repetidos:\n')
print(f'O menor valor foi: {min(numeros)}')

