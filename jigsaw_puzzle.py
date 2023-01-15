
#-----Assignment Description-----------------------------------------#
#
#  FOUR PIECE JIGSAW PUZZLE
#
#  This assignment tests your skills at defining functions, processing
#  data stored in lists and performing the arithmetic calculations
#  necessary to display a complex visual image.  The incomplete
#  Python script below is missing a crucial function, "draw_attempt".
#  You are required to complete this function so that when the
#  program is run it produces a picture of a jigsaw puzzle whose
#  state of completion is determined by data stored in a list which
#  specifies the locations of the pieces.  You are also required to
#  provide a solution to your particular puzzle.  See the instruction
#  sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.

from turtle import *
from math import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

size_of_pieces = 300 # pixels (excluding any protruding "tabs")
half_piece_size = size_of_pieces / 2
max_tab_size = 100 # pixels
box_size = size_of_pieces + (max_tab_size * 2)
half_box_size = box_size / 2
left_border = max_tab_size
gap = max_tab_size
top_bottom_border = max_tab_size
canvas_height = (top_bottom_border + size_of_pieces) * 2
canvas_width = (size_of_pieces * 2 + left_border) * 2
template_centres = [[-(size_of_pieces + half_piece_size), -half_piece_size], # bottom left
                    [-half_piece_size, -half_piece_size], # bottom right
                    [-(size_of_pieces + half_piece_size), half_piece_size], # top left
                    [-half_piece_size, half_piece_size]] # top right
box_centre = [gap + (box_size / 2), 0]

#
#--------------------------------------------------------------------#



#-----Functions for Drawing the Background---------------------------#
#
# The functions in this section are called by the main program to
# draw the background for the puzzle, i.e., the template for the
# pieces and the box they're kept in.  You should not change any of
# the code in this section.  Note that each of these functions
# leaves the turtle's pen up and at its standard width and colour.
#


# Draw the box that contains unused puzzle pieces.  (The box is
# larger than the puzzle pieces to allow for tabs sticking out on
# any of their four sides.)
def draw_box():

    # Determine the position of the box's bottom-left corner
    bottom_left = [box_centre[0] - half_box_size,
                   box_centre[1] - half_box_size]

    # Go to the bottom-left corner and get ready to draw
    penup()
    goto(bottom_left)
    width(5)
    color('black')
    pendown()
    
    # Walk around the box's perimeter
    setheading(0) # point east
    for side in [1, 2, 3, 4]:
        forward(box_size)
        left(90)

    # Reset the pen
    width(1)
    penup()
 

# Draw the individual squares of the jigsaw's template
def draw_template(show_template = False):

    # Only draw if the argument is True
    if show_template:

        # Set up the pen
        width(3)
        color('grey')

        # Draw a box for each centre coordinate
        for centre_x, centre_y in template_centres:
            
            # Determine the position of this square's bottom-left corner
            bottom_left = [centre_x - half_piece_size,
                           centre_y - half_piece_size]

            # Go to the bottom-left corner and get ready to draw
            penup()
            goto(bottom_left)
            pendown()
        
            # Walk around the square's perimeter
            setheading(0) # point east
            for side in [1, 2, 3, 4]:
                forward(size_of_pieces)
                left(90)

        # Reset the pen
        width(1)
        color('black')
        penup()


# As a debugging aid, mark the coordinates of the centres of
# the template squares and the box
def mark_coords(show_coords = False):

    # Only mark the coordinates if the argument is True
    if show_coords:

        # Don't draw lines between the coordinates
        penup()

        # Go to each coordinate, draw a dot and print the coordinate
        color('black')
        for x_coord, y_coord in template_centres + [box_centre]:
            goto(x_coord, y_coord)
            dot(4)
            write(str(x_coord) + ', ' + str(y_coord),
                  font = ('Arial', 12, 'normal'))

    # Reset the pen
    width(1)
    penup()
               
#
#--------------------------------------------------------------------#



#-----Test data------------------------------------------------------#
#
# These are the data sets you will use to test your code.
# Each of the data sets is a list specifying the locations of
# jigsaw puzzle pieces:
#
# 1. The name of the piece, from 'Piece A' to 'Piece D'
# 2. The place to put the piece, either in the template, denoted
#    'Top left', 'Top right', 'Bottom left' or 'Bottom right', or
#    in the unused pieces box, denoted 'In box'
# 3. An optional mystery value, 'X', whose purpose will be
#    revealed only in the second part of the assignment
#
# Each data set does not necessarily mention all pieces.  Also notice
# that several pieces may be in the box at the same time, in which
# case they should just be drawn on top of each other.
#
# You can create further data sets, but do not change any of the
# given ones below because they will be used to test your submission.
#
# Most importantly, you must write your own data set at the end
# to provide the correct solution to your puzzle.
#

# The following data set doesn't require drawing any jigsaw pieces
# at all.  You may find it useful as a dummy argument when you
# first start developing your "draw_attempt" function.

attempt_00 = []

# Each of the following data sets put just one piece in the box.
# You may find them useful when creating your individual pieces.

attempt_01 = [['Piece A', 'In box']]
attempt_02 = [['Piece B', 'In box']]
attempt_03 = [['Piece C', 'In box']]
attempt_04 = [['Piece D', 'In box']]

# Each of the following data sets put just one piece in a
# location in the template.

attempt_05 = [['Piece A', 'Top left']]
attempt_06 = [['Piece B', 'Bottom right']]
attempt_07 = [['Piece C', 'Top right']]
attempt_08 = [['Piece D', 'Bottom left']]
attempt_09 = [['Piece A', 'Bottom left']]
attempt_10 = [['Piece B', 'Top left']]
attempt_11 = [['Piece C', 'Bottom right']]
attempt_12 = [['Piece D', 'Top right']]

# Each of the following data sets put all four pieces in the
# box, but in different orders.

attempt_13 = [['Piece A', 'In box'], ['Piece B', 'In box'],
              ['Piece C', 'In box'], ['Piece D', 'In box']]
attempt_14 = [['Piece D', 'In box'], ['Piece C', 'In box'],
              ['Piece B', 'In box'], ['Piece A', 'In box']]
attempt_15 = [['Piece C', 'In box'], ['Piece D', 'In box'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]

# Each of the following data sets uses between two and four pieces,
# either in the template or in the box

attempt_16 = [['Piece A', 'Top right'], ['Piece B', 'Bottom left']]
attempt_17 = [['Piece D', 'Bottom right'], ['Piece C', 'In box']]
attempt_18 = [['Piece C', 'Bottom right'], ['Piece A', 'Bottom right']]
attempt_19 = [['Piece B', 'In box'], ['Piece D', 'Top left'],
              ['Piece C', 'In box']]
attempt_20 = [['Piece C', 'Top left'], ['Piece D', 'Top right'],
              ['Piece A', 'Bottom left']]
attempt_21 = [['Piece A', 'In box'], ['Piece D', 'Bottom left'],
              ['Piece C', 'Top right']]
attempt_22 = [['Piece A', 'Bottom left'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom right'], ['Piece D', 'In box']]
attempt_23 = [['Piece D', 'Bottom right'], ['Piece C', 'In box'],
              ['Piece B', 'Top right'], ['Piece A', 'Top left']]
attempt_24 = [['Piece C', 'Bottom right'], ['Piece D', 'Top left'],
              ['Piece A', 'In box'], ['Piece B', 'In box']]
attempt_25 = [['Piece D', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece C', 'Bottom right'], ['Piece A', 'Top right']]
attempt_26 = [['Piece C', 'Bottom left'], ['Piece B', 'In box'],
              ['Piece A', 'Bottom right'], ['Piece D', 'Top right']]
attempt_27 = [['Piece C', 'Bottom left'], ['Piece D', 'In box'],
              ['Piece A', 'Top left'], ['Piece B', 'Top right']]

# Each of the following data sets is a complete attempt at solving
# the puzzle using all four pieces (so there are no pieces left in the box)

attempt_28 = [['Piece A', 'Bottom left'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Top right']]
attempt_29 = [['Piece A', 'Top right'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left']]
attempt_30 = [['Piece A', 'Bottom left'], ['Piece B', 'Top left', 'X'],
              ['Piece C', 'Bottom right'], ['Piece D', 'Top right']]
attempt_31 = [['Piece A', 'Bottom right'], ['Piece B', 'Top right'],
              ['Piece C', 'Bottom left', 'X'], ['Piece D', 'Top left']]
attempt_32 = [['Piece D', 'Top right', 'X'], ['Piece A', 'Bottom left', 'X'],
              ['Piece B', 'Top left'], ['Piece C', 'Bottom right']]
attempt_33 = [['Piece A', 'Top right', 'X'], ['Piece B', 'Bottom right'],
              ['Piece C', 'Top left'], ['Piece D', 'Bottom left', 'X']]
# Here you must provide a list which is the correct solution to
# your puzzle.

# ***** Put the solution to your puzzle in this list
solution = [
['Piece A', 'Top left'], 
['Piece B', 'Top right'], 
['Piece C', 'Bottom left'],
['Piece D', 'Bottom right']] 

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "draw_attempt" function.
#

# Draw the jigsaw pieces as per the provided data set
def draw_attempt(dummy_parameter):
    dict = { 'Piece A' : draw_piece_A,  'Piece B' : draw_piece_B, 'Piece C' : draw_piece_C, 'Piece D' : draw_piece_D }
    for next_param in dummy_parameter:
        piece, place = next_param[0], next_param[1]
        # Draw image section
        dict[piece](get_coords(place))

# Function return coordinates for each placeholder (Top left, Top right, Bottom left, Bottom right, In box)
def get_coords(place):
    if place == 'Top left':
        return { 'x' : -450, 'y' : 150 }
    elif place == 'Top right':
        return { 'x' : -150, 'y' : 150 }
    elif place == 'Bottom left':
        return { 'x' : -450, 'y' : -150 }
    elif place == 'Bottom right':
        return { 'x' : -150, 'y' : -150 }
    elif place == 'In box':
        return { 'x' : 350, 'y' : 0 }
    else:
        return { 'x' : 0, 'y' : 0 }

# Left top part of image
def draw_piece_A(place, X=None):
    print('Draw A at: ', place)
    ### Draw image piece border
    # Set pen size to 2
    pensize(2)
    # Remove brush from paper
    up()
    # Move to the origin
    home()
    # Set pen color (borders), and fillcolor (inner part)
    pencolor('black')
    fillcolor('white')
    # Move to the apropriate place
    setpos(place['x'] - 150, place['y'] - 150)
    # Put brush to the 'paper'
    down()
    begin_fill()
    # Bottom part of border
    forward(105)
    right(90)
    forward(40)
    left(90)
    forward(60)
    left(90)
    forward(40)
    right(90)
    forward(135)
    # Right side
    left(90)
    forward(139)
    right(90)
    forward(40)
    left(90)
    forward(60)
    left(90)
    forward(40)
    right(90)
    forward(101)
    left(90)
    # Top and left side
    forward(300)
    left(90)
    forward(300)
    end_fill()
    up()
    ### Draw Homer head
    pensize(3)
    home()
    setpos(place['x'] + 52, place['y'] - 149)  
    pencolor('black')
    fillcolor('gold')
    begin_fill()
    down()
    left(108)
    forward(125)    
    right(18)
    forward(40)    
    right(38)
    forward(50)
    right(12)
    forward(29)
    right(15)
    forward(32)
    right(25)
    forward(54)
    right(90)
    pensize(1)
    forward(30)
    left(90)
    forward(40)
    right(90)
    forward(60)
    right(90)
    forward(40)	
    left(90)
    forward(139)
    end_fill()
    up()
    ### Draw Homer hair at the top
    pensize(3)
    home()
    setpos(place['x'] + 140, place['y'] + 79)  
    down()
    left(110)
    circle(39, 210)
    up()
    home()
    setpos(place['x'] + 90, place['y'] + 77)  
    down()
    left(125)
    circle(39, 210)
    up()
    ### Draw Homer hair at the bottom
    home()
    setpos(place['x'] + 27, place['y'] - 140)    
    down()
    left(95)
    forward(45)
    right(135)
    forward(45)
    left(135)
    forward(45)
    right(135)
    forward(45)
    up()	
	### Draw left eye (Outer circle)
    home()
    setpos(place['x'] + 148, place['y'] - 135)   
    pencolor('black')
    fillcolor('white')
    down()
    begin_fill()
    circle(47, -180)    
    end_fill()
    up()
	### Draw left eye (inner circle)
    home()
    setpos(place['x'] + 149, place['y'] - 93)  	
    pencolor('black')
    fillcolor('black')
    down()
    begin_fill()
    circle(6, -180)    
    end_fill()
    up()
    #######

def draw_piece_B(place, X=None):
    print('Draw B at: ', place)
    ### Draw border for current image piece 
    pensize(2)
    up()
    home()
    pencolor('black')
    fillcolor('white')
    setpos(place['x'] - 150, place['y'] - 150)  
    down()
    begin_fill()
    forward(135)
    right(90)
    forward(40)
    left(90)
    forward(60)
    left(90)
    forward(40)
    right(90)
    forward(105)
    left(90)
    forward(300)
    left(90)
    forward(300)
    left(90)
    forward(101)
    left(90)
    forward(40)
    right(90)
    forward(60)
    right(90)
    forward(40)
    left(90)
    forward(138)
    left(90)
    forward(135)
    right(90)
    forward(40)
    left(90)
    forward(60)
    left(90)
    forward(40)
    end_fill()
    # Draw Homer head
    pensize(3)
    up()
    home()    
    setpos(place['x'] - 148, place['y'] + 81)  
    pencolor('black')
    fillcolor('gold')
    begin_fill()
    down()
    right(17)
    forward(35)
    right(18)
    forward(20)
    right(20)
    forward(25)
    right(15)
    forward(50)
    left(46)
    forward(20)
    right(38)
    forward(15)
    right(47)
    forward(10)
    left(15)
    forward(50)
    left(15)
    forward(20)
    right(30)
    forward(38)
    right(25)
    forward(8)

    pensize(2)
    right(46)
    forward(87)
    right(90)
    forward(139)
    right(90)
    forward(40)
    left(90)
    forward(60)
    left(90)
    forward(40)
    right(90)
    forward(101)
    end_fill()    
    pensize(3)
    up()
    ### Draw Homer right eye (Outer circle)
    home()
    setpos(place['x'] - 74, place['y'] - 110)   
    pencolor('black')
    fillcolor('white')
    down()
    begin_fill()
    circle(41, 360)    
    end_fill()
    up()
	### Draw Homer right eye (inner circle)
    home()
    setpos(place['x'] - 70, place['y'] - 78)  	
    pencolor('black')
    fillcolor('black')
    down()
    begin_fill()
    circle(6, 360)    
    end_fill()
    up()
    ### Draw Homer left eye (Outer circle)
    home()
    setpos(place['x'] - 149, place['y'] - 135)   
    pencolor('black')
    fillcolor('white')
    down()
    begin_fill()
    circle(47, 180)    
    end_fill()
    up()
    ### Draw Homer left eye (inner circle)
    home()
    setpos(place['x'] - 149, place['y'] - 93)  	
    pencolor('black')
    fillcolor('black')
    down()
    begin_fill()
    circle(6, 180)    
    end_fill()
    up()
    ### Draw Homer nose
    home()
    setpos(place['x'] - 104, place['y'] - 95)   
    pencolor('black')
    fillcolor('gold')
    down()
    begin_fill()
    right(40)
    forward(12)
    left(40)
    forward(44)    
    right(45)
    forward(10)
    right(50)
    forward(17)
    right(35)
    forward(17)
    end_fill()
    up()
	

def draw_piece_C(place, X=None):
    print('Draw C at: ', place)
    ### Draw border for current chunk
    pensize(2)
    up()
    home()
    pencolor('black')
    fillcolor('white')
    setpos(place['x'] - 150, place['y'] - 150)  
    down()
    begin_fill()
    left(90)
    forward(300)
	
    right(90)
    forward(105)
    right(90)
    forward(40)
    left(90)
    forward(60)
    left(90)
    forward(40)
    right(90)
    forward(135)
	
    right(90)
    forward(130)
    left(90)
    forward(40)
    right(90)
    forward(60)
    right(90)
    forward(40)
    
    left(90)
    forward(110)
    right(90)
    forward(300)    
    
    end_fill()
    up()
    ### Draw Homer neck
    pensize(3)
    home()
    setpos(place['x'] + 52, place['y'] + 149)  
    pencolor('black')
    fillcolor('gold')
    begin_fill()
    down()
    right(87)
    forward(57)
    right(11)
    forward(47)
    right(11)
    forward(35)
    right(1)
    forward(21)
    left(90)
    forward(30)
    left(5)
    forward(94)
    left(105)    
    forward(1)
    right(90)
    forward(40)
    left(90)
    forward(60)
    left(90)
    forward(40)
    right(90)
    forward(130)
    end_fill()
    up()
    ### Draw Homer shirt
    pensize(3)
    home()
    setpos(place['x'] - 5, place['y'] + 18)  	
    pencolor('black')
    fillcolor('white')
    down()
    right(45)
    forward(25)
    left(23)
    forward(18)
    up()
    home()
    setpos(place['x'] - 5, place['y'] + 18)
    down()
    left(45)
    forward(10)
    right(25)
    forward(30)
    right(15)
    forward(12)
    up()
    home()
    setpos(place['x'] - 5, place['y'] + 18)
    down()

    right(110)
    forward(70)
    
    begin_fill()
    left(70)
    forward(30)
    right(98)
    forward(17)
    backward(17)
    left(110)
    forward(25)
    left(5)
    forward(35)
    left(5)
    forward(78)
    left(80)
    forward(55)
    
    pensize(3)
    left(28)
    forward(25)
    end_fill()
    up()
    pensize(3)
	### Draw Homer ear
    home()
    setpos(place['x'] + 50, place['y'] + 86)
    down()
    pencolor('black')
    fillcolor('gold')
    begin_fill()
    circle(30)
    end_fill()
    up()
    left(90)
    forward(30)
    right(90)
    forward(15)
    left(80)
    down()
    circle(15, 160)
    up()
    left(80)    
    forward(15)
    right(80)
    down()
    backward(14)
    forward(15) 
    left(25)
    forward(10)
    up()
    ### Draw Homer mouth
    home()
    setpos(place['x'] + 149, place['y'] + 8)
    pencolor('black')
    fillcolor('DarkKhaki')
    down()
    begin_fill()
    circle(64, -180)
    left(90)
    up()
    forward(128)
    left(93)
    down()
    forward(40)
    right(3)
    left(90)
    forward(10)
    left(90)
    forward(40)   
    end_fill()
    up()

def draw_piece_D(place, X=None):
    print('Draw D at: ', place)
    ### Draw border for next image chunk
    pensize(2)
    up()
    home()
    pencolor('black')
    fillcolor('white')
    setpos(place['x'] - 150, place['y'] - 150)  
    down()
    begin_fill()
    forward(300)
    left(90)
    forward(300)
    left(90)
    forward(105)
    left(90)
    forward(40)
    right(90)
    forward(60)
    right(90)
    forward(40)
    left(90)
    forward(135)
	
    left(90)
    forward(130)
    left(90)
    forward(40)
    right(90)
    forward(60)
    right(90)
    forward(40)
    left(90)
    forward(110)    
    end_fill()
    up()
	### Draw part of Homer nose
    pensize(3)
    up()
    home()
    setpos(place['x'] - 67, place['y'] + 149)  
    pencolor('black')
    fillcolor('gold')
    begin_fill()
    down()
    right(150)
    forward(15)
    right(30)
    forward(40)
    left(10)
    forward(29)
    left(260)
    pensize(1)
    forward(14)
    end_fill()
    pensize(3)
    up()
    ### Draw part of Homer mouth
    home()
    setpos(place['x'] - 149, place['y'] + 135)  
    pencolor('black')
    fillcolor('DarkKhaki')
    down()
    begin_fill()
    left(15)
    forward(23)
    right(15)
    forward(60)
    right(5)
    forward(7)

    right(40)
    forward(18)	
    right(15)
    forward(17)
    right(15)
    forward(15)
    right(15)
    forward(10)
    left(75)
    forward(15)
    right(65)
    forward(10)
    right(5)
    forward(5)
    right(25)
    forward(10)
    right(15)
    forward(10)
    right(45)
    forward(35)
    right(10)
    forward(20)
    right(10)
    forward(45)
    end_fill()
    up()
    home()
    pensize(1)
    setpos(place['x'] - 149, place['y'] + 135)  
    down()
    begin_fill()
    right(90)
    forward(115)
    pensize(3)
    left(90)
    forward(40)
    right(90)
    forward(10)
    left(95)
    forward(20)

    left(10)
    forward(25)
    left(45)
    forward(20)
    right(45)
    forward(20)
    left(55)
    forward(15)
    end_fill()

    up()
    home()
    setpos(place['x'] - 149, place['y'] + 135)  
    pencolor('black')
    fillcolor('DarkKhaki')
    down()
    begin_fill()
    left(15)
    forward(23)
    right(15)
    forward(60)
    right(5)
    forward(7)

    right(40)
    forward(18)	
    right(15)
    forward(17)
    right(15)
    forward(15)
    right(15)
    forward(10)
    left(75)
    forward(15)
    right(65)
    forward(10)
    right(5)
    forward(5)
    right(25)
    forward(10)
    right(15)
    forward(10)
    right(45)
    forward(35)
    right(10)
    forward(20)
    right(10)
    forward(45)
    end_fill()
    up()
    ### Draw Homer shirt and neck
    home()
    setpos(place['x'] - 148, place['y'] - 43)  
    pencolor('black')
    fillcolor('white')
    down()
    begin_fill()
    right(15)
    forward(15)
    right(105)
    forward(26)
    left(210)
    forward(26)
    right(105)
    forward(15)
    right(40)
    forward(80)
    left(110)
    forward(90)
    backward(30)
    right(125)
    forward(90)
    end_fill()
    up()
 
    pensize(3)
    home()	
    setpos(place['x'] - 149, place['y'] - 42)
    down()
    begin_fill()
    right(15)
    forward(13)
    right(105)
    forward(29)
    left(210)	
    forward(30)
    end_fill()
    
    pensize(3)
    right(105)
    forward(15)
    right(40)
    forward(80)
    left(110)
    
    begin_fill()
    forward(90)
    right(120)    
    forward(80)
    right(120)
    forward(35)
    end_fill()
    
    right(65)
    forward(47)
    right(55)
    
    begin_fill()
    forward(30)
    left(95)
    forward(50)
    left(125)
    forward(15)
    left(10)
    forward(15)
    left(5)
    forward(21)
    left(12)
    forward(9)
    end_fill()

    pencolor('black')
    fillcolor('gold')
    begin_fill()
    backward(9)
    right(12)
    backward(21)
    right(5)
    backward(15)    
    backward(30)
    right(5)
    backward(10)
	
    left(90)
    backward(15)
    right(10)
    backward(5)
	
    pensize(1)
    left(90)
    backward(50)
    right(90)
    backward(40)
    left(90)
    backward(2)	
	
    left(85)
    backward(17)
    right(50)
    backward(78)
    left(110)
    backward(40)
    
    end_fill()
    up()

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your jigsaw pieces.  Do not change any of this code except
# where indicated by comments marked '*****'.
#
    
# Set up the drawing canvas
setup(canvas_width, canvas_height)

# Give the canvas a neutral background colour
# ***** You can change the background colour if necessary to ensure
# ***** good contrast with your puzzle pieces
bgcolor('light grey')

# Give the window a title
# ***** Replace this title with one that describes the picture
# ***** produced by solving your puzzle
title('Four Piece Jigsaw Puzzle - Describe your picture here')

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** while the cursor moves around the screen
tracer(True)

# Draw the box that holds unused jigsaw puzzle pieces
draw_box()

# Draw the template that holds the jigsaw pieces
# ***** If you don't want to display the template change the
# ***** argument below to False
draw_template(True)

# Mark the centres of the places where jigsaw puzzle pieces must
# be drawn
# ***** If you don't want to display the coordinates change the
# ***** argument below to False
mark_coords(True)

# Call the student's function to display the attempted solution
# ***** Change the argument to this function to test your
# ***** code with different data sets

draw_attempt(solution)

# Exit gracefully by hiding the cursor and releasing the window
tracer(True)
hideturtle()
done()

#
#--------------------------------------------------------------------#

