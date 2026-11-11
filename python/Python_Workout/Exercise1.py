import random 

def guessing_game():
    
    print(f"We are gonna generate a number between 1 and 10, lets see whether you can guess it")
    number = random.randint(1,10)
    while True:
        user_number = int(input())
        if user_number < number:
            print(f"Too small, keep trying")
        elif user_number > number:
            print(f"Too big, keep trying")
        else:
            print(f"Yeah that is the correct answer, the number is actually {number}")
            print(f"Do you wanna play again? Y or N")
            answer = input()
            if answer == 'y':
                guessing_game()
            elif answer == 'n':
                break    
        


guessing_game()