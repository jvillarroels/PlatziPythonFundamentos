'''
print("Hola, esto es python")

print("Hola soy Jose y tengo 12 años")
'''
# Operaciones matemáticas...
'''
print(12 + 5)  
print(10 - 5) 
print(2 * 3) 
print(8 / 2)
'''
# Esto es un comentario

"""
varias 
lineas 
otra
"""

'''
varias 
lineas
'''
import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

# while True:
while True:
    
    print('*' * 10)
    print('ROUND: ', rounds)
    print('COMPUTER_WINS: ', computer_wins)
    print('USER_WINS: ', user_wins)
    print('\n')
    
    user_option = input('Piedra, papel o tijera => ').lower()
    rounds += 1

    if not user_option in options:
        print('Esa opción no es válida')
        continue
    
    computer_option = random.choice(options)
    
    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('piedra gana a tijera')    
            print('\n')
            print('user wins!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('\n')
            print('Computer wins!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('papel gana a piedra')    
            print('\n')
            print('user wins!')
            user_wins += 1
        else:
            print('tijera gana a papel')
            print('\n')
            print('Computer wins!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('tijera gana a papel')    
            print('\n')
            print('user wins!')
            user_wins += 1
        else:
            print('piedra gana a tijera')
            print('\n')
            print('Computer wins!')
            computer_wins += 1

    print('\n')
    
    if computer_wins == 2:
        print('-' * 39)
        print('COMPUTER WINS THE GAME WITH ', computer_wins, ' POINTS !!!')
        break
    
    if user_wins == 2:
        print('-' * 39)
        print('USER WINS THEN GAME WITH ', user_wins, ' POINTS !!!')
        break
    
print('-' * 39)

