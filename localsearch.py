import math
import random

"""

 The local search playground is a grid with size height x width. When the playground is created, a set of fixed spots defined by their coordinates (x, y) are placed in the grid
 these fixed spots represent real-world objects such as houses, schools, hospitals, pharmacies, police stations, etc.

 For example, the grid below has 5 rows, 9 columns, and four fixed spots (S) at locations {(0,2), (1,8), (3,0), (4, 3)}. Stars represent the grid locations that minimize
 the total distance to the fixed spots. In this example, the minimum total cost from stars to the fixed spots is 6.

  __S______
  __*____*S
  _________
  S*_______
  ___S_____

 Local search algorithms allow to find the optimal coordinates in the grid for a given number of locations, the coordinates (x, y) minimize or maximize the total distance
 from these locations to the fixed spots

 The local search playground may be used to solve local search problems such as finding the minimum distance from a set of public services (e.g. pharmacies, hospitals, etc.) to
 some fixed spots (e.g. houses, schools, etc.) in a neighborhood represented as a grid

 The class LocalSearchPlayground provides the following functions:

 - __available_positions(self) return all available cells in the grid
 - __calculate_cost(self, current_state) calculate the sum of distances from fixed spots to the current state
 - __find_neighbors(self, row, col) return available neighbors for coordinates (row, col)
 - __is_a_fixed_spot(self, row, col) return true if coordinates (row, col) are a spot and false otherwise
 - __random_state(self) return a random state
 - __temperature(self, i) the temperature function used by simulated annealing is a decreasing function T(t) = 1/t
 - hill_climbing(self, max_iterations=25, verbose=True)
 - hill_climbing_random_restart(self, max_iterations=20, verbose=True)
 - simulated_annealing(self, max_iterations=100, verbose=True)
 - show(self, title, solutions=[]) prints out the grid and the solution

 The class LocalSearchPlayground implements three local search algorithms: hill climbing, hill climbing with random restart, and simulated annealing

 - Hill climbing is a simple greedy algorithm that stops when it finds a local maximum by choosing what looks best locally
   The value of the current state is compared with its neighbor states. If any neighbor is better, the current state takes the value of the best neighbor
 - Hill climbing with random restart runs hill climbing multiple times and returns the best solution
 - Simulated annealing is a probabilistic method that approximates the global optimum for an optimization problem in a large search space

"""

class LocalSearchPlayground():
    def __init__(self, height, width, spots, solutions):
        self.__height = height
        self.__width = width
        self.__solutions = solutions
        self.__infinity = float('inf')

        # initialize the coordinates of the fixed spots with pairs (x, y) of the input list spots

        self.__spots = set()

        for spot in spots:
            self.__spots.add((spot[0], spot[1]))

    def __available_positions(self):
        # return all available cells in the grid

        positions = set()

        for row in range(self.__height):
            for col in range(self.__width):
                positions.add((row, col))

        # remove positions occupied by the fixed spots

        for spot in self.__spots:
            positions.remove(spot)

        return positions

    def __calculate_cost(self, current_state):
        # calculate the sum of distances from fixed spots to the current state

        cost = 0

        for spot in self.__spots:
            cost += min(
                abs(spot[0] - current[0]) + abs(spot[1] - current[1])
                for current in current_state
            )

        return cost

    def __find_neighbors(self, row, col):
        available_neighbors = []

        # calculate coordinates for neighbors

        neighbors = [ (row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1) ]

        # check if coordinates (r, c) are valid and it is an available neighbor

        for r, c in neighbors:
            if r >= 0 and r < self.__height and c >= 0 and c < self.__width and not (r, c) in self.__spots and not (r, c) in self.__current_state:
                available_neighbors.append((r, c))

        return available_neighbors

    def __is_a_fixed_spot(self, row, col):
        # return true if coordinates (row, col) are a spot and false otherwise

        return (row, col) in self.__spots

    def __random_state(self):
        # return a random state

        random_state = set()

        for i in range(self.__solutions):
            random_state.add(random.choice(list(self.__available_positions())))

        return random_state

    def hill_climbing(self, max_iterations=25, verbose=True):
        # code for hill climbing

        pass

    def hill_climbing_random_restart(self, max_iterations=25, verbose=True):
        # code for hill climbing with random restart

        pass

    def simulated_annealing(self, max_iterations=100, verbose=True):
        # code for simulated annealing

        pass

    def show(self, title, solutions=[]):
        print("\n" + title + "\n")

        for i in range(self.__height):
            for j in range(self.__width):
                if self.__is_a_fixed_spot(i, j):
                    print("S", end="")
                elif (i, j) in solutions:
                    print("*", end="")
                else:
                    print("_", end="")

            print(" ")

        if len(solutions) != 0:
            print("\nBest cost is", self.__calculate_cost(solutions), "with solutions", solutions, "\n")