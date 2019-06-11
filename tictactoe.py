#This program runs on pyflakes, but should work in most other places.
while True: #This repeats every time someone wants a new game.
    x_o=1 if input("X first or O first (answer x or o) Ans: ").lower()=="x" else 2 #x will go first if x_o is odd.
    table="|---|---|---|\n| 1 | 2 | 3 |\n|---|---|---|\n| 4 | 5 | 6 |\n|---|---|---|\n| 7 | 8 | 9 |\n|---|---|---|"; print (table + "\nEnter the coordinate to place a marker.")
    while True: #what happens every turn
        turn="X" if x_o%2==1 else "O"
        while True:
            ans= input(turn + "? ")
            if ans not in table or len(ans)!=1 or str(ans) not in "123456789": print ("Sorry, error! Try again: ")
            else: break
        table=table.replace(ans,turn); print("\033c" + table)
        if table[:25].count(turn)==3 or table[26:53].count(turn)==3 or table[70:].count(turn) ==3 or table[16]==turn and table[44]==turn and table[72]==turn or table[20]==turn and table[48]==turn and table[76] ==turn or table[24]==turn and table[52]==turn and table[80] ==turn or table[16]==turn and table[48]==turn and table[80]==turn or table[24]==turn and table[48]==turn and table[72]==turn: print(turn + " wins!!"); break
        if table.count("X")==5: print ("Tie!!"); break
        x_o+=1
    while True:
        playAgain=input("Play again (answer yes or no) Ans: ")
        if playAgain.lower()== "no": break
        if playAgain.lower()=="yes": print("\033c"); break
        else: print ("Try again?")
    if playAgain.lower()=="no": break; print ("Thanks for playing!!")