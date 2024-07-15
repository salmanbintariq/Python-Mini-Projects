import random

print('\n---ROCK, PAPER, SCISSOR GAME---\n')
print("GAME RULES:\n1)Rock wins against scissors;\n2)Paper wins against rock;\n3)Scissors wins against paper.")

moves = ['Rock', 'Paper', 'Scissor']

#Take input from User
user_move = input("Enter your move (Rock, Paper, or Scissor): ").capitalize()
print(f"User Move is : {user_move}")

#Computer will chose randomly
computer_move = random.choice(moves)
print(f"Computer Move is: {computer_move}")

#Conditions
if user_move == computer_move:
    print("It's a Tie.")

elif (user_move == "Rock" and computer_move == "Scissor") or (user_move == "Paper" and computer_move == "Rock") \
   or (user_move == "Scissor" and computer_move == "Paper"):
    print("User Wins!")
else:
    print("Computer Wins!")    
