#Jeu de devinettes en gros tu dois deviner le nombre choisi par l'ordinateur ;)

import random

nbr_secret = random.randint(1,1000)
invite = 'Choose a number : '
while True:
    nbr_joueur = raw_input(invite)
    if nbr_secret == int(nbr_joueur):
        print('You find it !!!')
        break
    elif nbr_secret > int(nbr_joueur):
        print('Too small')
    else:
        print('Too big')
