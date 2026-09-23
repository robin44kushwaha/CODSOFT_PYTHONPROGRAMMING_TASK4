import random

# initialize scores and round count
user_score = 0
computer_score = 0
count = 0

# Game loop for 5 rounds
while count < 5:

    user = int(input('''
Enter 0 for choosing Rock
Enter 1 for choosing Paper
Enter 2 for choosing Scissors
'''))

    print('You chose: {}'.format(
        'Rock' if user == 0 else
        'Paper' if user == 1 else
        'Scissors' if user == 2 else
        'Invalid choice'
    ))

    computer = random.randint(0, 2)

    print('Computer chose: {}'.format(
        'Rock' if computer == 0 else
        'Paper' if computer == 1 else
        'Scissors'
    ))

# condition for having a tie
    if user == computer:
        print("It's a tie!")

# condition for user winning
    elif (user == 0 and computer == 2) or \
         (user == 1 and computer == 0) or \
         (user == 2 and computer == 1):

        print("You win!")
        user_score += 1

# condition for computer winnig
    else:
        print("Computer wins!")
        computer_score += 1

    count += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")
    print(f"Round {count}/5 completed\n")


# Game over, display final scores and winner
print("========== GAME OVER ==========")
print(f"Final Score → You: {user_score} | Computer: {computer_score}")

if user_score > computer_score:
    print("You won the game!")

elif computer_score > user_score:
    print("Computer won the game!")

else:
    print("The game is tied!")
