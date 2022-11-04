graph={
    'S':['A','B'],
    'A':['C','D'],
    'B':['I','J'],
    'C':['E','F'],
    'D':['G'],
    'I':['H'],
    'J':[]
}

def dls(start,goal,path,level,maxLimit):
    print('\nCurrent level -->',level)
    print('Goal node testing',start)
    path.append(start)
    if start==goal:
        print('Test successfull goal found')
        return path
    print('Goal node test failed')
    if level==maxLimit:
        return False
    print('Expanding current node:',start)
    for child in graph[start]:
        if dls(child, goal, path, level+1, maxLimit):
            return path
    return False

start='S'
goal=input('Enter goal:')
maxLimit=int(input("Enter max limit:"))
print()
path=list()
res=dls(start, goal, path, 0, maxLimit)
if(res):
    print('Path exists')
    print('Path',path)
else:
    print('Path doesnt exist')





























































"""
Output:
Enter goal:D
Enter max limit:3


Current level --> 0
Goal node testing S
Goal node test failed
Expanding current node: S

Current level --> 1
Goal node testing A
Goal node test failed
Expanding current node: A

Current level --> 2
Goal node testing C
Goal node test failed
Expanding current node: C

Current level --> 3
Goal node testing E
Goal node test failed

Current level --> 3
Goal node testing F
Goal node test failed

Current level --> 2
Goal node testing D
Test successfull goal found
Path exists
Path ['S', 'A', 'C', 'E', 'F', 'D']

ALGORITHM:
1. We start with finding and fixing a start node.
2. Then we search along with the depth using the DFS algorithm.
3. Then we keep checking if the current node is the goal node or not
If the answer is no: then we do nothing.
If the answer is yes: then we return.
4. Now we will check whether the current node is lying under the depth limit specified earlier
or not.
If the answer is not : then we do nothing.
If the answer is yes: we will explore the node further and save all of its successors into a
stack.
5. Now we call the function of DLS iteratively or recursively for all the nodes of the stack and go
back to step 2.
Thus we have successfully explored all the nodes in the given depth limit and found the goal
node if it exists within a specified depth limit.
ADVANTAGES: It takes lesser memory when compared to other search techniques.
DISADVANTAGES: DLS may not offer an optimal solution if the problem has more than one solution.
DLS also encounters incompleteness.
Optimality: No
If a solution found is best (lowest path cost) among all the solutions identified, then that solution is
said to be an optimal one.
Completeness: No
A search algorithm is said to be complete when it gives a solution or returns any solution for a given
random input.
Time: O(b^l) & Space complexity: O(bl)
APPLICATIONS: 1. Solving Puzzles with only one solution
2. Toplogical sorting.
"""