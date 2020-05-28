import random

def eval_spaces():
    spaces=[]
    for x in table:
        if x in "XO123456789":
            spaces.append(x)
    return spaces

def iswinner(turn):
    if \
            table[:25].count(turn) == 3\
            or table[26:53].count(turn) == 3\
            or table[70:].count(turn) == 3\
            or table[16] == turn and table[44] == turn and table[72] == turn\
            or table[20] == turn and table[48] == turn and table[76] == turn\
            or table[24] == turn and table[52] == turn and table[80] == turn\
            or table[16] == turn and table[48] == turn and table[80] == turn\
            or table[24] == turn and table[48] == turn and table[72] == turn:
        return True
        #each index represents some point on the table.
        #although admittedly not the most comprehensible way, or the most flexible, it works
        #maybe will improve it soon?
    else:
        return False

#2p
while True:
    x=input("How many players, 1 or 2?")
    if x=="1" or "2":
        break
if x=="2":
    while True: #This repeats every time someone wants a new game.
        x_o=1 if input("X first or O first (answer x or o) Ans: ").lower()=="x" else 2 #x will go first if x_o is odd.
        table="|---|---|---|\n| 1 | 2 | 3 |\n|---|---|---|\n| 4 | 5 | 6 |\n|---|---|---|\n| 7 | 8 | 9 |\n|---|---|---|"; print (table + "\nEnter the coordinate to place a marker.")
        while True: #what happens every turn
            turn="X" if x_o%2==1 else "O"
            while True:
                ans= input(turn + "? ")
                if ans not in table or len(ans)!=1 or str(ans) not in "123456789": print ("Sorry, error! Try again: ")
                else: break
            table=table.replace(ans,turn); print("\n" + table)
            if iswinner(turn): print(turn + " wins!!"); break
            if table.count("X")==5: print ("Tie!!"); break
            x_o+=1
        while True:
            playAgain=input("Play again (answer yes or no) Ans: ")
            if playAgain.lower()== "no": break
            if playAgain.lower()=="yes": print("\n"); break
            else: print ("Try again?")
        if playAgain.lower()=="no":
            print ("Thanks for playing!!")
            break

#1p
#Having two different lines of code for different scenarios may not be byte-efficient,
#but makes the code far less confusing.
else:
    while True: #This repeats every time someone wants a new game.
        table="|---|---|---|\n| 1 | 2 | 3 |\n|---|---|---|\n| 4 | 5 | 6 |\n|---|---|---|\n| 7 | 8 | 9 |\n|---|---|---|"; print (table + "\nEnter the coordinate to place a marker.")
        if input("Do you want to be X or O?").lower()=="o":
            x_o=2
            player="O"
            computer="X"
        else:
            x_o=1
            player="X"
            computer="O"
        while True: #what happens every turn
            turn="X" if x_o%2==1 else "O"
            space=eval_spaces()
            table1=table
            if turn==player: #if turn == player
                while True:
                    ans= input(turn + "? ")
                    if ans not in table or len(ans)!=1 or str(ans) not in "123456789": print ("Sorry, error! Try again: ")
                    else: break
            else:
                corners=(list('1369'))
                edges=(list('2468'))
                random.shuffle(corners)
                random.shuffle(edges)

                points=corners+["5"]+edges

                for x in points: #Chooses a random corner, then center, then random edge
                    if x in space:
                        ans=str(x)
                        break
                for x in space: #Block user's win
                    if x not in "XO": #cur place is a number
                        table = table.replace(x, player) #sets up to see if it is a win
                        if iswinner(player):
                            ans=x
                            break
                    table=table1

                for x in space:  # One-move win
                    if x not in "XO":  # cur place is a number
                        table = table.replace(x, computer)  # sets up to see if it is a win
                        if iswinner(computer):
                            ans = x
                            break
                    table=table1

            #The reason that the order of for loops goes from worst to best-case-scenario is because this way
            #ans has a priority of best case first (because after "one move win" the computer letter doesn't change.)
            table=table.replace(ans,turn)
            #"Why is ans highlighted?"
            #If all the letters were to be taken already, then there would be an error.
            #However, lines 114-116 cover that.
            print("\n" + table)
            if iswinner(turn):
                print(turn, "wins!")
                break
            if table.count(player)==5:
                print ("Tie!!")
                break
            x_o+=1
        while True:
            playAgain=input("Play again (answer yes or no): ").lower()
            if playAgain == "no" or "yes":
                break
            else:
                print ("Try again?")
        if playAgain=="no":
            print ("Thanks for playing!!")
            break

#1p
#Having two different lines of code for different scenarios may not be byte-efficient,
#but makes the code far less confusing.
else:
    while True: #This repeats every time someone wants a new game.
        table="|---|---|---|\n| 1 | 2 | 3 |\n|---|---|---|\n| 4 | 5 | 6 |\n|---|---|---|\n| 7 | 8 | 9 |\n|---|---|---|"; print (table + "\nEnter the coordinate to place a marker.")
        if input("Do you want to be X or O?").lower()=="o":
            x_o=2
            player="O"
            computer="X"
        else:
            x_o=1
            player="X"
            computer="O"
        while True: #what happens every turn
            turn="X" if x_o%2==1 else "O"
            space=eval_spaces()
            table1=table
            if turn==player: #if turn == player
                while True:
                    ans= input(turn + "? ")
                    if ans not in table or len(ans)!=1 or str(ans) not in "123456789": print ("Sorry, error! Try again: ")
                    else: break
            else:
                corners=(list('1369'))
                edges=(list('2468'))
                random.shuffle(corners)
                random.shuffle(edges)

                points=corners+["5"]+edges

                for x in points: #Chooses a random corner, then center, then random edge
                    if x in space:
                        ans=str(x)
                        break
                for x in space: #Block user's win
                    if x not in "XO": #cur place is a number
                        table = table.replace(x, player) #sets up to see if it is a win
                        if iswinner(player):
                            ans=x
                            break
                    table=table1

                for x in space:  # One-move win
                    if x not in "XO":  # cur place is a number
                        table = table.replace(x, computer)  # sets up to see if it is a win
                        if iswinner(computer):
                            ans = x
                            break
                    table=table1

            #The reason that the order of for loops goes from worst to best-case-scenario is because this way
            #ans has a priority of best case first (because after "one move win" the computer letter doesn't change.)
            table=table.replace(ans,turn)
            #"Why is ans highlighted?"
            #If all the letters were to be taken already, then there would be an error.
            #However, lines 114-116 cover that.
            print("\n" + table)
            if iswinner(turn):
                print(turn, "wins!")
                break
            if table.count(player)==5:
                print ("Tie!!")
                break
            x_o+=1
        while True:
            playAgain=input("Play again (answer yes or no): ").lower()
            if playAgain == "no" or "yes":
                break
            else:
                print ("Try again?")
        if playAgain=="no":
            print ("Thanks for playing!!")
            break