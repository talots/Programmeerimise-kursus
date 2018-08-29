# Imports math module, math is needed to use square root
import math


# Class for quadratic equations
class Quadratic:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        # x1 is def get_x1() and x2 is def get_x2() answer
        self.x1 = self.get_x1()
        self.x2 = self.get_x2()

    def get_x1(self):
        # Tries to find x1
        try:
            radican = (self.b ** 2) - (4 * self.a * self.c)
            x1 = (-1 * self.b - math.sqrt(radican)) / (2 * self.a)
            return x1
        # If there is a value error then it returns 'x1 lahend puudub'
        except ValueError:
            return "Lahend puudub"

    def get_x2(self):
        # Tries to find x2
        try:
            radican = (self.b ** 2) - (4 * self.a * self.c)
            x2 = (-1 * self.b + math.sqrt(radican)) / (2 * self.a)
            return x2
        # If there is a value error then it returns 'x2 lahend puudub'
        except ValueError:
            return 'Lahend puudub'


# Starts when this is the main script that runs
if __name__ == '__main__':
    # Gets a, b and c values
    while True:
        try:
            a_number = float(input('Enter a value: '))
            b_number = float(input('Enter b value: '))
            c_number = float(input('Enter c value: '))
            solve_equation = Quadratic(a_number, b_number, c_number)
	# When user inputs anything besides a number, then the program asks again for a number
        except ValueError:
            print('Please enter a number.')
            continue
        break
    # Tries to get x1 and x2 answers
    try:
        give_x1 = solve_equation.x1
        give_x2 = solve_equation.x2
        print('x1 =', give_x1)
        print('x2 =', give_x2)
    # If there was an error, then it gives out that x1 and x2 couldn't be solved
    except TypeError:
        print(solve_equation.x1)
        print(solve_equation.x2)

