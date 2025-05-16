import random  # Import the random module for computer's random choice

def get_user_choice(player_name):
    # Randomly select and return 'rock', 'paper', or 'scissors' for the user
    choice = random.choice(['rock', 'paper', 'scissors'])
    print(f"{player_name}, your choice (randomly selected): {choice.random.choice(['rock','paper','sc'])}")
    return choice  # Return the randomly selected choice

def get_computer_choice():
    # Randomly select and return 'rock', 'paper', or 'scissors' for the computer
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winners(choices):
    # Count how many times each choice appears among all players
    counts = {choice: list(choices.values()).count(choice) for choice in set(choices.values())}
    # If all players chose the same or all chose differently, it's a tie
    if len(counts) == 1 or len(counts) == 3:
        return [], "It's a tie!"
    # Determine the winning choice based on the rules
    if counts.get('rock', 0) == 1 and counts.get('scissors', 0) == 1:
        winner_choice = 'rock'
    elif counts.get('paper', 0) == 1 and counts.get('rock', 0) == 1:
        winner_choice = 'paper'
    elif counts.get('scissors', 0) == 1 and counts.get('paper', 0) == 1:
        winner_choice = 'scissors'
    else:
        return [], "It's a tie!"
    # List all players who chose the winning option
    winners = [name for name, choice in choices.items() if choice == winner_choice]
    return winners, f"{', '.join(winners)} win(s)!"

def play_game():
    print("Welcome to 3-Player Rock, Paper, Scissors!")  # Greet the players
    players = ["Player 1", "Player 2", "Computer"]  # Define the three players
    points = {name: 0 for name in players}  # Initialize points for each player
    rounds = int(input("How many rounds would you like to play? "))  # Ask for number of rounds
    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")  # Display round number
        # Randomly select choices for all players
        choices = {
            "Player 1": get_user_choice("Player 1"),
            "Player 2": get_user_choice("Player 2"),
            "Computer": get_computer_choice()
        }
        # Show each player's choice
        for name, choice in choices.items():
            print(f"{name} chose: {choice}")
        # Determine winners and print result
        winners, result = determine_winners(choices)
        print(result)
        # Award points to each winner
        for winner in winners:
            points[winner] += 1
    print("\nFinal Points:")  # Display final scores after all rounds
    for name, score in points.items():
        print(f"{name}: {score}")

if __name__ == "__main__":
    play_game()  # Start the game if the script is run directly