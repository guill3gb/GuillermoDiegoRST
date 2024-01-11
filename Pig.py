import random

def roll_die():
    return random.randint(1, 6)

def player_turn(player_name, total_score):
    print(f"{player_name}'s turn:")
    turn_score = 0

    while True:
        roll = roll_die()
        print(f"Rolled a {roll}")

        if roll == 1:
            print("Pig! You lose your turn and score for this round.")
            return 0

        turn_score += roll
        print(f"Current round score: {turn_score}")

        choice = input("Do you want to roll again? (y/n): ").lower()
        if choice != 'y':
            break

    total_score += turn_score
    print(f"{player_name}'s total score: {total_score}")
    return total_score

def computer_turn():
    print("Computer's turn:")
    turn_score = 0

    while turn_score <= 15:
        roll = roll_die()
        print(f"Computer rolled a {roll}")

        if roll == 1:
            print("Pig! Computer loses its turn and score for this round.")
            return 0

        turn_score += roll
        print(f"Current round score: {turn_score}")

    print("Computer banks its points.")
    return turn_score

def pig_game():
    player_name = input("Enter your name: ")
    computer_score = 0
    player_score = 0

    while player_score < 100 and computer_score < 100:
        player_score = player_turn(player_name, player_score)
        if player_score >= 100:
            print(f"{player_name} wins!")
            break

        computer_score += computer_turn()
        print(f"Computer's total score: {computer_score}")
        if computer_score >= 100:
            print("Computer wins!")

if __name__ == "__main__":
    pig_game()