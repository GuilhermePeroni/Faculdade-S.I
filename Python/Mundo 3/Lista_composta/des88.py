#Faça um programa que ajude um jogador da mega sena a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta;

from random import randint
from time import sleep

# Lista principal para armazenar todos os jogos
jogos = []

# Pergunta ao usuário quantos jogos ele quer gerar
print('-' * 30)
print(f'{"JOGOS PARA A MEGA SENA":^30}')
print('-' * 30)
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print(f'\n--- SORTEANDO {quantidade_jogos} JOGOS ---')
sleep(1)

# Loop para gerar a quantidade de jogos solicitada
for i in range(quantidade_jogos):
    jogo = []
    
    # Loop para sortear 6 números para cada jogo
    while len(jogo) < 6:
        numero_sorteado = randint(1, 60)
        
        # Garante que o número não se repita no mesmo jogo
        if numero_sorteado not in jogo:
            jogo.append(numero_sorteado)
    
    # Adiciona o jogo sorteado à lista principal de jogos
    jogos.append(jogo)
    
    # Exibe o jogo sorteado com um pequeno delay
    jogo.sort()
    print(f'Jogo {i+1}: {jogo}')
    sleep(0.5)

print('-=' * 15)
print(f'{"BOA SORTE!":^30}')