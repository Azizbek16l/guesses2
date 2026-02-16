import random

n = random.randint(0, 10)
guess = int(input( "guess a number between 0 and 10: "))
            
guesses = 0
while True:
    if n==guess:
        print("toping")
        break
    
    if guesses>=3:
        print('yutqazding')
        break