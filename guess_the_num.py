import random

# Example of a game that is best suited for victory using a binary search algorithm... Also just bored...
# Generate a random number for user to guess

random_num = 0

for i in range(1, 101):
    random_num = random.randint(1, 101)

game_round = 0

# Game loop

while True:
    choice = input("Guess a number between 1 and 100 press q to quit >> ").strip()
    if not choice:
        choice = 1

    if choice is "q":
        print("Thanks for playing")
        break

    choice = int(choice)

    if choice is random_num:
        game_round += 1
        print("You win. It took you " + str(game_round) + " number of guesses to get it right")
        break

    if choice < random_num:
        game_round += 1
        print("Guess Higher")

    elif choice > random_num:
        game_round += 1
        print("Guess Lower")
