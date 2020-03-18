# HL component 9b - End Game Stats

# To Do
# Set up Game Play list with each round's results
# Set up average, best and worst scores (see 09b Stats_experiment)

import random

# Functions go here...
def int_check(question, low = None, high = None):

    # sets up error messages
    if low is not None and high is not None:
        error = "please enter an integer between {} and {} " \
                "(inclusive)".format(low,high)
    elif low is not None and high is None:
        error = "please enter an integer that is more than or " \
                "equal to {}".format(low)
    elif low is None and high is not None:
        error = "please enter an integer that is less than or " \
                "equal to {}".format(high)
    else:
        error = "please enter an integer"

    while True:

        try:
            response = int(input(question))

            # Checks response is not too low
            if low is not None and response < low:
                print(error)
                continue

            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue

# Main Routine goes here

# Get user input...
lowest = int_check("Low Nunber: ")
highest = int_check("High Number: ", lowest + 1)

GUESSES_ALLOWED = 4
rounds = int_check("How many rounds? ", 1)
game_stats = []

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWED

    secret = random.randint(lowest, highest)

    while guess != secret and guesses_left >= 1:

        guess = int_check("Guess: ", lowest, highest)
        guesses_left -= 1

        if guesses_left >= 1:

            if guess < secret:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

            elif guess > secret:
                print("Too high, try a lower number. Guesses left: {}".format(guesses_left))
        else:
            if guess < secret:
                print("Too low!")
            elif guess > secret:
                print("Too high!")

    if guess == secret:
        if guesses_left == GUESSES_ALLOWED - 1:
            print("Amazing! You got it in one guess")
        else:
            print("Well done, you got it in {} guesses".format(GUESSES_ALLOWED - guesses_left))
        num_won += 1
    else:
        print("Sorry - you lose this round as you have run out of guesses")
        guesses_left -= 1   # penalty point for losing

    game_stats.append(GUESSES_ALLOWED - guesses_left)
    print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1

# print each round's outcome...
print()
print("*** Game Scores ***")
list_count = 1
for item in game_stats:

    # indicates if game has been won or lost
    if item > GUESSES_ALLOWED:
        status = "lost, ran out of guesses"
    else:
        status = "won"

    print("Round {}: {} ({})".format(list_count, item, status))
    list_count += 1

# Calcualate (and then print) game statistics
game_stats.sort()
best = game_stats[0]    # first item in sorted list
worst = game_stats[-1]  # last item in sorted list
average = sum(game_stats)/len(game_stats)

print()
print("*** Summary Statistics ***")
print("Best: {}".format(best))
print("Worst: {}".format(worst))
print("Average: {:.2f}".format(average))