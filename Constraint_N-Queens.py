# Taking number of queens as input from user
N = int(input("Enter the number of queens: "))
# here we create a chessboard
# NxN matrix with all elements set to 0
board = [[0]*N for _ in range(N)]

def attack(i, j):
    #checking vertically and horizontally if there are any queen placed
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonally if there are any queen placed
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False

def N_queens(n):
    if n==0:
        return True
    # here we are checking whether we can place queen at ith row and jth column
    for i in range(0,N):
        for j in range(0,N):
            if (not(attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                if N_queens(n-1)==True:
                    return True
                board[i][j] = 0
    return False

N_queens(N)
for i in board:
    print(i)
































































"""
Output:
Enter the number of queens: 8
[1, 0, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 0, 1]
[0, 0, 0, 0, 0, 1, 0, 0]
[0, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 1, 0]
[0, 1, 0, 0, 0, 0, 0, 0]
[0, 0, 0, 1, 0, 0, 0, 0]

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