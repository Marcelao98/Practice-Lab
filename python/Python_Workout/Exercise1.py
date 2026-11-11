#Now this is an alternate version of the exercise, now the user only has three chances you see

import random 
def guessing_game():
    n = 0
    print(f"""We are gonna generate a number between 1 and 10, lets see whether you can guess it.
    You only have 3 attempts okay""")
    number = random.randint(1,10)
    while n < 3:
        user_number = int(input())
        if user_number < number:
            n = n+1
            print(f"Attemtpt number{n}, too small")
            
        elif user_number > number:
            n = n+1
            print(f"Attempt number{n}, too big")
            
        else:
            print(f"Yeah that is the correct answer, the number is actually {number}")
            print(f"Do you wanna play again? Y or N")
            answer = input()
            if answer == 'y':
                guessing_game()
            elif answer == 'n':
                break    
        


guessing_game()
#Just kidding, we weren't done with guessing just yet. 
