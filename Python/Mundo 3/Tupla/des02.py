#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro, na ordem de colocação:
#Depois mostre:

#A) apenas os 5 primeiros.
#B) Os 4 últimos
#C) Lista com os time em ordem alfabetica
#D) em que posição na tabela está o time da Grêmio.

times = (
    "Flamengo",
    "Cruzeiro",
    "Palmeiras",
    "Bahia",
    "Botafogo",
    "Mirassol",
    "São Paulo",
    "Red Bull Bragantino",
    "Fluminense",
    "Internacional",
    "Ceará",
    "Corinthians",
    "Grêmio",
    "Atlético-MG",
    "Vasco da Gama",
    "Santos",
    "Vitória",
    "Juventude",
    "Fortaleza",
    "Sport"
)

#A

print(f'Os primeiros colocados:\n ')

for pos, time in enumerate(times[:4]):
    print(f'{pos+1}° colocado é o {time} ')
#B

print(f'\nZona de rebaixamento:\n')

for c in range(len(times)-4, len(times)):
    print(f'{c+1} ° colocado: {times[c]}')
print('\n')
#C
for t in sorted(times):
    print(t)

print('\n')
#D
print(f'O {times[12]} está na {times.index('Grêmio')+1}° colocado.')