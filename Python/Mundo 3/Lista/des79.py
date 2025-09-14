#Crie um programa onde o usuário possa digitar valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro. 
#ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

num=[]
while True:
    n=int(input('Digite um número: '))
    if n in num:
        print(f'Número {n} já foi inserido.')
    else:
        num.append(n)
    print('Continuar? [1-Sim/2-Não]')
    opcao=int(input(''))
    if (opcao == 2):
        break
print(sorted(num))