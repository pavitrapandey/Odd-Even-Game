import random as r

#This function is for choices input by the user in the following game...
def get_player_choice(prompt, choices):
    while True:
        choice = input(prompt).strip().lower()
        if choice in choices:
            return choice
        print(f"Invalid choice... \nPlease choose from {choices}.")

#Here we write the input for Toss...
def get_player_number():
    while True:
        try:
            number = int(input("Enter your number (1-6): "))
            if 1 <= number <= 6:
                return number
            print("🚨🚨Invalid number...🚨🚨 \nPlease choose a number between 1 and 6.")
        except ValueError:
            print("🚨🚨Invalid input...🚨🚨 \nPlease enter an number between 1 and 6.")

#Now this the 1st Part of our game
#Toss Time
def odd_even_game():
    print("Welcome to the game!!!")
    print("🎉🎉🎉🎉🎉🎉🎉🎉")
    print("🎇🎇TOSS TIME!!🎇🎇")

    player_choice = get_player_choice("Choose 'odd' or 'even': ", ['odd', 'even'])
    player_number = get_player_number()

    computer_number = r.randint(1, 6)

    print(f"You chose {player_number}.")
    print(f"The computer chose {computer_number}.")

    total = player_number + computer_number
    result = 'odd' if total % 2 != 0 else 'even'

    print(f"The total is {total}, which is {result}.")

    if result == player_choice:
        print("Congratulations, You win the toss!")
        print("🥳🥳🥳🥳🥳🥳🥳")
        return True  # Player wins the toss
    else:
        print("You lose 🙃")
        print("Computer wins the toss.")
        return False  # Computer wins the toss

#This a Second Part of Our Game
#Cricketing part...
#This function returns the choice
def play_cricket_game():
    if odd_even_game():
        choice = get_player_choice("Choose 'bat🏏' or 'bowl⚾': ", ['bat', 'bowl'])
        if choice == 'bat':
            player_bats_first()
        else:
            computer_bats_first()
    else:
        choice = r.choice(['bat', 'bowl'])
        print(f"Computer chooses to {choice} first.")
        if choice == 'bat':
            computer_bats_first()
        else:
            player_bats_first()

#If Player bats first
def player_bats_first():
    player_score = 0
    print("You are batting first!🏏\n")

    while True:
        player_input = get_player_number()
        computer_input = r.randint(1, 6)
        print(f"Computer bowls: {computer_input}")

        if player_input == computer_input:
            print("You are out!😐")
            break
        else:
            player_score += player_input
            print(f"Your score: {player_score}")

    print(f"End of your innings..\n Your total score: {player_score}")

    computer_score = 0
    print("Computer is batting now!🏏\n")

    while computer_score <= player_score:
        player_input = get_player_number()
        computer_input = r.randint(1, 6)
        print(f"Computer bats: {computer_input}")

        if player_input == computer_input:
            print("Computer is out!😀😀")
            break
        else:
            computer_score += computer_input
            print(f"Computer score: {computer_score}")

    if computer_score > player_score:
        print("Sorry!! 😔😔\nYou Lose!!")
        print("😓😓😓")
    else:
        print("CONGRATULATION!!!!🎊\nYou win!")
        print("🎉🎉✨✨🎇🎇🎆🎆")

#if Computer bats First
def computer_bats_first():
    computer_score = 0
    print("Computer is batting first!🏏🏏")
    print("\nYou are bowling⚾⚾")

    while True:
        player_input = get_player_number()
        computer_input = r.randint(1, 6)
        print(f"Computer bats: {computer_input}")

        if player_input == computer_input:
            print("Computer is out!😀😀")
            break
        else:
            computer_score += computer_input
            print(f"Computer score: {computer_score}")

    print(f"End of computer's innings. Computer's total score: {computer_score}")

    player_score = 0
    print("You are batting now!🏏🏏")

    while player_score <= computer_score:
        player_input = get_player_number()
        computer_input = r.randint(1, 6)
        print(f"Computer bowls: {computer_input}")

        if player_input == computer_input:
            print("You are out!😐")
            break
        else:
            player_score += player_input
            print(f"Your score: {player_score}")

    print(f"End of your innings...\nYour total score: {player_score}")

    if player_score > computer_score:
        print("CONGRATULATION!!!!🎊\nYou win!")
        print("🎉🎉✨✨🎇🎇🎆🎆")

    else:
       print("Sorry!! 😔😔\nYou Lose!!")
       print("😓😓😓")

if __name__ == "__main__":
    play_cricket_game()
