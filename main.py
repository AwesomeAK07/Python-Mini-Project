import random

def play_snake_water_gun():
    """
    Snake Water Gun Game
    
    Game Rules:
    - Snake (1) beats Water (-1)
    - Water (-1) beats Gun (0) 
    - Gun (0) beats Snake (1)
    """
    
    # Define the game choices and their numeric values
    GAME_CHOICES = {
        "s": 1,    # Snake
        "w": -1,   # Water
        "g": 0     # Gun
    }
    
    # Dictionary to convert numbers back to readable names
    CHOICE_NAMES = {
        1: "Snake",
        -1: "Water", 
        0: "Gun"
    }
    
    # Get computer's random choice
    computer_choice = random.choice([-1, 0, 1])
    
    # Get player's choice
    print("Enter your choice:")
    print("s - Snake")
    print("w - Water") 
    print("g - Gun")
    
    player_input = input("Your choice: ").lower()
    
    # Validate player input
    if player_input not in GAME_CHOICES:
        print("Invalid choice! Please enter 's', 'w', or 'g'.")
        return
    
    player_choice = GAME_CHOICES[player_input]
    
    # Display both choices
    print(f"\nYou chose: {CHOICE_NAMES[player_choice]}")
    print(f"Computer chose: {CHOICE_NAMES[computer_choice]}")
    
    # Check for draw
    if computer_choice == player_choice:
        print("It's a draw!")
        return
    
    # Determine winner based on game rules
    if is_player_winner(player_choice, computer_choice):
        print("You win!")
    else:
        print("You lose!")

def is_player_winner(player_choice, computer_choice):
    """
    Check if player wins based on game rules:
    - Snake (1) beats Water (-1)
    - Water (-1) beats Gun (0)
    - Gun (0) beats Snake (1)
    """
    winning_combinations = [
        (1, -1),   # Snake beats Water
        (-1, 0),   # Water beats Gun
        (0, 1)     # Gun beats Snake
    ]
    
    return (player_choice, computer_choice) in winning_combinations

# Start the game
if __name__ == "__main__":
    play_snake_water_gun()