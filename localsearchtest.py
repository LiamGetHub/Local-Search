import sys
from localsearch import *

# Usage: python "localsearch test.py" 2 1

if __name__=="__main__":

    if len(sys.argv) == 3:
        total_solutions = int(sys.argv[1])
        show_trace = False if int(sys.argv[2]) == 0 else True
    else:
        total_solutions = 2
        show_trace = True

    #
    # 5x9 grid with 4 fixed spots and max_solutions with minimum cost
    #

    search = LocalSearchPlayground(height=5, width=9, spots=[(0,2), (1,8), (3,0), (4, 3)], solutions=total_solutions)

    #search.show("Local search \n")

    #print("Testing the helper functions...")

    #search.test_helper_functions(verbose = True)


    #hill climbing
    print("\nHill climbing with random restart")

    solution = search.hill_climbing(verbose=show_trace)

    search.show("Final state", solution)