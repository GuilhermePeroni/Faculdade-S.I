#Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quiais são suas vogais.

palavras = ('casa', 'carro','manha', 'comida','sapato', 'escritorio','uva')

for vogal in palavras:
    print(f'A palavra {vogal} tem essas vogais {vogal.count('a'), vogal.count('e'), vogal.count('i'), vogal.count('o'), vogal.count('u')}')
print(f'Fim das palavras')

