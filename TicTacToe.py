
import turtle
import time
import random

# This list represents the state of the
# board. It's a list of nine strings,
# each of which is either "X", "O", "_",
# representing, respectively,
# a position occupied by an X, by an O, and
# an unoccupied position. The first three
# elements in the list represent the first row,
# and so on. Initially, all positions are
# unoccupied.

the_board = [ "_", "_", "_",
              "_", "_", "_",
              "_", "_", "_"]



    
def draw_board(board):
    """
    signature: list(str) -> NoneType
    The current state of the board, indicating
    the position of all pieces, is given
    as a parameter. This function should draw
    the entire board on the screen using turtle.
    It must draw the grid lines as well as
    the X and O pieces at the position
    indicated by the parameter.
    Hint: Write this function first!
    """
    turtle.setheading(0)
    turtle.pencolor('black')
    turtle.setup(600,600)
    x=turtle.window_width()
    y=turtle.window_height()
    #print(x)
    #print(y)
    turtle.clear()
    turtle.goto(0,0)
    turtle.up()
    turtle.forward(100)
    turtle.left(90)
    turtle.down()
    turtle.forward(300)
    turtle.backward(600)
    turtle.up()
    turtle.goto(0,0)
    turtle.left(90)
    turtle.forward(100)
    turtle.down()
    turtle.right(90)
    turtle.forward(300)
    turtle.backward(600)
    turtle.up()
    turtle.goto(0,0)
    turtle.forward(100)
    turtle.left(90)
    turtle.down()
    turtle.forward(300)
    turtle.backward(600)
    turtle.up()
    turtle.goto(0,0)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.down()
    turtle.forward(300)
    turtle.backward(600)
    turtle.update()
    for i in range(len(board)):
        turtle.setheading(0)
        if (i%3==0):
            xcoord = -200
        elif (i%3==1):
            xcoord = 0
        else:
            xcoord = 200

        if (i<=2):
            ycoord = 200
        elif (i<=5 and i>2):
            ycoord = 0
        else:
            ycoord = -200

        if board[i] =="X":
            draw_x(xcoord,ycoord)
            turtle.setheading(0)
        elif board[i]=="O":
            draw_circle(xcoord,ycoord)

    turtle.update()

    
################################################################################
#Drawing the Characters, X and O:
    
def draw_x(x,y):
    #sig: int, int-> nonetype
    turtle.penup()
    turtle.goto(x,y)
    turtle.color('blue')
    turtle.pendown()
    turtle.left(45)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(120)
    turtle.backward(60)
    turtle.left(90)
    turtle.forward(60)
    turtle.backward(120)
    turtle.penup()


      
def draw_circle(x,y):
    #sig: int, int-> nonetype
    turtle.up()
    turtle.goto(x,y-50)
    turtle.color('red')
    turtle.pendown()
    turtle.circle(60)
    turtle.up()

#print(draw_circle(0,0))

################################################################################
#Will be used to reset the board to an empty board.

new_board=[ "_", "_", "_",
            "_", "_", "_",
            "_", "_", "_"]
    
################################################################################  
def player_input(x,y): #identifies which position in the grid the user clicked on
    #sig: int,int, -> int
    if y >= 100 and y <= 300:
        if x >= -300 and x <= -100:
            board_pos=0
            #draw_circle(-200,200)
        elif x >= -100 and x<=100:
            board_pos=1
            #draw_circle(0,100)
        elif x > 100 and x <= 300:
            board_pos=2
            #draw_circle(200,200)
        return board_pos
    if 200 >=y and y >= -100:
        if -100 >= x >= -300:
            board_pos=3
            #draw_circle(-200,0)
        elif 100 >= x >=-100:
            board_pos=4
            #draw_circle(0,0)
        elif 300 >= x and x >100:
            board_pos=5
            #draw_circle(200,0)
        return board_pos
    if -100 >= y >= -300:
        if -100 >= x >= -300:
            board_pos=6
            #draw_circle(-200,-200)
        elif 100 >= x >=-100:
            board_pos=7
            #draw_circle(0,-200)
        elif 300 >= x >100:
            board_pos=8
            #draw_circle(200,-200)
        return board_pos
    return -1

def do_user_move(board, x, y):
    """
    signature: list(str), int, int -> bool
    if the user clicks on a position that is already occupied or outside of the board area, the move is
    invalid, and the function should return False, otherise True.
    """
    print("user clicked at "+str(x)+","+str(y))
    box=player_input(x,y)
    if box == -1:
        return False 
    if board[box] == 'O' or board[box]=='X':  #checks if the board is empty in the specified position, if not replaces with user move. 
        return False
    else:
        board[box]="O"
        return True
      
def check_game_over(board):
    global the_board
    """
    signature: list(str) -> bool
    Given the current state of the board, determine
    if the game is over, by checking for
    a three-in-a-row pattern in horizontal,
    vertical, or diagonal lines; and also if the
    game has reached a stalemate, achieved when
    the board is full and no further move is possible.
    If there is a winner or if there is a stalemante, display
    an appropriate message to the user and clear the board
    in preparation for the next round. If the game is over,
    return True, otherwise False.
    """
    #To check if any wins have been mande yet: 
    if board[0] == board[1] and board[1] == board[2] and board[0]!="_":  #horizontal win
        turtle.goto(0,0)
        result= str(board[0]) + " is the winner!"
        turtle.write(result)
        the_board=new_board[:]
        return True
    elif board[3]== board[4] and board[4] == board[5] and board[3]!="_":
        turtle.goto(0,0)
        result= str(board[3]) + " is the winner!"
        turtle.write(result)
        the_board=new_board[:]
        return True
    elif board[6]== board[7] and board[7]==board[8] and board[6]!="_":
        turtle.goto(0,0)
        result= str(board[6]) + " is the winner!"
        turtle.write(result)
        the_board=new_board[:]
        return True
    elif board[0]==board[4] and board[4]==board[8] and board[4]!="_":  #diagonal win
        turtle.goto(0,0)
        result= str(board[0]) + " is the winner!"
        turtle.write(result)
        the_board=new_board[:]
        return True
    elif board[2]==board[4] and board[4]==board[6] and board[2]!="_":
        turtle.goto(0,0)
        result= str(board[2]) + " is the winner!"
        turtle.write(result)
        the_board=new_board[:]
        return True
    elif board[0]==board[3] and board[3]==board[6] and board[0]!="_":   #vertical win
        turtle.goto(0,0)
        result= str(board[0]) + " is the winner!"
        turtle.write(result)
        the_board=new_board[:]
        return True
    elif board[1]==board[4] and board[4]==board[7] and board[1]!="_":
        turtle.goto(0,0)
        result= str(board[1]) + " is the winner!"
        turtle.write(result)
        the_board=new_board[:]
        return True
    elif board[2]==board[5] and board[5]==board[8] and board[2]!="_":
        turtle.goto(0,0)
        result= str(board[2]) + " is the winner!"
        turtle.write(result)
        the_board=new_board[:]
        return True
    elif board.count("_")==0:
        the_board=new_board[:]
        turtle.goto(0,0)
        result= "Stalemate!"
        turtle.write(result)
        return True
    else:
        return False
def whose_winning(board,available_spots, player):
    for j in available_spots:
        if j%3==0:
            column = [board[0],board[3],board[6]]
            if column.count(player)==2:
                return j
        elif j%3==1:
            column = [board[1],board[4],board[7]]
            if column.count(player) == 2:
                return j
        elif j%3==2:
            column = [board[2],board[5],board[8]]
            if column.count(player) == 2:
                return j
        if 0<=j<=2:
            row = [board[0],board[1],board[2]]
            if row.count(player)==2:
                return j
        elif 3<=j<=5:
            row = [board[3],board[4],board[5]]
            if row.count(player)==2:
                return j
        elif 6<=j<=8:
            row = [board[6],board[7],board[8]]
            if row.count(player)==2:
                return j
        if j in [0,4,8]:
            diagonal = [board[0],board[4],board[8]]
            if diagonal.count(player)==2:
                return j
        elif j in [2,4,6]:
            diagonal = [board[2],board[4],board[6]]
            if diagonal.count(player)==2:
                return j
    return -1
def priority_cross(board,available_spots):
    '''

    :param board:
    :param available_spots: list of indices of board with available position
    :return: the best index that blocks possible win of the user
    '''
    ind_X = whose_winning(board,available_spots, "X")
    if  ind_X!= -1:
        return ind_X
    ind_O = whose_winning(board, available_spots, "O")
    if ind_O!=-1:
        return ind_O
    return available_spots[random.randint(0, len(available_spots) - 1)]


def do_computer_move(board):
    """
    signature: list(str) -> NoneType
    Given a list representing the state of the board,
    select a position for the computer's move and
    update the board with an X in an appropriate
    position. The algorithm for selecting the
    computer's move shall be as follows: if it is
    possible for the computer to win in one move,
    it must do so. If the human player is able 
    to win in the next move, the computer must
    try to block it. Otherwise, the computer's
    next move may be any random, valid position
    (selected with the random.randint function).
    """
    available_spots=[]
    for i in range(len(board)):
        if board[i]=="_":
            available_spots.append(i)
    ind = priority_cross(board,available_spots)
    board[ind] = "X"



def clickhandler(x, y):
    #signature: int, int -> NoneType
    global the_board
    if do_user_move(the_board,x,y):
        draw_board(the_board)
        if check_game_over(the_board) == False:
            do_computer_move(the_board)
            draw_board(the_board)
            check_game_over(the_board)
        #draw_board(the_board)

def main():
    """
    signature: () -> NoneType
    Runs the tic-tac-toe game. You shouldn't
    need to modify this function.
    """
    turtle.tracer(0,0)
    #turtle.hideturtle()
    turtle.onscreenclick(clickhandler)
    draw_board(the_board)
    turtle.mainloop()

main()
