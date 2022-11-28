#Thomas Chubb#
#11/06/2022#
#Chubb-HiLoGame#
#A simpe number guessing game#
import random
replay = True
while replay:
    range_play = int(input('What should the maximum number for this game be?: '))
    random_number = random.randint(1,range_play)
    player_guess = int(input("Guess my number: "))
    game_complete = False 
    while game_complete == False:
        if player_guess == random_number:
            print(f'You guessed my number!')
            break
        elif player_guess > random_number:
            print(f'your guess is too high.')
            player_guess = int(input("Guess my number"))
        elif player_guess < random_number:
            print(f'your guess is too low')
            player_guess = int(input("Guess my number."))
        else: 
            player_guess == random_number
            print(f'You guessed my number!')
            game_complete = True

    play_again = input('Would you like to play again? (Y/N):')
    if play_again == 'n' or play_again == 'N':
        replay = False
    else: 
        play_again == 'y' or play_again == 'Y'
        replay = True