import random

# Variables for the 20 rounds
rounds = 0
score = 0
userAnswer = ""
newRound = ""

# Variables for the 10 guess rounds
guesses = 10
userGuess = ""

while rounds != 20:
    numbergen = random.randint(1, 1000)  # Number generation
    # print(numbergen)  # DEBUGGING
    while not ((userAnswer := input(f"Please provide us with a number between 1 to 1000 or 'stop' to stop..\n-- You are currently on round {rounds} with score {score} --\nAnswer here: ")).isdigit() and 1 <= int(userAnswer) <= 1000):
        if userAnswer.lower() == "stop":
            exit(f"We are sad to see you go, you ended with {score} points in {rounds} rounds")
        print("------------------------------------------------------------------")

    if int(userAnswer) == numbergen:
        rounds += 1
        score += 1

    else:
        while guesses != 0:
            # print(numbergen)  # DEBUGGING
            while not ((userGuess := input("WRONG: Try again or 'stop' to stop, you have {} guesses left.".format(guesses))).isdigit() and 1 <= int(userGuess) <= 1000):
                if userGuess.lower() == "stop":
                    exit(f"We are sad to see you go, you ended with {score} points in {rounds} rounds")
                print("!!! Please provide us with a number between 1 to 1000 !!!")

            userGuess = int(userGuess)

            if userGuess == numbergen:
                guesses = 0
                rounds += 1
                score += 1

            else:
                guesses -= 1

                if numbergen > userGuess and numbergen - userGuess > 50:
                    print("Guess higher.")
                elif userGuess > numbergen and userGuess - numbergen > 50:
                    print("Guess lower.")
                elif numbergen > userGuess and 50 > numbergen - userGuess > 20:
                    print("Getting warm, guess higher..")
                elif userGuess > numbergen and 50 > userGuess - numbergen > 20:
                    print("Getting warm, guess lower..")
                elif numbergen > userGuess and numbergen - userGuess < 20:
                    print("Getting very warm, guess higher.")
                elif userGuess > numbergen and userGuess - numbergen < 20:
                    print("Getting very warm, guess lower.")

    newRound = input("Want to play another round? Y/YES/N/NO | The game will automatically continue if other arguments are given.").lower()
    if newRound == "n" or newRound == "no":
        break

print(f"{'We are sad to see you go.' if newRound == 'n' or newRound == 'no' else 'Congratulations on beating the game!'} You ended on {score} points in {rounds} rounds!")
