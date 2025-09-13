#Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular. 

tabela = ('Uva', 2.99, 'Banana', 4.98, 'Maça', 3.45, 'Morango', 4, 'Melancia', 3.99)

print('-' * 40)
print(f'{"TABELA DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0,len(tabela)):
    if pos % 2 == 0:
        print(f'{tabela[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R${tabela[pos]:>8.2f}')
print('-' * 40)