from logo import Logo

BOX = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
BOX_OF_X = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
BOX_OF_O = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
valid_moves = ["00", "01", "02", "11", "10", "12", "20", "21", "22"]


def draw():
    print("   |   |   ")
    print(f" {BOX[0][0]} | {BOX[0][1]} | {BOX[0][2]} ")
    print("   |   |   ")
    print("--- --- ---")
    print("   |   |   ")
    print(f" {BOX[1][0]} | {BOX[1][1]} | {BOX[1][2]} ")
    print("   |   |   ")
    print("--- --- ---")
    print("   |   |   ")
    print(f" {BOX[2][0]} | {BOX[2][1]} | {BOX[2][2]} ")
    print("   |   |   ")


def win_check_for_x():
    for i in range(0, 3):
        sum1 = int(BOX_OF_X[i][0])+int(BOX_OF_X[i][1])+int(BOX_OF_X[i][2])
        sum2 = int(BOX_OF_X[0][i]) + int(BOX_OF_X[1][i]) + int(BOX_OF_X[2][i])
        if sum1 == 3 or sum2 == 3:
            print("X WON")
            return True
    if int(BOX_OF_X[0][0])+int(BOX_OF_X[1][1])+int(BOX_OF_X[2][2]) == 3:
        print("X WON")
        return True
    if int(BOX_OF_X[2][0])+int(BOX_OF_X[1][1])+int(BOX_OF_X[0][2]) == 3:
        print("X WON")
        return True


def win_check_for_o():
    for i in range(0, 3):
        sum1 = int(BOX_OF_O[i][0])+int(BOX_OF_O[i][1])+int(BOX_OF_O[i][2])
        sum2 = int(BOX_OF_O[0][i]) + int(BOX_OF_O[1][i]) + int(BOX_OF_O[2][i])
        if sum1 == 3 or sum2 == 3:
            print("O WON")
            return True
    if int(BOX_OF_O[0][0])+int(BOX_OF_O[1][1])+int(BOX_OF_O[2][2]) == 3:
        print("O WON")
        return True
    if int(BOX_OF_O[2][0])+int(BOX_OF_O[1][1])+int(BOX_OF_O[0][2]) == 3:
        print("O WON")
        return True


print(Logo)
play = True
turn = "1"
while play:
    if turn == "1":
        if win_check_for_o():
            play = False
            draw()
            break
        print("...X's Turn...")
        print("ENTER BOX INDEX(00-22) TO PLACE YOUR MARK(X)")
        draw()
        index_position = input(": ")
        if index_position not in valid_moves:
            print("INVALID INDEX ENTERED")
        elif BOX_OF_X[int(index_position[0])][int(index_position[1])] == 1 or BOX_OF_O[int(index_position[0])][int(index_position[1])] == 1:
            print("INVALID MOVE TRY AGAIN!")
        else:
            BOX[int(index_position[0])][int(index_position[1])] = "X"
            BOX_OF_X[int(index_position[0])][int(index_position[1])] = 1
            turn = "0"
    else:
        if win_check_for_x():
            play = False
            draw()
            break
        print("...O's Turn...")
        print("ENTER BOX INDEX(00-22) TO PLACE YOUR MARK(O)")
        draw()
        index_position = input(": ")
        if index_position not in valid_moves:
            print("INVALID INDEX ENTERED")
        elif BOX_OF_X[int(index_position[0])][int(index_position[1])] == 1 or BOX_OF_O[int(index_position[0])][int(index_position[1])] == 1:
            print("INVALID MOVE TRY AGAIN!")
        else:
            BOX[int(index_position[0])][int(index_position[1])] = "O"
            BOX_OF_O[int(index_position[0])][int(index_position[1])] = 1
            turn = "1"
