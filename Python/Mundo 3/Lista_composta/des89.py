#Crie um programa que leia nome e duas nota de vários alunos e guarde tudo em uma lista composta. 
# No final mostre um boletim conntendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

# Lista principal para armazenar os dados de todos os alunos
boletim = []

# Loop principal para cadastrar os alunos
while True:
    nome = input('Nome: ').strip().title()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    
    # Adiciona os dados do aluno à lista principal
    boletim.append([nome, [nota1, nota2], media])
    
    # Pergunta ao usuário se ele quer continuar
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar in 'N':
        break

# Exibe o cabeçalho do boletim
print('-' * 26)
print(f'{"Nº.":<4}{"NOME":<15}{"MÉDIA":>5}')
print('-' * 26)

# Exibe a lista de alunos e suas médias
for i, aluno in enumerate(boletim):
    print(f'{i:<4}{aluno[0]:<15}{aluno[2]:>5.1f}')

# Loop para permitir que o usuário veja as notas individuais
while True:
    print('-' * 35)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    
    # Verifica se a opção é válida
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if 0 <= opcao < len(boletim):
        print(f'Notas de {boletim[opcao][0]} são {boletim[opcao][1]}')
    else:
        print('Opção inválida. Tente novamente.')

print('<<< VOLTE SEMPRE >>>')