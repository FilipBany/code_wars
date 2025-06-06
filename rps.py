def rps(p1, p2):
    if((p1=="scissors" and p2=="paper") or (p1=="paper" and p2=="rock") or (p1=="rock" and p2=="scissors")):
        return("Player 1 won!")
    if((p1=="rock" and p2=="paper") or (p1=="scissors" and p2=="rock") or (p1=="paper" and p2=="scissors")):
        return("Player 2 won!")
        
    if((p1=="paper" and p2=="paper") or (p1=="rock" and p2=="rock") or (p1=="scissors" and p2=="scissors")):
        return("Draw!")

        
print(rps('scissors', 'paper'))
print(rps('paper', 'rock'))
print(rps('rock', 'scissors'))
print(rps('rock', 'paper'))
print(rps('scissors', 'rock'))
print(rps('paper', 'scissors'))
print(rps('rock', 'rock'))
print(rps('scissors', 'scissors'))
print(rps('paper', 'paper'))
