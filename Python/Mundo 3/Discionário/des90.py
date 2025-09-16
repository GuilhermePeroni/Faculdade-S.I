#Faça um programa que leia nome e média de umm aluno, guardando também a situação em um dicionário. No final, mostre o counteúdo da estrutura nna tela.

aluno = dict()

aluno['nome'] = str(input('Qual o seu nome?' ))
aluno['média'] = float(input('Qual foi sua média?' ))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'- Para {k} é igual a {v}')