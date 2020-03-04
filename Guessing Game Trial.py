import random

num = random.randint(1,100)
print ('1.If a players guess is less than 1 or greater than 100, say "OUT OF BOUNDS" \n2.On a players first turn, if their guess i \n 	within 10 of the number, return "WARM!"\n 	further than 10 away from the number, return "COLD!"\n3.On all subsequent turns, if a guess is \n 	closer to the number than the previous guess return "WARMER!"\n 	farther from the number than the previous guess, return "COLDER!"\n4.When the players guess equals the number, tell them theyve guessed correctly and how many guesses it took! ')

guesses = [0]

while True:

    
    guess = int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if guess < 1 or guess > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
   
    if guess == num:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!!')
        break
        
    guesses.append(guess)
    
    
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
        
    