#!/usr/bin/env python3

import turtle
#TURTLE DOCUMENTATION: https://docs.python.org/2/library/turtle.html
 
	#Create a program that does the following:
		#done 01/22/2017o Trap all input errors and respond with a helpful message
		#
		#done 01/22/2017o Ask the user if they choose to draw squares, rectangles, circles,
		#	triangles, or 5-point stars.
		#
		#done 01/22/2017o Ask the user how many rows and columns of shapes they would like (1-20).
		#
		#done 01/22/2017o Ask the user to choose one of 10 colors for the shapes
		#
		#o Draw the shapes
		#
		#oWhen the user presses a key clear the graphics and give the user option to restart or
		#	quit the program.  
	
	#Please print some screenshots of your running program, as well as provide the source code. PyCharm does a very good job of printing nicely formatted Python source code. 

shapeToDraw = None
inputMessage = 'Would you like to draw some 1. squares, 2. rectangles, 3. circles, 4. triangles, or 5. 5-point stars? Enter a number and press enter: '
while shapeToDraw is None:
	try:
		shapeToDraw = float(input(inputMessage))
		#todo: convert the if elif block to a compound if statement
		if shapeToDraw == 1:
			break	#get out of the while loop and do the rest of the logic since the user input the correct options
		elif shapeToDraw == 2:
			break
		elif shapeToDraw == 3:
			break
		elif shapeToDraw == 4:
			break
		else:
			print('Error: please enter a 1, 2, 3, 4, or 5 to select the shape you want to draw and then press enter: ')
			shapeToDraw = None	#setting x back to none allows to re-execute the while loop to sort of trap the user until correct input is given
	
	except ValueError as error:
		#if I wanted to print the full error message I could do the following:
		#	`print(error)`
		print('Error: please choose a number: 1, 2, 3, 4, or 5 to select the shape you want to draw and then press enter: ')

#now I will ask the user for the number of rows they want to draw of the shape they choose
rows = None
inputMessage = 'How many rows of shapes would you like to draw? (1-20): '
while rows is None:
	try:
		rows = int(input(inputMessage))
		if rows >= 1 and rows <= 20:
			break	#if here then the user has entered a valid value
		else:
			print('Error: please enter a whole number that is between 1 and 20: ')
			rows = None	
	except ValueError as error:
		print('Error: please enter a whole number for the number of rows you want of your shape to draw that is between 1 and 20: ')


#now I will ask the user for the number columns they want to draw of the shape they chose
columns = None
inputMessage = 'How many columns of shapes would you like to draw? (1-20): '
while columns is None:
	try:
		columns = int(input(inputMessage))
		if columns >= 1 and columns <= 20:
			break	#if here then the user has entered a valid value
		else:
			print('Error: please enter a whole number that is between 1 and 20: ')
			columns = None	
	except ValueError as error:
		print('Error: please enter a whole number for the number of columns you want of your shape to draw that is between 1 and 20: ')


#now I will ask the user for the color they want the shapes to be
color = None
inputMessage = 'What color do you want the shapes to be? 1. red 2. orange 3. yellow 4. blue 5. purple 6. green 7. black 8. gray 9. pink 10. turquoise (1-10): '
while color is None:
	try:
		color = int(input(inputMessage))
		if color >= 1 and color <= 10:
			break	#if here then the user has entered a valid value
		else:
			print('Error: please enter a whole number that is between 1 and 10: ')
			color = None	
	except ValueError as error:
		print('Error: please enter a whole number for the color you want the shapes to be. 1. red 2. orange 3. yellow 4. blue 5. purple 6. green 7. black 8. gray 9. pink 10. turquoise (1-10): ')

#singleton turtle instance and constants
myTurtle = turtle.Turtle(shape="arrow")
circlesCreated = 0
circleRadius = 25

#function definitions
def drawCircle( numberOfRows, numberOfColumns ):
	x = 50	#I will default the x and y to 50
	y = 50
	#do some stuff
	for i in range(0, numberOfRows):		#for each of the rows
		for i in range(0, numberOfColumns):	#and also for each of the columns I need to create circles
			myTurtle.penup()
			myTurtle.setposition(x, y)
			myTurtle.pendown()
			myTurtle.circle(circleRadius)
			global circlesCreated 
			circlesCreated += 1
			#while I am in the columns for loop section I will only worry about incrementing the y position
			y += 50

			if circlesCreated >= numberOfRows:
				#now that I have completed a full column, it is time to reset the y to do the next row
				#I will also set the x value here for the next iteration
				y = 50
				x += 50
				circlesCreated = 0

	'''
	myTurtle.penup()
	myTurtle.setposition(20, 20)
	myTurtle.pendown()
	myTurtle.circle(20)
	'''


	'''
	CircleCount=input("How many circles?")

myTurtle = turtle.Turtle(shape="arrow")
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-120, 0)
myTurtle.pendown()
myTurtle.circle(50)

	
def drawRectangle( arg1, arg2 ):
	#do some stuff
	
def drawSquare( arg1, arg2 ):
	#do some stuff
	
def drawStar( arg1, arg2 ):
	#do some stuff
	'''
#now that I know the number of rows and columns the user wants to draw of the shape
#as well as its color, its time to actually draw the shapes
	#2. rectangles, 3. circles, 4. triangles, or 5. 5-point stars? Enter a number and press enter: '
if shapeToDraw == 1:
	#squares
	print('true')
elif shapeToDraw == 2:
	#rectangles
	print('true')
elif shapeToDraw == 3:
	#circles
	drawCircle(rows,columns)
elif shapeToDraw == 4:
	print('true')


#help for using the turtle api
'''
CircleCount=input("How many circles?")

myTurtle = turtle.Turtle(shape="arrow")
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-120, 0)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(60, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.penup()
myTurtle.setposition(-180, 60)
myTurtle.pendown()
myTurtle.circle(50)
'''

