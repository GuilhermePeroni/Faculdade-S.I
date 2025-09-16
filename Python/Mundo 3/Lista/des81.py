#Crie um programa que vai ler vários números e colocar em uma lista. 
#Depois disso, mostre:
#A) Quantos números fortam digitados:
#B) A liosta de valores ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.

valores=[]

while True:
    
    valores.append(int(input('Digite um valor: ')))
    
    print('Deseja continuar?')
    opcao= int(input('1 - Sim || 2 - Não'))
    if opcao == 2:
        break
print()

#A
print(f'Foram digitados {len(valores)} números.')
#B
print(f'Do maior ao menor:')
valores.reverse()
print(valores)
# OU
print(list(reversed(valores)))
#C
if 5 in valores:
    print(f'O número 5 está na lista.')
else:
    print('O valor 5 não se encontra na lista.')