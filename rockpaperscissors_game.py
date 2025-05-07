import random

# Emoji choices
choices = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}

def get_user_choice(player_name):
    print(f"\n{player_name}, choose one:")
    for choice in choices:
        print(f"- {choice.capitalize()} {choices[choice]}")
    user_input = input(f"{player_name}'s choice: ").lower()
    while user_input not in choices:
        user_input = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    return user_input

def get_computer_choice():
    return random.choice(list(choices.keys()))

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "tie"
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "paper" and choice2 == "rock") or \
         (choice1 == "scissors" and choice2 == "paper"):
        return "player1"
    else:
        return "player2"

def play_round(player1, player2, is_vs_computer=False):
    choice1 = get_user_choice(player1)
    choice2 = get_computer_choice() if is_vs_computer else get_user_choice(player2)

    print(f"\n{player1} chose: {choice1.capitalize()} {choices[choice1]}")
    print(f"{player2} chose: {choice2.capitalize()} {choices[choice2]}")

    winner = determine_winner(choice1, choice2)
    if winner == "tie":
        print("⚖️ It's a tie!")
    elif winner == "player1":
        print(f"🎉 {player1} wins this round!")
    else:
        print(f"💥 {player2} wins this round!")

    return winner

def play_game():
    print("🎮 Welcome to Rock-Paper-Scissors (Single or Two Player Mode) 🎮")
    mode = input("Select mode - Type '1' for Single Player or '2' for Two Player: ")

    while mode not in ['1', '2']:
        mode = input("Invalid input. Please type 1 or 2: ")

    is_vs_computer = mode == '1'
    player1 = input("Enter Player 1 name: ").strip() or "Player 1"
    player2 = "Computer" if is_vs_computer else input("Enter Player 2 name: ").strip() or "Player 2"

    rounds = int(input("How many rounds would you like to play? "))
    score = {player1: 0, player2: 0}

    for i in range(1, rounds + 1):
        print(f"\n--- Round {i} ---")
        winner = play_round(player1, player2, is_vs_computer)
        if winner == "player1":
            score[player1] += 1
        elif winner == "player2":
            score[player2] += 1
        print(f"📊 Current Score -> {player1}: {score[player1]} | {player2}: {score[player2]}")

    print("\n🏁 Final Results:")
    if score[player1] > score[player2]:
        print(f"🏆 {player1} wins the game!")
    elif score[player1] < score[player2]:
        print(f"🏆 {player2} wins the game!")
    else:
        print("🤝 It's a tie game!")

    if input("\n🔄 Play again? (yes/no): ").lower().startswith("y"):
        play_game()
    else:
        print("👋 Thanks for playing!")

if __name__ == "__main__":
    play_game()
