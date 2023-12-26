##
##  Guess The Number Game
##


import random


## User Name and Intro to the Game

print('Hello, what is your name?')
name = input()
secretNumber = random.randint(1, 20)
print('Well, '+name+', I am thinking of a number between 1 and 20.')


##  Processing

for time in range(1,7):
    
    print('Take a guess.')
    number = input()
        
    if int(number) > secretNumber:
        print('Too high, try again.')
        
    elif int(number) < secretNumber:
        print('Too low, try again.')
    else:
        break

if int(number) == secretNumber:
    print('Congratulations. You got it in '+str(time)+' attempt(s).')     
else:
    print('Nope, the number I was thinking of is '+str(secretNumber))
    
