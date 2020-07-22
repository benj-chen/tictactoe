from onep import eval_spaces,iswinner
def twoplayer(p1,p2,score=[0,0]):
    while True:  # This repeats every time someone wants a new game.
        x_o = 1 if input("X first or O first (answer x or o) Ans: ").lower() == "x" else 2  # x will go first if x_o is odd.
        table = "|---|---|---|\n| 1 | 2 | 3 |\n|---|---|---|\n| 4 | 5 | 6 |\n|---|---|---|\n| 7 | 8 | 9 |\n|---|---|---|"
        print(table + "\nEnter the coordinate to place a marker.")
        coordinates = [''] + [table.find(str(x)) for x in range(1, 10)]
        while True:  # what happens every turn
            space = eval_spaces(table)
            turn = "X" if x_o % 2 == 1 else "O"
            while True:
                ans = input(turn + "? ")
                if ans not in table or len(ans) != 1 or str(ans) not in "123456789":
                    print("Sorry, error! Try again: ")
                else:
                    break
            table = table.replace(ans, turn)
            print("\n" + table)
            if iswinner(table,coordinates,turn): print(turn + " wins!!"); break
            if table.count("X") == 5: print("Tie!!"); break
            x_o += 1
        while True:
            playAgain = input("Play again (answer yes or no) Ans: ")
            if playAgain.lower() == "no": break
            if playAgain.lower() == "yes":
                print("\n"); break
            else:
                print("Try again?")
        if playAgain.lower() == "no":
            print("Thanks for playing!!")
            break