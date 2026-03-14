def board_creator(size, state=0):
    mainboard = [[state for _ in range(size)] for _ in range(size)]
    return mainboard

def board_display(board):
    for i in board:
        for j in i:
            print(j,end=" ")
        print()
    pass#this comment is being made to test the github-jetbrains sync

def board_updater(final_inputs,board):
    for i in final_inputs:
        row=int(i[0]-1)
        column=int(i[1]-1)
        value=int(i[2])
        board[row][column]=value
    board_display(board)
    pass

def input_parser(input_list,size,board):
    final_inputs=[]
    ignored_commands=0
    for i_input in input_list:
        user_demands=i_input.split(",")
        row=int(user_demands[0])
        column=int(user_demands[1])
        value=int(user_demands[2])
        if row < 1 or row > size or column < 1 or column > size or value < 0 or value > 9:
            ignored_commands+=1
            continue
        else:
            final_inputs.append([row,column,value])
    print("out of entered commands, {} have been ignored".format(ignored_commands))
    pass
    board_updater(final_inputs,board)

def user_input_intake(max_size,board):
    number_of_inputs=int(input("please enter the number of inputs: "))
    input_list=[]
    for i in range(number_of_inputs):
        a = input("enter a command for editing the cell which you want to edit in this format..(row,column,value)......")
        input_list.append(a)
    input_parser(input_list,max_size,board)

def main():

    while True:
        a = input("how many rows of a sudoku do you want to solve today bro..?")
        if a.isdigit():
            board = board_creator(int(a), 0)
            break
        else:
            print("please enter a valid size ")
    print("the board is ",board)
    #user_command(int(a),board)
    user_input_intake(int(a),board)
print(" ==========\'classic sudoku\'========== ")
main()




