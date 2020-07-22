
import random


def eval_spaces(table):
    spaces=''
    for x in table:
        if x in "XO123456789": spaces+=x
    return spaces

def iswinner(table,coordinates,turn):
    def ch(t1,t2,t3):
        return table[coordinates[t1]]==turn and table[coordinates[t2]]==turn and table[coordinates[t3]]==turn

    return \
ch(1,2,3) \
or ch(4,5,6) \
or ch(7,8,9) \
or ch(1,4,7) \
or ch(2,5,8) \
or ch(3,6,9) \
or ch(1,5,9) \
or ch(3,5,7)

def oneplayer(p1,score=[0,0]):
    '''

    :param p1: the name of player 1
    :param score: list, 2-long, element 0 is the first player's score, element 1 is the second.
    :return:
    '''
    while True:  # This repeats every time someone wants a new game.
        table = "|---|---|---|\n| 1 | 2 | 3 |\n|---|---|---|\n| 4 | 5 | 6 |\n|---|---|---|\n| 7 | 8 | 9 |\n|---|---|---|";
        print(table + "\nEnter the coordinate to place a marker.")
        coordinates = [''] + [table.find(str(x)) for x in range(1, 10)]
        if input("Do you want to be X or O?").lower() == "o":
            x_o = 2
            player = "O"
            computer = "X"
        else:
            x_o = 1
            player = "X"
            computer = "O"
        while True:  # what happens every turn
            turn = "X" if x_o % 2 == 1 else "O"
            space = eval_spaces(table)
            table1 = table
            if turn == player:  # if turn == player
                while True:
                    ans = input(p1 + ", input your move {}: ".format(turn))
                    if ans not in table or len(ans) != 1 or str(ans) not in "123456789":
                        print("Sorry, error! Try again: ")
                    else:
                        break
            else:
                corners = (list('1379'))
                edges = (list('2468'))
                random.shuffle(corners)
                random.shuffle(edges)

                points = corners + ["5"] + edges

                for x in points:  # Chooses a random corner, then center, then random edge
                    if x in space:
                        ans = str(x)
                        break
                for x in space:  # Block user's win
                    if x not in "XO":  # cur place is a number
                        table = table.replace(x, player)  # sets up to see if it is a win
                        if iswinner(table,coordinates,player):
                            ans = x
                            break
                    table = table1

                for x in space:  # One-move win
                    if x not in "XO":  # cur place is a number
                        table = table.replace(x, computer)  # sets up to see if it is a win
                        if iswinner(table,coordinates,computer):
                            ans = x
                            break
                    table = table1

            # The reason that the order of for loops goes from worst to best-case-scenario is because this way
            # ans has a priority of best case first (because after "one move win" the computer letter doesn't change.)
            table = table.replace(ans, turn)
            # "Why is ans highlighted?"
            # If all the letters were to be taken already, then there would be an error.
            # However, the line that includes "if table.count(player)==5" covers that.
            print("\n" + table)
            if iswinner(table,coordinates,turn):
                print(turn, "wins!")
                break
            if table.count(player) == 5:
                print("Tie!!")
                break
            x_o += 1
        while True:
            playAgain = input("Play again (answer yes or no): ")[0]
            if playAgain in 'nNyY':
                break
            else:
                print("Try again?")
        if playAgain in 'nN':
            print("Thanks for playing!!")
            break