colors = ['Red','Blue','Green']
states = ['Nagpur','Thane','Pune','Mumbai']
neighbors = {}
neighbors['Nagpur'] = ['Thane','Pune']
neighbors['Thane'] = ['Nagpur','Pune','Mumbai']
neighbors['Pune'] = ['Nagpur','Thane','Mumbai']
neighbors['Mumbai'] = ['Thane','Pune']
colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state):
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
    print(colors_of_states)

main()








































































"""
Output:
{'Nagpur': 'Red', 'Thane': 'Blue', 'Pune': 'Green', 'Mumbai': 'Red'}

ALGORITHM:
1) Open all objects that must be assigned values in a complete solution.
2) Repeat until all objects assigned valid values.
3) Select an object and strengthen as much as possible. The set of constraints that apply to object.
4) If set of constraints is different from previous set then open all objects that share any of these
constraints. Remove selected objects.
5) If union of constraints discovered above defines a solution, return solution.
6) If union of constraints discovered above defines a contradiction, return failure.
7) Make a guess in order to proceed. Repeat until a solution is found.
8) Select an object with a number assigned value and try strengthen its constraints.
ADVANTAGES: Constraint satisfaction is a technique where a problem is solved when its values
satisfy certain constraints or rules of the problem. Such type of technique leads to a deeper
understanding of the problem structure as well as its complexity.
DISADVANTAGES:
• CSPs include representational limits in terms of dealing with variables and variable values
instead of component types and corresponding components (instances)
• static CSPs are limited with regard to the description of configuration problems in which the
size and structure of configurations cannot be estimated beforehand.
Time: & Space complexity:
• Time complexity: O(9^(n*n))
For every unassigned index, there are 9 possible options so the time complexity is O(9^(n*n)).
• Space Complexity: O(n*n).
To store the output array a matrix is needed.

APPLICATIONS:
• Constraint Graph
• Backtracking
• Graph Coloring
• Sudoku
• Assignment problems
• Timetabling problems
• Transportation scheduling
• Factory scheduling
• Hardware configuration
• Floor planning
"""