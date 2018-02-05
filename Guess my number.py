#this is to guess my number
import random, sys

print ('Hello, What\'s your name?')
name = input ()

print ('Hey,' + name + ' You wanna play guess the number game? Answer Yes or No')
answer = input ()


if answer == 'No':
    print ('Goodbye')
    sys.exit() 
else:
    print ('Great!' + name + ' I am thinking of a number between 1 to 20')
    secretnumber = random.randint(1,20)
    print ('Guess the number')
    guessednum = int (input())
    if guessednum < secretnumber:
        print ('That\'s too low')
    elif guessednum > secretnumber:
        print ('That\'s too high')
    else:
        print ('Awesome')

    for guessestaken in range (1,6):
        print ('Guess Again')
        guessednum = int (input ())
        if guessednum < secretnumber:
            print ('That\'s too low')
        elif guessednum > secretnumber:
            print ('That\'s too high')
        else:
            break

if guessednum == secretnumber:
    print ('Awesome ' + name+ ' You guessed the number in ' + str(guessestaken) + ' trials')
else:
    print ('Nope, I was thinking of ' + str  (secretnumber))
    

