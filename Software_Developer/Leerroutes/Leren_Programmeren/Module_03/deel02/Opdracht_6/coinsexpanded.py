# name of student: Joshua Slui
# number of student: 90069867
# purpose of program:
# function of program:
# structure of program:

toPay = int(float(input('Amount to pay: ')) * 100)  # Ask what the costs are
paid = int(float(input('Paid amount: ')) * 100)  # Ask what was paid
change = paid - toPay  # Subtract toPay from paid to check what has to be returned
returnedCoins = []
returnedValue = []

if change > 0:  # condition to check if there is change to be returned (more than 0)
    coinValue = 500  # Sets the value of variable coinValue to 50

    while change > 0 and coinValue > 0:  # loops if change is more than 0 and coinvalue is also more than 0
        nrCoins = change // coinValue  # Divides change with coinvalue and rounds it down to the nearest full number
        print(nrCoins)

        if nrCoins > 0:  #
            print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!')  # Prints how many coins you need to return
            nrCoinsReturned = int(input('How many coins of ' + str(coinValue) + ' cents did you return? '))  # Asks how many coins you returned
            returnedCoins.append(str(nrCoinsReturned))
            returnedValue.append(str(coinValue))
            change -= nrCoinsReturned * coinValue  # Removes nrCoins

        # comment on code below:
        # This code checks how much coinValue is left and then changes it
        if coinValue == 500:
            coinvalue = 300
        elif coinValue == 300:
            coinValue = 200
        elif coinValue == 200:
            coinValue = 50
        elif coinValue == 50:
            coinValue = 20
        elif coinValue == 20:
            coinValue = 10
        elif coinValue == 10:
            coinValue = 5
        elif coinValue == 5:
            coinValue = 2
        elif coinValue == 2:
            coinValue = 1
        else:
            coinValue = 0

    listiteration = 0
    loop = True
    print("You have returned:")
    while loop == True:
        try:
            print(f"{returnedCoins[listiteration]} coins of {returnedValue[listiteration]} cents")
            listiteration += 1
        except IndexError:
            loop = False

if change > 0:  # Checks if change is still more than 0
    print('Change not returned: ', str(change) + ' cents')
else:
    print('done')