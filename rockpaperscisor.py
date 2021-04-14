import random 
def function():
    player1 = 0
    ai_player = 0
    n = int(input('''Welcome to Rock-Paper-Scrissors game.
How many rounds do you want to play?(please note that you have to pick an odd number):
    '''))
    rounds = n
    animate()
    while (n):
        v = int(input("Choose !\n1-Rock\n2-paper\n3-scissors\n"))
        ai = random.randint(1, 3)
        print("Ur choice :" ,show(v))
        print("ai's choice :", show(ai))
        if ai == v:
            pass
            # player1 += 1
            # ai_player += 1
        elif v == 1: #player1 is Rock 
            if ai == 2:
                player1 += 1
            elif ai == 3:
                ai_player += 1
        elif v == 2: #player1 is paper 
            if ai == 1:
                player1 += 1
            elif ai == 3:
                ai_player += 1
        elif v == 3: #player1 is scissors 
            if ai == 2:
                player1 += 1
            elif ai == 1:
                ai_player += 1
        n -= 1
        print("ur score:", player1)
        print("ai's score:", ai_player)
    if player1 > ai_player:
        print("U WON!!! u got "+str(player1)+ " out of "+ str(rounds))
    else:
        print("U Lost :((u got "+ str(player1)+ " out of "+ str(rounds))
        print("player 2 got " + str(player1) + " out of " + str(rounds))
    #this parts is not mine but the others are mine :/
    # its for beauty reasons , makes the game more acceptable 
import time
import sys

#here is the animation
def animate():
    done = False
    while done == False:
        sys.stdout.write('\rMatch begins in 3 ...')
        time.sleep(1)
        sys.stdout.write('\rMatch begins in 2 ...')
        time.sleep(1)
        sys.stdout.write('\rMatch begins in 1 ...')
        time.sleep(1)
        sys.stdout.write('\rMatch begins now ')
        time.sleep(1)
        done = True

def show(number):
    if number == 1:
        return "Rock"
    elif number == 2:
        return "Paper"
    else:
        return "Scissors"
function()