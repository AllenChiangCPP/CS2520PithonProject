Project Title: Estimating Pi using Three Different Methods
Team Members: Allen Chiang, Johnny Truong, Nathan Wang


Overview
This project uses three different methods to estimate the value of pi: Archimedes' Approach, Accumulator Approximations, and the Monte Carlo method. Each method is implemented in a separate Python class.


Archimedes' Approach
The Archimedes class uses a geometric approach to estimate the value of pi. The class generates a sequence of inscribed and circumscribed polygons with increasing number of sides, and calculates the perimeter of each polygon. The class then uses the perimeters to estimate the value of pi.


To run the Archimedes class, create an instance of the class and specify the number of iterations to run. For example:


archimedes = Archimedes(iterations=20)
archimedes.calculate()


Accumulator Approximations
The Ramanujan formula is used to compute the value of pi in this program. It is defined by the following equation:


pi = 1 / sum( (2k)! / (k!)^2 * (2^10k + 62k - 748) / 2^10k * (5^k) )
where k = 0, 1, 2, ...


The program first defines a function factorial that computes the factorial of a given number using recursion. It then defines another function pi_formula that takes the number of terms to use in the Ramanujan formula as an argument and calculates the estimated value of pi using the formula.


The program prompts the user to enter the number of terms to use in the formula and then calls the pi_formula function to calculate the estimated value of pi. It then uses the turtle module to draw a visual representation of the estimation.


The program then asks the user if they want to continue. If the user enters 'y', the program will prompt them again to enter the number of terms to use in the formula and repeat the process. If the user enters 'n', the program will exit.




Monte Carlo Method
The MonteCarlo class uses the Monte Carlo method to estimate the value of pi. The class randomly generates points within a square, and counts how many points fall inside a quarter of a circle inscribed in the square. The ratio of the number of points inside the quarter circle to the total number of points generated is then used to estimate the value of pi.


To run the MonteCarlo class, create an instance of the class and specify the number of iterations. For example:


monteCarlo = MonteCarlo(iterations=100000)
monteCarlo.calculate()


Dependencies
This project uses the following libraries:


turtle
random
time
numpy
math
matplotlib


Results
Each class prints out the estimated value of pi, the time it took to run, and any other relevant information. The results can be compared across the different methods to see how accurate and efficient each method is.


Note
          -Code and run tests were done on Visual Studio Code, Replit, and IntelliJ. Running code and compiling code was done using the terminals in Visual Studio Code, Replit, and IntelliJ.


Usage
          -Running
                    Top right button to run python file
                    (note, may need to download matplotlib and numpy on Visual Studio Code)