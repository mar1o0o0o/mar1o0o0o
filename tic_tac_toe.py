# Tic Tac Toe in Python!
# This program is pretty simple but it does the job hehe
# When I become better at Python I will try to create a game mode where you can play against the CPU, but I reckon it won't come soon

boxes = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def input_func(inputvar):
    global boxes
    output = None
    while not(output in ("1", "2", "3")):
        output = input(f"Choose {inputvar} between 1 and 3: ")
    return int(output)

def board(boxes):
    print(f"1  {boxes[0][0]} | {boxes[0][1]} | {boxes[0][2]}")
    print("     |   |  ")
    print("   ---------")
    print("     |   |  ")
    print(f"2  {boxes[1][0]} | {boxes[1][1]} | {boxes[1][2]}")
    print("     |   |  ")
    print("   ---------")
    print("     |   |  ")
    print(f"3  {boxes[2][0]} | {boxes[2][1]} | {boxes[2][2]}")
    print("")
    print("   1   2   3")

def place(boxes, current_player):
    row, column = input_func("row")-1, input_func("column")-1
    while boxes[row][column]!=" ":
        print("That box is already occupied! Choose another one.")
        row, column = input_func("row")-1, input_func("column")-1
    boxes[row][column]=current_player
    return boxes

def game(boxes):
    for i in range(9):
        if i%2==0:
            current_player="X"
        else:
            current_player="O"
        print("")
        board(boxes)
        print()
        print(f"Player {current_player}, your turn!")
        place(boxes, current_player)
        if boxes[0].count(current_player)==3 or boxes[1].count(current_player)==3 or boxes[2].count(current_player)==3 or (boxes[0][0]==current_player and boxes[1][0]==current_player and boxes[2][0]==current_player) or (boxes[0][1]==current_player and boxes[1][1]==current_player and boxes[2][1]==current_player) or (boxes[0][2]==current_player and boxes[1][2]==current_player and boxes[2][2]==current_player) or (boxes[0][0]==current_player and boxes[1][1]==current_player and boxes[2][2]==current_player) or (boxes[0][2]==current_player and boxes[1][1]==current_player and boxes[2][0]==current_player):
            break
    print("")
    board(boxes)
    print("\n")
    print(f"Player {current_player}, you won!")

game(boxes)
