def sum(a, b, c):
    return a + b + c

# print gboard
def gboard(xState, zState):
    zero = 'x' if xState[0] else ('o' if zState[0] else 0)
    one = 'x' if xState[1] else ('o' if zState[1] else 1)
    two = 'x' if xState[2] else ('o' if zState[2] else 2)
    three = 'x' if xState[3] else ('o' if zState[3] else 3)
    four = 'x' if xState[4] else ('o' if zState[4] else 4)
    five = 'x' if xState[5] else ('o' if zState[5] else 5)
    six = 'x' if xState[6] else ('o' if zState[6] else 6)
    seven = 'x' if xState[7] else ('o' if zState[7] else 7)
    eight = 'x' if xState[8] else ('o' if zState[8] else 8)

    print(f"{zero} | {one} | {two}")
    print("--|---|---")
    print(f"{three} | {four} | {five}")
    print("--|---|---")
    print(f"{six} | {seven} | {eight}")

# Check if any person is winner
def checkwinner(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            gboard(xState,zState)
            print(play_1,"WON THE MATCH")
            return 1
        
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            gboard(xState,zState)
            print(play_2,"WON THE MATCH")
            return 0
            
    return -1

#Check if the gboard is full
def is_board_full(xState, zState):
    return all(x or z for x, z in zip(xState, zState))

#Check if intput is valid or not
def get_valid_input():
    while True:
        value = input("Please enter a value: ")
        if value.isdigit():
            return int(value)
        else:
            print("Invalid input. Please enter an integer value between 0 to 8.")

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1

    print("Welcome to Tic-Tac-Toe")

    #inputs of names
    play_1 = input("Enter name of player1 : ")
    play_2 = input("Enter name of player2 : ")

    print(play_1,"Your turn is 'X' ")
    print(play_2,"Your turn is 'O' ")

    while True:
        gboard(xState, zState)

        if is_board_full(xState, zState):
            print("It's a DRAW!")
            break

        if turn == 1:
            print(play_1," turn")
            value = get_valid_input()

            if 0 <= value <= 8:
                if xState[value] == 0 and zState[value] == 0:
                    xState[value] = 1
                else:
                    print("Position already taken. Please choose another value.")
                    continue
            else:
                print("Invalid input. Please enter a value between 0 and 8.")
                continue
        else:
            print(play_2,"turn")
            value = get_valid_input()

            if 0 <= value <= 8:
                if xState[value] == 0 and zState[value] == 0:
                    zState[value] = 1
                else:
                    print("Position already taken. Please choose another value.")
                    continue
            else:
                print("Invalid input. Please enter a value between 0 and 8.")
                continue

        winner = checkwinner(xState, zState)
        
        if winner != -1:
            print("Match over!!") 
            break

        turn = 1 - turn