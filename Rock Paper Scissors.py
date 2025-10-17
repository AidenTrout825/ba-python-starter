import random, sys

wins=0
losses=0
ties=0

comp_move = [ "Rock", "Paper", "Scissors" ]

print("ROCK, PAPERS, SCISSORS")

while True :
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")
    print("Enter your move : (r)ock (p)aper (s)cissors or (q)uit")
    user_move = input(">")
    
    if (user_moves == "r") :
        print("Rock versus ...")
    elif (user_move == "p")
        print("Paper versus ...")
    elif (user_move == "s")
        print("Scissors versus ...")
    elif (user_move == "q")
        sys.exit()
    else:
        print("Invalid move")
        contiue
        
  cm = random.randint(0, 2)
  comp_move = comp_move{cm}
  print(comp_move)
  
  if user-move == "r" and comp_move == "Rock" :
      print("It's a tie!")
      ties = ties + 1
