import random as rd
print("                                             ---------WELCOME---------")

def get_inputs():
    player_score = 0
    computer_score = 0
    player_name = input("Enter your name: ")
    rounds=int(input("Enter the number of rounds you want to play"))
    
    count = 0
    options = ["rock", "paper", "scissors"]
    while count < rounds:
        print("\n")
        player_choice = input(f"{player_name} enter your choice (rock or paper or scissors): ")
        computer_choice = rd.choice(options)
        print(f"{player_name}'s choice is {player_choice} and computer choice is {computer_choice}")
        final_result = check_choices(player_choice, computer_choice, player_name)  
        print(final_result)
        player_score, computer_score = update_scores(final_result, player_score, computer_score)  
        count += 1
    print("\nFinal Scores: ")
    print(f"{player_name} Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    declare_winner(player_score, computer_score, player_name) 
    play_again()

def check_choices(player, computer, player_name):  
    if player == computer:
        return "It's a tie\n"
    elif player == "scissors":
        if computer == "rock":
            return f"Rock smashes scissors!! Computer wins\n"
        elif computer == "paper":
            return f"Scissors cuts paper!! {player_name} wins\n"
    elif player == "rock":
        if computer == "paper":
            return f"Paper covers rock!! Computer wins\n"
        elif computer == "scissors":
            return f"Rock smashes scissors!! {player_name} wins\n"
    elif player == "paper":
        if computer == "rock":
            return f"Paper covers rock!! {player_name} wins\n"
        elif computer == "scissors":
            return f"Scissors cuts paper!! Computer wins\n"
    return "Invalid choice"  

def update_scores(result, player_score, computer_score):
    if "wins" in result:
        if "Computer wins" in result:
            computer_score += 1
        else:
            player_score += 1
    return player_score, computer_score

def declare_winner(player_score, computer_score, player_name):  
    if player_score > computer_score:
        print(f"                                            *****{player_name} wins the game*****")
    elif computer_score > player_score:
        print("                                             *****Computer wins the game*****")
    else:
        print("                                             *****It's a Tie Match*****")

def play_again():
    print("\n")
    again = input("Do you want to play again? (yes/no): ")
    if again == 'yes':
        get_inputs()
    else:
        print("                                             *****Thanks for playing*****")
    print("\n")

get_inputs()
