import turtle
import random
import time
import numpy
import math
import matplotlib.pyplot as plt

class Archimedes:
    t = turtle.Turtle() #set turtle pen t
    iterations = 0
    def __init__(self, iterations=20):
        self.iterations = iterations
        
    def calculate(self):
        self.t.pencolor('red')
        self.t.speed(0) 
        startTime = time.time()
        self.t.penup()
        self.t.goto(-65, -125)
        self.t.pendown()
        # Set the initial number of sides for the inscribed and circumscribed polygons
        numSides = 6 #set initial number of sides for the inscribed and circumscribed polygons
        radius = 250 #set radius of circle for clarity
        sideLength = 2 * radius * math.sin(math.pi / numSides) #calculate the initial side length of the inscribed polygon
        piEstimatesList = [] #piEstimatesList to store estimates of pi
        adjustmentX = 0 #adjustmentX length for turtle to line up the polygons horizontally, set to 0 initially due to not needing an allignment
        adjustmentY = 12.5 #adjustmentY length for turtle to line up polygons vertically
        for i in range(self.iterations): #for loop for calculating the side length for the circumscribed polygon
            expr = 1 - (sideLength / 2)**2  #expr for later caculations, calculated here to check if less than zero
            if expr < 0: #if expr less than zero, set the sidelength to a very small value: 1e-10
                sideLength = 1e-10
            else: #else, calculate side length based on current side length and number of sides of the current polygon
                sideLength = math.sqrt(2 - 2 * math.sqrt(expr))
            p_inscribed = numSides * sideLength #calculate the perimeters of the inscribed polygons
            p_circumscribed = 2 * numSides * radius * math.sin(math.pi / numSides) #calculate the perimeter of the circumscribed polygon
            piEstimate = ((p_inscribed + p_circumscribed) / 2)/250 #calculate the piEstimate using the perimeters of the circumscribed and inscribed polygons
            piEstimatesList.append(piEstimate) #add current pi estimate to piEstimatesList
            # Draw the inscribed and circumscribed polygons
            self.t.penup() 
            self.t.pendown()
            if i >= 1:
                self.t.pencolor('blue')
                self.t.right(90)
                self.t.penup()
                self.t.forward(adjustmentY)
                self.t.left(90)
                self.t.pendown()
                adjustmentY = adjustmentY/4
            for j in range(numSides): #for loop for printing a polygon, based on the number of sides
                self.t.forward(radius * math.sin(math.pi / numSides)) #draw the side
                self.t.left(180 - (180 * (numSides - 2) / numSides)) #rotate to draw next side

            self.t.penup()
            adjustmentX = ((radius * math.sin(math.pi / numSides))/4)
            self.t.forward(adjustmentX)
            self.t.pendown()
            numSides *= 2 #Double the number of sides for the next iteration
        endTime = time.time()
        turtle.resetscreen()
        turtle.reset()
        print(f"Archimedes method for estimating pi:\nIteration(s): {self.iterations}\nPi estimates: {piEstimatesList}\nTime: {endTime - startTime} seconds\n")

class Accumulator:
    t = turtle.Turtle() # create a new turtle object
    iterations = 0 # initialize the number of iterations to zero

    def __init__(self, iterations=100):
        self.iterations = iterations # set the number of iterations

    def drawCircle(self, radius):
        """Draws a circle using the turtle graphics library"""
        # set turtle pen color and attributes
        self.t.color("black")
        self.t.hideturtle()
        self.t.speed(0)
        self.t.penup()
        self.t.setx(0)
        self.t.sety(-radius)
        self.t.pendown()
        self.t.width(3)
        self.t.circle(radius)

    def display(self, x, y, value):
        """Displays a point at the specified coordinates using the turtle graphics library"""
        self.t.speed(0)
        self.t.hideturtle()
        self.t.penup()
        self.t.setx(x)
        self.t.sety(y)
        self.t.pendown()
        # set turtle pen color based on whether the point is inside or outside the circle
        if value == 1:
            self.t.color("blue")
            self.t.dot()
        else:
            self.t.color("red")
            self.t.dot()

    def calculate(self, radius):
        """Calculates an approximation of pi using the Monte Carlo method"""
        startTime = time.time()
        insideCount = 0
        totalCount = 0
        piEstimatesList = []
        # loop through the specified number of iterations
        for i in range(self.iterations):
            # generate random x and y coordinates within the circle's radius
            x = random.uniform(-radius, radius)
            y = random.uniform(-radius, radius)
            # calculate the distance from the point to the center of the circle
            distance = math.sqrt(x**2 + y**2)
            # if the distance is less than or equal to the circle's radius, the point is inside the circle
            if distance <= radius:
                insideCount += 1
                self.display(x, y, 1)
            else:
                self.display(x, y, 0)
            totalCount += 1
            # calculate the current estimate of pi and add it to the list of estimates
            piEstimate = 4 * insideCount / totalCount
            piEstimatesList.append(piEstimate)

        endTime = time.time()
        # reset the turtle graphics window and print the results
        turtle.resetscreen()
        turtle.reset()
        print(f"Accumulator approximation method for estimating pi:\nIteration(s): {self.iterations}\nPi estimates: {piEstimatesList}\nTime: {endTime - startTime} seconds\n")
               
class MonteCarlo:
    t = turtle.Turtle()
    iterations = 0

    def __init__(self, iterations=100):
        self.iterations = iterations

    # to draw a square
    def drawSquare(self):
        self.t.hideturtle()
        self.t.penup()
        self.t.color("darkred")
        self.t.goto(-100.5, -100.5)
        self.t.pendown()
        self.t.goto(100.5, -100.5)
        self.t.goto(100.5, 100.5)
        self.t.goto(-100.5, 100.5)
        self.t.goto(-100.5, -100.5)

    # to draw a circle
    def drawCircle(self):
        self.t.color("burlywood4")
        self.t.hideturtle()
        self.t.speed(0)
        self.t.penup()
        self.t.setx(0)
        self.t.sety(-100)
        self.t.pendown()
        self.t.width(3)
        self.t.circle(100.5)

    # display the dots
    def display(self, x, y, value):
        self.t.speed(0)
        self.t.hideturtle()
        self.t.penup()
        self.t.setx(x * 100)
        self.t.sety(y * 100)
        self.t.pendown()
        # if it's inside the circle color green
        if value == 1:
            self.t.color("chartreuse3")
            self.t.dot()
        # otherwise dot is red
        else:
            self.t.color("brown3")
            self.t.dot()

    # calculate the approximate value
    def calculate(self):
        iterationList = list()
        resultList = list()

        # draw the shapes
        self.drawCircle()
        self.drawSquare()

        squarePts = 0
        circlePts = 0

        # iterate n times and generate random values x, y
        for i in range(self.iterations):
            x = random.uniform(-1, 1)
            y = random.uniform(-1, 1)

            # check if x, y is in the circle using pythagorean theorem
            if ((x ** 2 + y ** 2) <= 1):
                self.display(x, y, 1)
                squarePts += 1
                circlePts += 1
            else:
                self.display(x, y, 0)
                squarePts += 1

            # calculate the approximate value
            result = 4 * (circlePts / squarePts)
            resultList.append(result)
            iterationList.append(i)
            print(i, ":", result)

        # draw the shapes again
        self.drawCircle()
        self.drawSquare()
        
        # draw the table
        plt.semilogx(resultList)
        plt.xlabel("Number of iterations")
        plt.ylabel("Current approximation")
        plt.axhline(numpy.pi, color="r", alpha=0.5);
        plt.show()

def main():
    print("Pi Computation Program")
    while True:
        print("1) Archimedes Approach\n2) Accumulator Approximations\n3) Monte Carlo Method \n4) Exit")
        userInput = input("Select an option: ")
        if userInput == "1":
            print("Archimedes Approach Selected:")
            while True:
                try:
                    iterations = int(input("Please input the number of iterations: : "))
                    archmed = Archimedes(iterations)
                    archmed.calculate()
                    break
                except ValueError:
                    print("Invalid input. Please input the number of iterations: : ")
        elif userInput == "2":
            print("Accumulator Approximation Selected")
            while True:
                try:
                    iterations = int(input("Please input the number of iterations: : "))
                    acc = Accumulator(iterations)
                    acc.drawCircle(iterations)
                    acc.calculate(iterations)
                    break
                except ValueError:
                    print("Invalid input. Please input the number of iterations: : ")
        elif userInput == "3":
            print("Monte Carlo Method Selected")
            while True:
                try:
                    iterations = int(input("Please input  the number of iterations: : "))
                    start = time.time()
                    mc = MonteCarlo(iterations)
                    mc.calculate()
                    end = time.time()
                    print(end-start)
                    break
                except ValueError:
                    print("Invalid input. Please input the number of iterations: : ")
        elif userInput == "4":
            break
        else:
            print("Invalid input. Select an option: ")
          
main()