# Initial values of Alpha and Beta
MAX, MIN = 1000, -1000
# Returns optimal value for current player
#(Initially called for root and maximizer)
def minimax(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    # Terminating condition. i.e
    # leaf node is reached
    if depth == 3:
        return values[nodeIndex]
    if maximizingPlayer:
        best = MIN
        # Recur for left and right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i,False, values, alpha,beta)
            best = max(best, val)
            alpha = max(alpha, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best
    else:
        best = MAX
        # Recur for left and
        # right children
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i,True, values, alpha,beta)
            best = min(best, val)
            beta = min(beta, best)
            # Alpha Beta Pruning
            if beta <= alpha:
                break
        return best


if __name__ == "__main__":
    values = [4, 2, 6, 19, 1, -2, 3, -1]
    print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))






























































"""
Output:
The optimal value is : 4

ALGORITHM:
1. Start DFS traversal from the root of game tree.
2. Set initial values of alpha and beta as follows:
A] alpha = INT_MIN(-INFINITY)
B] beta = INT_MAX(+INFINITY)

3. Traverse tree in DFS fashion where maximizer player tries to get the highest score possible while
the minimizer player tries to get the lowest score possible.
4. While traversing update the alpha and beta values accordingly.
ADVANTAGES:
Decreases number of nodes that are evaluated by minimax algorithm.
Limits the search time to more promising sub-trees, which enables a deeper search.
Reduces computation and searching during the minimax algorithm.
Prevents the use of additional computational time, making the process more responsive and faster.
DISADVANTAGES:
It does not solve all the problems associated with the original minimax algorithm.
Requires a set depth limit, as in most cases, it is not feasible to search the entire game tree.

Though designed to calculate the good move, it also calculates the values of all the legal moves.
Time: & Space complexity:
O(b^(d/2)) correspond to the best case time complexity of alpha-beta pruning.
branching factor of b, and a search depth of d
Space complexity: O(BDm) [Branching factor is B
The maximum depth of the tree is Dm]
APPLICATIONS:

Alpha Beta Pruning is an adversarial search algorithm used commonly for machine playing of two-
player games (Tic-tac-toe, Chess, Connect 4, etc.).
"""