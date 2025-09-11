lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)
print(lanche[1]) # Acessando o segundo elemento
print(lanche[1:3]) # Acessando do segundo ao terceiro elemento
print(lanche[-2])   # Acessando o penúltimo elemento
print(lanche[1:]) # Acessando do segundo elemento até o final
print(lanche[:2])   # Acessando do início até o segundo elemento
print(lanche[-2:]) # Acessando do penúltimo elemento até o final

#for cont in range(0,len(lanche)):
    #print(f'Eu vou comer {lanche[cont]}')

# for comida in lanche: # Percorrendo os elementos da tupla
#     print(f'Eu vou comer {comida}')
# print('Comi pra caramba!')

for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida} em {pos+1}°')
print(len(lanche))
print(sorted(lanche))

print('---------------------------')

num = (2,3,5)
num1 = (2,3,5,9,3)
num2 = num + num1

print(num2)
print(len(num2))
print(num2.count(3))
print(num2.index(5))
# num2 = ()

# for i in num:
#     if (i in num2):
#         num2.append()
        