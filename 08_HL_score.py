# HL component 8 - set up score mechanics

# To Do
# Set up round and win counter
# update feedback statements


SECRET = 7
GUESSES_ALLOWEd = 4
rounds = 3

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = GUESSES_ALLOWEd

    while guess != SECRET and guesses_left >= 1:

        guess = int(input("Guess: "))
        guesses_left -= 1

        if guesses_left >= 1:

            if guess < SECRET:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

            elif guess > SECRET:
                print("Too high, try a lower number. Guesses left: {}".format(guesses_left))
        else:
            if guess < SECRET:
                print("Too low!")
            elif guess > SECRET:
                print("Too high!")

    if guess == SECRET:
        if guesses_left == GUESSES_ALLOWEd - 1:
            print("Amazing! You got it in one guess")
        else:
            print("Well done, you got it in {} guesses".format(GUESSES_ALLOWEd - guesses_left))
        num_won += 1
    else:
        print("Sorry - you lose this round as you have run out of guesses")

    print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1
