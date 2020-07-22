from onep import oneplayer
from twop import twoplayer

while True:
    x=input("How many players, 1 or 2? ")
    if x=="1" or x=="2": break

if x=="2":
    twoplayer(input("Who's player one? "),input("Who's player two? "))
else:
    oneplayer(input("Who are you? "))