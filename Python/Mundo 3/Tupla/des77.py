#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quiais são suas vogais.

palavras = ('casa', 'carro','manha', 'comida','sapato', 'escritorio','uva')

for vogal in palavras:
    print(f'\nA palavra {vogal.upper()} tem essas vogais: ', end='')
    for letra in vogal:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
print(f'\nFim das palavras')

