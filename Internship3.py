import random

# getting user choice
def getting_user_choice():
    your_choice = input("Choose rock, paper, or scissor: ").lower()
    return your_choice
    
# generating random choice
def getting_comp_choice():
    return random.choice(["rock", "paper", "scissor"])
    
#conditions for winning and loosing
def determine_results(user, computer):
    if user == computer:
        return "Game Tied!"
    elif user == "rock" and computer == "scissor":
        return "You Win :)"
    elif user == "paper" and computer == "rock":
        return "You Win :)"
    elif user == "scissor" and computer == "paper":
        return "You Win :)"
    else:
        return "You Lose :("
        
# displaying result
def display_results(user, computer, results, user_score, computer_score):
    print("~" * 8)
    print("You Chose:", user)
    print("Computer Chose:", computer)
    print(results)
    print("Score Card:")
    print("User's Score:", user_score)
    print("Computer's Score:", computer_score)
    print("~" * 8)
    
# keeping track of the score
user_score = 0
computer_score = 0

while True:
    user = getting_user_choice()
    computer = getting_comp_choice()

    results = determine_results(user, computer)
    
    if "You Win :)" in results:
        user_score += 1
    elif "You Lose :(" in results:
        computer_score += 1

    display_results(user, computer, results, user_score, computer_score)
    
# asking user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again == "no":
        print("Thanks for playing!")
        break
