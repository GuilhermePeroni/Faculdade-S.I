#  Guia Completo de Listas em Python

# 1. O que é uma lista
# Lista é uma coleção ordenada, mutável e que aceita elementos de qualquer tipo.
# É o tipo de estrutura de dados mais usado em Python.

# Criada com [] ou com list(). 

# Exemplo:
frutas = ['maçã', 'banana', 'uva']
numeros = [1, 2, 3, 4, 5]
mistura = [1, 'oi', True, 3.5]

# 2. Criando listas
vazia = []  # lista vazia
numeros = [10, 20, 30]  # com valores
palavra = list('Python')  # ['P', 'y', 't', 'h', 'o', 'n']

# 3. Acessando elementos. 
# Índices começam do 0.
frutas = ['maçã', 'banana', 'uva']
frutas[0]  # maçã
frutas[-1] # uva (índice negativo começa do final)

# 4. Alterando elementos
# Listas são mutáveis, você pode trocar valores.
frutas = ['maçã', 'banana', 'uva']
frutas[1] = 'laranja'
print(frutas)  # ['maçã', 'laranja', 'uva']

# 5. Operações básicas
lista = [1, 2, 3]
len(lista)     # tamanho da lista -> 3
2 in lista     # True (verifica se o 2 está na lista)
lista + [4, 5] # concatenação -> [1, 2, 3, 4, 5]
lista * 2      # repete -> [1, 2, 3, 1, 2, 3]

# 6. Métodos de listas
# append(x)  -> adiciona x no final
# insert(i,x)-> insere x na posição i
# extend(l2) -> junta outra lista
# remove(x)  -> remove primeira ocorrência
# pop(i)     -> remove e retorna índice i
# clear()    -> esvazia lista
# index(x)   -> retorna índice de x
# count(x)   -> conta ocorrências
# sort()     -> ordena lista
# reverse()  -> inverte lista
# copy()     -> copia lista

# 7. Fatiamento (slicing)
letras = ['a','b','c','d','e']
letras[1:4]  # ['b','c','d']
letras[:3]   # ['a','b','c']
letras[2:]   # ['c','d','e']
letras[::2]  # ['a','c','e']

# 8. Iterando listas
for fruta in ['maçã','banana','uva']:
    print(fruta)

for i, fruta in enumerate(['maçã','banana','uva']):
    print(i, fruta)

# 9. List Comprehension
numeros = [x for x in range(5)]            # [0,1,2,3,4]
pares = [x for x in range(10) if x%2==0]  # [0,2,4,6,8]
quadrados = [x**2 for x in range(5)]      # [0,1,4,9,16]

# 10. Funções úteis
numeros = [5, 3, 8, 1]
max(numeros)  # 8
min(numeros)  # 1
sum(numeros)  # 17
sorted(numeros)  # [1, 3, 5, 8]

# 11. Listas aninhadas
matriz = [[1, 2, 3],[4, 5, 6]]
matriz[0][1]  # 2

# 12. Cópias de listas
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1,2,3,4] (b alterou a!)

b = a.copy()  # forma correta
b = a[:]      # outra forma de copiar
