#!/usr/bin/env python3

#Author:	John Coty Embry
#Date:		01/31/2017
#Comment:	This program can be ran in the terminal on a computer that has python installed. This program will do the following

import turtle
#TURTLE DOCUMENTATION: https://docs.python.org/2/library/turtle.html
		#done 01/22/2017o Trap all input errors and respond with a helpful message
		#
		#done 01/22/2017o Ask the user if they choose to draw squares, rectangles, circles,
		#	triangles, or 5-point stars.
		#
		#done 01/22/2017o Ask the user how many rows and columns of shapes they would like (1-20).
		#
		#done 01/22/2017o Ask the user to choose one of 10 colors for the shapes
		#
		#done 01/31/2017o Draw the shapes
		#
		#done 01/31/2017oWhen the user presses a key clear the graphics and give the user option to restart or
		#	quit the program.  
	
	#Please print some screenshots of your running program, as well as provide the source code. PyCharm does a very good job of printing nicely formatted Python source code. 

keepRunningFlag = True

#singleton turtle instance and constants
myTurtle = turtle.Turtle(shape="arrow")
myTurtle.speed(0)			#to make it where there is no animation time

#variables that are used in the function definitions
circlesCreated = 0			#this will be some state to help me know well.. how many circles have been created for a particular iteration
circleRadius = 25
rectanglesCreated = 0
squaresCreated = 0
starsCreated = 0
trianglesCreated = 0

startingX = 0				#these variables will help me to finish the 5-point star drawing
startingY = 0

#function definitions
def drawCircle( numberOfRows, numberOfColumns ):
	x = -200				#I will default the x and y to -200
	y = -200
	for i in range(0, numberOfRows):		#for each of the rows
		for i in range(0, numberOfColumns):	#and also for each of the columns I need to create circles
			myTurtle.penup()
			myTurtle.setposition(x, y)
			myTurtle.pendown()
			myTurtle.circle(circleRadius)
			global circlesCreated			#to reference the global variable outside of this scope (I think..idk how python scopes work fully yet. I would imagin between the indentions of functions..)
			circlesCreated += 1
			#while I am in the columns for loop section I will only worry about incrementing the y position
			y += 50

			if circlesCreated >= numberOfRows:
				#now that I have completed a full column, it is time to reset the y to do the next row
				#I will also set the x value here for the next iteration
				y = -200
				x += 50
				circlesCreated = 0

def drawFivePointStart( numberOfRows, numberOfColumns ):
	x = -200	#I will default the x and y to -200
	y = -200

	for i in range(0, numberOfRows):		#for each of the rows
		for j in range(0, numberOfColumns):	#and also for each of the columns I need to create circles
			#this creates a 5 point start in svg's path attribute:
			#	`m 55 237 l 74 -228 l 74 228 L 9 96 h 240`
			#use this to help draw the start in turtle graphics
			
			startingX = x	#save these for later to actually complete the start drawing
			startingY = y

			myTurtle.penup()
			myTurtle.setposition(x, y)
			myTurtle.pendown()
			
			x += 50
			#y -= 25
			myTurtle.setposition(x, y)
			x -= 25
			y -= 25
			myTurtle.setposition(x, y)
			x -= 25
			y += 25
			myTurtle.setposition(x, y)
			#x += 50
			#y -= 25

			myTurtle.penup()
			x += 25
			y += 25
			myTurtle.setposition(x, y)
			myTurtle.pendown()

			x += 12.5
			y -= 75
			myTurtle.setposition(x, y)
			x -= 12.5
			y += 25
			myTurtle.setposition(x, y)
			x -= 12.5
			y -= 25
			myTurtle.setposition(x, y)
			x += 12.5
			y += 75
			myTurtle.setposition(x, y)
			
			x -= 25
			y -= 25

			global starsCreated 
			starsCreated += 1
			#while I am in the columns for loop section I will only worry about incrementing the y position
			y += 75

			if starsCreated >= numberOfRows:
				#now that I have completed a full column, it is time to reset the y to do the next row
				#I will also set the x value here for the next iteration
				y = -200
				x += 50
				starsCreated = 0
	


def drawRectangle( numberOfRows, numberOfColumns ):
	x = -200								#I will default the x and y to -200
	y = -200

	for i in range(0, numberOfRows):		#for each of the rows
		for i in range(0, numberOfColumns):	#and also for each of the columns I need to create circles
			myTurtle.penup()
			myTurtle.setposition(x, y)
			myTurtle.pendown()

			x += 70							#to make it rectangular
			myTurtle.setposition(x, y)

			y += 50
			myTurtle.setposition(x, y)

			x -= 70
			myTurtle.setposition(x, y)

			y -= 50
			myTurtle.setposition(x, y)

			global squaresCreated 
			squaresCreated += 1
			#while I am in the columns for loop section I will only worry about incrementing the y position
			y += 50

			if squaresCreated >= numberOfRows:
				#now that I have completed a full column, it is time to reset the y to do the next row
				#I will also set the x value here for the next iteration
				y = -200
				x += 70
				squaresCreated = 0

def drawSquare( numberOfRows, numberOfColumns ):
	x = -200								#I will default the x and y to -200
	y = -200

	for i in range(0, numberOfRows):		#for each of the rows
		for i in range(0, numberOfColumns):	#and also for each of the columns I need to create circles
			myTurtle.penup()
			myTurtle.setposition(x, y)
			myTurtle.pendown()

			x += 50
			myTurtle.setposition(x, y)

			y += 50
			myTurtle.setposition(x, y)

			x -= 50
			myTurtle.setposition(x, y)

			y -= 50
			myTurtle.setposition(x, y)

			global squaresCreated 
			squaresCreated += 1
			#while I am in the columns for loop section I will only worry about incrementing the y position
			y += 50

			if squaresCreated >= numberOfRows:
				#now that I have completed a full column, it is time to reset the y to do the next row
				#I will also set the x value here for the next iteration
				y = -200
				x += 50
				squaresCreated = 0

def drawTriangle( numberOfRows, numberOfColumns ):
	x = -200								#I will default the x and y to -200
	y = -200

	for i in range(0, numberOfRows):		#for each of the rows
		for i in range(0, numberOfColumns):	#and also for each of the columns I need to create circles
			myTurtle.penup()
			myTurtle.setposition(x, y)
			myTurtle.pendown()

			x += 50
			myTurtle.setposition(x, y)

			x -= 25
			y += 50
			myTurtle.setposition(x, y)

			x -= 25
			y -= 50
			myTurtle.setposition(x, y)


			global trianglesCreated 
			trianglesCreated += 1
			#while I am in the columns for loop section I will only worry about incrementing the y position
			y += 50

			if trianglesCreated >= numberOfRows:
				#now that I have completed a full column, it is time to reset the y to do the next row
				#I will also set the x value here for the next iteration
				y = -200
				x += 50
				trianglesCreated = 0

#here I will define the program
def Program():
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
			elif shapeToDraw == 5:
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
	inputMessage = 'What color do you want the shapes to be? 1. red 2. orange 3. yellow 4. green 5. blue 6. violet 7. purple 8. black 9. gray 10. pink (1-10): '
	while color is None:
		try:
			color = int(input(inputMessage))
			if color >= 1 and color <= 10:
				#if here then the user has entered a valid value
				if color == 1:
					color = 'red'
				elif color == 2:
					color = 'orange'
				elif color == 3:
					color = 'yellow'
				elif color == 4:
					color = 'green'
				elif color == 5:
					color = 'blue'
				elif color == 6:
					color = 'violet'
				elif color == 7:
					color = 'purple'
				elif color == 8:
					color = 'black'
				elif color == 9:
					color = 'gray'
				else:
					color = 'pink'
			else:
				print('Error: please enter a whole number that is between 1 and 10: ')
				color = None	
		except ValueError as error:
			print('Error: please enter a whole number for the color you want the shapes to be. 1. red 2. orange 3. yellow 4. blue 5. purple 6. green 7. black 8. gray 9. pink 10. turquoise (1-10): ')

	global myTurtle
	myTurtle.pencolor(color)	#to set the color of the pen


	#now that I know the number of rows and columns the user wants to draw of the shape
	#as well as its color, its time to actually draw the shapes
		#1. squares 2. rectangles, 3. circles, 4. triangles, or 5. 5-point stars
	if shapeToDraw == 1:
		#squares
		drawSquare(rows, columns)
	elif shapeToDraw == 2:
		#rectangles
		drawRectangle(rows, columns)
	elif shapeToDraw == 3:
		#circles
		drawCircle(rows, columns)
	elif shapeToDraw == 4:
		drawTriangle(rows, columns)
	elif shapeToDraw == 5:
		drawFivePointStart(rows, columns)


#now to actually run the program
while(keepRunningFlag == True):
	Program()

	answer = None
	while answer is None:
		try:
			answer = int(input('Would you like to run this again? 1. Yes 2. No '))
			#todo: change this to a compound if statement
			if answer == 1:
				break	#if here then the user has entered a valid value
			elif answer == 2:
				break	#if here then the user has entered a valid value
			else:
				print('Error: That is not a valid number: Would you like to run this again? 1. Yes 2. No ')
				answer = None
		except ValueError as error:
			print('Error: That is not a valid number: Would you like to run this again? 1. Yes 2. No ')

	if answer == 2:
		keepRunningFlag = False
	else:
		myTurtle.clear()


