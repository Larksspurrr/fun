spaces = ["*" for i in range(10)]
turn = 1 # 1 for player 1, 2 for player 2
turns = 0
symbol = "X"

print("Tic-Tac-Toe")

name_1 = input("Player 1's Name: ")
print(f"{name_1} will be X")
name_2 = input("Player 2 Name: ")
print(f"{name_2} will be O")
print("The squares are numbered 1-9 from left to right, starting from the top left. Just type in the desired square.")

def win(turn, name_1, name_2, turns):
    board = f"""     |     |     
  {spaces[0]}  |  {spaces[1]}  |  {spaces[2]}  
     |     |     
-----------------
     |     |     
  {spaces[3]}  |  {spaces[4]}  |  {spaces[5]}  
     |     |     
-----------------
     |     |     
  {spaces[6]}  |  {spaces[7]}  |  {spaces[8]}  
     |     |     """
    if turn == 1:
        print(f"{name_1} wins!")
    elif turn == 2:
        print(f"{name_2} wins!")
    print(board)
    print(f"Turns: {turns}")


while True:
    turns += 1
    board = f"""     |     |     
  {spaces[0]}  |  {spaces[1]}  |  {spaces[2]}  
     |     |     
-----------------
     |     |     
  {spaces[3]}  |  {spaces[4]}  |  {spaces[5]}  
     |     |     
-----------------
     |     |     
  {spaces[6]}  |  {spaces[7]}  |  {spaces[8]}  
     |     |     """
    print(board)
    print("Reminder: Stars mean empty squares.\n")
    if turn == 1:
        print(f"It is {name_1}'s turn.")
        symbol = "X"
    elif turn == 2:
        print(f"It is {name_2}'s turn.")
        symbol = "O"
    
    choice = int(input("Choose a square: "))
    if spaces[choice - 1] in ["X", "O"]: # spaces[choice - 1] so choice aligns with index
        print("That space is already chosen!")
    else:
        spaces[choice - 1] = symbol
        if (spaces[0] == spaces[3] == spaces[6] != "*") or (spaces[1] == spaces[4] == spaces[7] != "*") or (spaces[2] == spaces[5] == spaces[8] != "*"): # Columns
            win(turn, name_1, name_2, turns)
            break
        elif (spaces[0] == spaces[1] == spaces[2] != "*") or (spaces[3] == spaces[4] == spaces[5] != "*") or (spaces[6] == spaces[7] == spaces[8] != "*"): # Rows
            win(turn, name_1, name_2, turns)
            break
        elif (spaces[0] == spaces[4] == spaces[8] != "*") or (spaces[2] == spaces[4] == spaces[6] != "*"): # Diagonal
            win(turn, name_1, name_2, turns)
            break
        if turn == 1:
            turn = 2
        elif turn == 2:
            turn = 1