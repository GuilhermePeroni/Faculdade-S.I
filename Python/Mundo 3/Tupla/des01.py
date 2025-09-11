#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado entre (0 e 20) e mostrá-lo por extenso.

extenso = ('zero', 'um', 'dois', 'três','quatro','cinco')

numero= int(input('Me de um número de 0 a 5 que eu lhe devolvo por extenso: '))

print(f'O número foi {numero} e ele é escrito assim {extenso[numero]}')