# HL - Get (and Check) user input

# To Do
# Check a lowst is an integer (any integer)
# Check that highest is more than lowest (lower bound only)
# Check that rounds is more than 1 (upper bound only)
# Check that guess is between lowest and highest (lower and upper bound)


#Number checking function goes here
def intcheck(question, low = None, high = None):

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
# Main routine

lowest = intcheck("Low Nunber: ")
highest = intcheck("High Number: ", lowest + 1)
rounds = intcheck("Round: ", 1)
guess = intcheck("Guess: ", lowest, highest)