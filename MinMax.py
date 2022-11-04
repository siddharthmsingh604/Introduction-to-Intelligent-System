import math

def fun_minmax(cd, node, maxt, scr, td):
    if(cd == td):
        return scr[node]
    if(maxt):
        return max(fun_minmax(cd+1, node*2, False, scr, td),fun_minmax(cd+1,node*2+1, False, scr, td))
    else:
        return min(fun_minmax(cd+1, node*2, True, scr, td),fun_minmax(cd+1,node*2+1, True, scr, td))

scr = []
x =int(input("Enter total number of leaf Node = "))
for i in range(x):
    y = int(input("Enter leaf value: "))
    scr.append(y)
    
td = math.log(len(scr), 2)
cd = int(input("Enter current depth value: "))
nodev = int(input("Enter node value: "))
maxt = True

print("The answer is: ", end=" ")
answer = fun_minmax(cd, nodev, maxt, scr, td)
print(answer) 











































































"""
Input:-
Enter total number of leaf Node = 16
Enter leaf value: 50
Enter leaf value: 70
Enter leaf value: 60
Enter leaf value: 90
Enter leaf value: 60
Enter leaf value: 70
Enter leaf value: 80
Enter leaf value: 90
Enter leaf value: 20
Enter leaf value: 30
Enter leaf value: 40
Enter leaf value: 23
Enter leaf value: 40
Enter leaf value: 30
Enter leaf value: 30
Enter leaf value: 30
Enter current depth value: 0
Enter node value: 0
The answer is:  60


ALGORITHM:
Pseudo-code for MinMax Algorithm:
function minimax(node, depth, maximizingPlayer) is
if depth ==0 or node is a terminal node then
return static evaluation of node
if MaximizingPlayer then // for Maximizer Player
maxEva= -infinity
for each child of node do
eva= minimax(child, depth-1, false)
maxEva= max(maxEva,eva) //gives Maximum of the values
return maxEva
else // for Minimizer player
minEva= +infinity
for each child of node do
eva= minimax(child, depth-1, true)
minEva= min(minEva, eva) //gives minimum of the values
return minEva

Create the entire game tree.
Evaluate the scores for the leaf nodes based on the evaluation function.
Backtrack from the leaf to the root nodes:
For Maximizer, choose the node with the maximum score.
For Minimizer, choose the node with the minimum score.
At the root node, choose the node with the maximum value and select the respective move.
ADVANTAGES: It provides an optimal move for the player assuming that opponent is also playing
optimally.
A thorough assessment of the search space is performed.
Decision making in AI is easily possible.
New and smart machines are developed with this algorithm.
DISADVANTAGES: The main drawback of the minimax algorithm is that it gets really slow for
complex games such as Chess, go, etc. This type of games has a huge branching factor, and the

player has lots of choices to decide. This limitation of the minimax algorithm can be improved from
alpha-beta pruning
Because of the huge branching factor, the process of reaching the goal is slower.
Evaluation and search of all possible nodes and branches degrades the performance and efficiency
of the engine.
Both the players have too many choices to decide from.
If there is a restriction of time and space, it is not possible to explore the entire tree.
Complete- Min-Max algorithm is Complete. It will definitely find a solution (if exist), in the finite
search tree.
Optimal- Min-Max algorithm is optimal if both opponents are playing optimally.
Time complexity- As it performs DFS for the game-tree, so the time complexity of Min-Max
algorithm is O(bm), where b is branching factor of the game-tree, and m is the maximum depth of
the tree.
Space Complexity- Space complexity of Mini-max algorithm is also similar to DFS which is O(bm).
APPLICATIONS:
Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find
the optimal move for a player, assuming that your opponent also plays optimally. It is widely used in
two player turn-based games such as Tic-Tac-Toe, Backgammon, Mancala, Chess, etc.
"""

