import random

chances = 5
print('#'*25)
print('ADIVINHE O NÚMERO')


jogador  = input('Qual seu nome? ').capitalize()
print(f'Saudações, {jogador}! Você tem 5 chances de acertar o número que estou pensando entre 1 a 20.')
numero = random.randint(1, 20)
print(numero)

while (chances != numero):
  chances = chances - 1
  chute = int(input('\nEm qual número estou pensando? '))
  if (chute == numero):
    print(f'\nParabéns, {jogador}! Este era o número que eu estava pensando!')
    break
  elif (chances == 0):
    print(f'\nVocê perdeu, {jogador}!\nO número era {numero}.')
    break
  else:
    if (chute < numero):
      print(f'\nO número é maior! Tente novamente, {jogador}!\nChances: {chances}')
    else:
      print(f'\nO número é menor! Tente novamente, {jogador}!\nChances: {chances}')

print('\nGAME OVER')
print('#'*25)
