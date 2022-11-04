import numpy as np

def find_neighbours(state, landscape):
    neighbours = []
    dim = landscape.shape

    # left neighbour
    if state[0] != 0:
        neighbours.append((state[0] - 1, state[1]))

    # right neighbour
    if state[0] != dim[0] - 1:
        neighbours.append((state[0] + 1, state[1]))

    # top neighbour
    if state[1] != 0:
        neighbours.append((state[0], state[1] - 1))

    # bottom neighbour
    if state[1] != dim[1] - 1:
        neighbours.append((state[0], state[1] + 1))

    # top left
    if state[0] != 0 and state[1] != 0:
        neighbours.append((state[0] - 1, state[1] - 1))

    # bottom left
    if state[0] != 0 and state[1] != dim[1] - 1:
        neighbours.append((state[0] - 1, state[1] + 1))

    # top right
    if state[0] != dim[0] - 1 and state[1] != 0:
        neighbours.append((state[0] + 1, state[1] - 1))

    # bottom right
    if state[0] != dim[0] - 1 and state[1] != dim[1] - 1:
        neighbours.append((state[0] + 1, state[1] + 1))
        return neighbours

# Current optimization objective: local/global maximum
def hill_climb(curr_state, landscape):
    neighbours = find_neighbours(curr_state, landscape)
    bool
    ascended = False
    next_state = curr_state
    for neighbour in neighbours: #Find the neighbour with the greatest value
        if landscape[neighbour[0]][neighbour[1]] > landscape[next_state[0]][next_state[1]]:
            next_state = neighbour
            ascended = True
    return ascended, next_state

def __main__():
    landscape = np.random.randint(1, high=50, size=(10, 10))
    print(landscape)
    start_state = (3, 6) # matrix index coordinates
    current_state = start_state
    count = 1
    ascending = True
    while ascending:
        print("\nStep #", count)
        print("Current state coordinates: ", current_state)
        print("Current state value: ",landscape[current_state[0]][current_state[1]])
        count += 1
        ascending, current_state = hill_climb(current_state, landscape)
    print("\nStep #", count)
    print("Optimization objective reached.")
    print("Final state coordinates: ", current_state)
    print("Final state value: ",
landscape[current_state[0]][current_state[1]])

__main__()




























"""
Output:
Will be Random Just Run

Hill climbing Algorithm:
ALGORITHM: Algorithm for Simple Hill Climbing:
Step 1: Evaluate the initial state, if it is goal state then return success and Stop.
Step 2: Loop Until a solution is found or there is no new operator left to apply.
Step 3: Select and apply an operator to the current state.
Step 4: Check new state:
If it is goal state, then return success and quit.
Else if it is better than the current state then assign new state as a current state.
Else if not better than the current state, then return to step2.
Step 5: Exit.
ADVANTAGES:
• It can be used in conversions and discrete domains.
• It requires fewer conditions than other search techniques.
• Helpful in solving pure optimization problems, where the focus is on finding the best state.
DISADVANTAGES:
• Local Maxima
• Plateau
• Ridge & Alleys
• It is not an efficient searching method.
• Not suitable for problems where the value of heuristic function drops suddenly.

• It is a local method, where the focus is on getting the immediate solution after
considering the current state, rather than exploring all possible outcomes.
Time: & Space complexity:
Hill climbing is neither complete nor optimal, has a time complexity of O(∞) but a space complexity
of O(b).
APPLICATIONS:
• Marketing
• Robotics
• Travelling Salesman Problem
• Job Scheduling
"""