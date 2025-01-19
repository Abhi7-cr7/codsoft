import random


def play_game():
    """Play a game of Rock, Paper, Scissors"""

    choices = ["rock", "paper", "scissors"]

    while True:
        # Get player's choice
        print("\nRock, Paper, Scissors - Shoot!")
        player_choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()

        # Check for quit
        if player_choice == 'q':
            print("Thanks for playing!")
            break

        # Validate input
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Get computer's choice
        computer_choice = random.choice(choices)

        # Show choices
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("Computer wins!")


if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!")
    play_game()