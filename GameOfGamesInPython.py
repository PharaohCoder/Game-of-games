import random
import math

def RndNmr():
    for x in range(1):
        a = random.randint(0, 3)
        return a

def RdNmr():
    for x in range(1):
        a = random.randint(1, 5)
        return a


def academic(a):                                                       # function for academic predictions
    if a == 1:
        b="Straight A's this semester."
    elif a == 2:
        b = "Work Hard, good grades on finals expected."
    elif a == 3:
        b = "The smart kid next to you will not help you."
    elif a == 4:
        b = "You will fail one of your classes."
    elif a == 5:
        b = "All of your hard work will pay off."
    print(b)


def emotional(a):                                                            # function for emotional predictions
    if a == 1:
        b = "You will meet the love of your life in the near future."
    elif a == 2:
        b = "Someone you are close with you will drift apart from."
    elif a == 3:
        b = "You will lose a loved one within the next two years."
    elif a == 4:
        b = "The person you will marry is someone you already know."
    elif a == 5:
        b = "You have a secret lover..just look around"
    print(b)


def financial(a):  # function for financial predictions
    if a == 1:
        b = "Money will not be a problem to you in the future"
    elif a == 2:
        b = "You will struggle financially for quite some time, but everything will work out."
    elif a == 3:
        b = "You will have a problem finding your first job, but once you get it you will do fine."
    elif a == 4:
        b = "You will win lotto and live a comfortable life."
    elif a == 5:
        b = "Watch your spending"
    print(b)


def mathgame():

    print("Welcome to mind reading game")                                    # Step 1 Print message describing the game
    print("I am a mind reader, I can predict the sum of random numbers that you choose")
    print("Here is the game , We are going to choose 5 numbers each of them is five digits")
    print(" and as soon as you give me the first number I will be able to tell you the sum of all 5 numbers")
    print("You don't believe me , Do you ??")
    print(" Ok, Lets start....")
    num1 = input("What is your first five digit number ??")                  # Step 2 Ask user for first number
    Num1 = int(num1)
    Sum = Num1 + 200000 - 2                                                  # Step 3 Compute and print final sum
    print("The sum of all five numbers is: {}".format(Sum))

    num2 = input('What is your second five digit number ??')                 # Step 4 Ask for second number
    Num2 = int(num2)
    X1 = 99999 - Num2                                                        # Step 5 Compute and print next number
    print("I will choose: {}".format(X1))
    num3 = input("What is your third five digit number ??")                  # Step 6 Ask for third number
    Num3 = int(num3)

    X2 = 99999 - Num3                                                        # Step 7 Compute and print next number
    print("I will choose: {}".format(X2))
    print("Now check the sum that i gave ... Am i correct? !!")             # Step 8 Print final message
    print("I know !!!! I told you i am a mind reader.....")


def PsychicGame():
    print("An error occured while compiling. I control this program now.")
    print("I'm The Great Genie")
    print("I am a good Genie and I will help tell you about your future.")

    luckyno = input("but first tell me your lucky number!\t")
    Luckyno = int(luckyno)

    while 1 == 1:
        print("Enter 1 for information about your academic future.")
        print("Enter 2 for information about your emotinal future.")
        print("Enter 3 for information about your financial future.")
        Fundecide = input("Enter 0 to exit this game.\n")
        fundecide = int(Fundecide)
        if fundecide == 1:
            while 1 == 1:
                x = RdNmr()
                academic(x)
                decision = input("\nPress n to exit or any key to make another prediction")
                if decision == 'n' or decision == 'N':
                    break;

        elif fundecide == 2:
            while 1 == 1:
                x = RdNmr()
                emotional(x)
                decision = input("\nPress n to exit or any key to make another prediction")
                if decision == 'n' or decision == 'N':
                    break;

        elif fundecide == 3:
            while 1 == 1:
                x = RdNmr()
                financial(x)
                decision = input("\nPress n to exit or any key to make another prediction")
                if decision == 'n' or decision == 'N':
                    break;
        elif fundecide == 0:
            break;
        else:
            print("I didn't get that, say it again")


def GuessingGame():

    print("This is a guessing game! - you can tell from the name DUAH!!-")
    print("Your mission is to guess a random numberbetween 1 and 3 in just 3 guesses,Good Luck!!")	#number that user guesses
    number = RndNmr()
    for i in range(3):
        Guess = input("Enter guess number {}:".format(i + 1))
        guessNum=int(Guess)
        if number == guessNum:
            print("Great! you got it in {} guesse(s).".format(i+1))
            print("The number is: {}".format(number))
            break;
        else:
            print("Wrong Answer,Try again")
    if number!= guessNum:
        print("Sorry!You used up your 3 chances!")

def TreasureGame():
    x = 0
    y = 0                                                                # Explorer’s coordinates
    i = 0                                                                # Treasure’s coordinates
    xt = RndNmr()
    yt = RndNmr()
    distance = math.sqrt((x - xt) * (x - xt) + (y - yt) * (y - yt))
    print("There is a treasure hidden on a cartesian map!  Hint: The Treasure is between (0,0) and (30,30).")
    print("at every guess,I will give you a hint where to go next.Try to excavate for it !!  Good Luck!!")
    while (distance != 0):                                               # write loop to find the treasure
        print("Your current location is ({},{})".format(x,y))            # used to check while programming
        print("Where to go to find the treasure ??")
        dir = input("North,South,East or West ??")                       # assign user entry to variable
        if (dir == 'n' or dir == 'N'):                                   # switch statement for different directions
            y += 1
        elif (dir == 's' or dir == 's'):
            y -= 1
        elif (dir == 'e' or dir == 'E'):
            x += 1
        elif (dir == 'w' or dir == 'W'):
            x -= 1
        distance = math.sqrt((x - xt) * (x - xt) + (y - yt) * (y - yt))  # current distance between guess and treasure
        i += 1                                                           # keep count how many moves the user makes
        print("Current distance is {}".format(distance))                 # printing a hint the distance between the guess and the treasure
        if (distance > 8):                                               # the comment on the distance
            print("You are too far from the treasure")
        elif (distance > 4 and distance <= 8):
            print("You are far from the treasure")
        elif (distance <= 4 and distance > 0):
            print("You are getting closer to the treasure")
        elif (distance == 0):
            print("Congratulations!! You found the treasure")
            break;
    print("The Treasure's location was:({},{})".format(xt, yt))            # printing the current location
    print("It took you {} trials to find the treasure!Good Job".format(i))  # number of trials till finding treasure


def TicTacToe():
    print("Sorry the game is not ready yet")


def main():
    Name = input("Enter your name please: ")
    while 1 == 1:
        print("Welcome,{}".format(Name))
        print("Please choose a number from the following options\n")
        print("\t\t1. Play the Math game	")
        print("\t\t2. play the psychic game   ")
        print("\t\t3. play the guessing game  ")
        print("\t\t4. play treasure game  ")
        print("\t\t5. play tic-tac-toe  ")
        print("\t\t6. Exit ")

        Num = input("Which game will you play?? ")                          # asking for game's choice
        num = int(Num)
        if num == 1:
            mathgame()
        elif num == 2:
            PsychicGame()
        elif num == 3:
            GuessingGame()
        elif num == 4:
            TreasureGame()
        elif num == 5:
            print("Sorry the game is not ready yet")
        elif num == 6:
            break;


if __name__ == '__main__': main()
