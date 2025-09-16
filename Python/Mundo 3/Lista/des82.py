#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois, crie duas listas extras que vão conter apenas os valores pares e os valores impares.
#Ao final mostre o conteúdo das listas.

from random import randint
valores=[randint(1,30) for c in range(0,20)]
par=[]
impar=[]
for num in valores:
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f'Na lista original temos os números: {list(sorted(valores))}.')
print(f'Aqui estão os PARES: {par}')
print(f'Aqui estão os ÍMPARES: {impar}')