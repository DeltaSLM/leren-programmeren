import random

anotherRound = ""
score = 0
rounds = 1

def guesser(question):
    #print("number ", number)  # uncomment this for debugging
    global guess
    while not (guess := input(question)).isdigit():
        if guess == "stop":
            print("Exiting game with a score of {}, we're sad to see you go.".format(score))
            exit()
        print("--- You need to provide us with a number between 1 and 1000 or \"stop\" to stop ---")
    #print(guess)

    if guess == str(number):
        return True

    else:
        return False

for x in range(20):
    if x != 0:
        while not (anotherRound == "y" or anotherRound == "n"):
            anotherRound = input("Do you want to play another round? Y/N").lower()

        if anotherRound == "n":
            print("Got it, aborting game.")
            break
        elif anotherRound == "y":
            print("You are currently on round {} with score {}.".format(rounds, score))
            pass
    number = random.randint(1, 1000)  # The number that has to be guessed

    if guesser("Guess a number between 1 to 1000") == True:
        score += 1
        rounds += 1
        if x != 20:
            print("You guessed correctly! Moving onto round {} with score {}".format(rounds, score))

    else:
        guesses = 10
        for x in range(10):
            if x == 10:
                print("You have failed to guess correctly, moving onto round {} with score {}".format(rounds, score))
                break
            #if number - guess > 50:
                #print("Guess higher")

            if guesser("Please guess again. You have {} guesses left.".format(guesses)) == True:
                score += 1
                rounds += 1
                print("You guessed correctly! Moving onto round {} with score {}".format(rounds, score))
                break

            else:
                sum = number - int(guess)

                if sum > 50:
                    print("Guess higher")
                elif sum < -50:
                    print("Guess lower")
                elif sum > 20 and sum < 50 or sum < -20 and sum > -50:
                    print("Getting warm...")
                elif sum < 20 or sum > -20:
                    print("Getting very warm...")

                guesses -= 1
        rounds += 1

print("Congratulations! You have finished the game with a score of {}".format(score))