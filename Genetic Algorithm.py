import random

def score(parent1, parent2):
    # doing crossover
    for i in range(len(parent1)-1, len(parent1)-4, -1):
        parent1[i], parent2[i] = parent2[i], parent1[i]
    #doint mutation by randomly selecting the genes
    mutation_index = [random.randint(0, len(parent1)-1) for i in range(len(parent1)//2)]
    for i in mutation_index:
        if parent1[i] == '0':
            parent1[i] = '1'
        else:
            parent1[i] = '0'
        if parent2[i] == '0':
            parent2[i] = '1'
        else:
            parent2[i] = '0'

    score1 = parent1.count('1')
    score2 = parent2.count('1')
    #checking which child is better with more gene of type1
    if score1 > score2:
        return [''.join(parent1), score1]
    else:
        return [''.join(parent2), score2]

def genetic_algo():
    # Taking input as no. of parents
    n = int(input('Enter the number of parents: '))
    parents = []

    #taking parents genes as input 1 by 1
    for i in range(n):
        parents.append(list(input(f'Enter the parent{i+1}: ')))
    results = []

    #finding the score and storing it in results
    for i in range(len(parents)):
        for j in range(i+1, len(parents)):
            arr = [parents[i].copy(), parents[j].copy()]
            scores = score(parents[i], parents[j])
            results.append(scores + arr)

    # finding the best score among all combination of parents
    results.sort(key=lambda x: x[1], reverse=True)
    print(f'The best offspring among the parents is : {results[0][0]} and the parents are {"".join(results[0][2])} and {"".join(results[0][3])}')
    
genetic_algo()



















































"""
Output:
Enter the number of parents: 4
Enter the parent1: 110101
Enter the parent2: 011011
Enter the parent3: 100001
Enter the parent4: 010011

ALGORITHM:
Genetic Algorithm
begin
Create initial population;
while (Until Stopping Criteria)
for (Each Chromosome)
Calculate fitness value;
Selection (Survival of strong
individuals);
Crossover (Here, new generation
produced);
if (There are same chromosomes)
Mutation (Changing some genes for
new and different individuals);
end
end
Generate new population;
end
end

ADVANTAGES:
1. Genetic algorithm is good for noisy environments
2. Genetic algorithms support multi objective optimization
DISADVANTAGES:
1. Genetic algorithms are computationally expensive
2. The "better" solution is only in comparison to other solutions. As a result, the stop
criterion is not clear in every problem.

Time: & Space complexity:
Given the usual choices (point mutation, one point crossover, roulette wheel selection) a Genetic
Algorithms complexity is O(g(nm + nm + n)) with g the number of generations, n the population size
and m the size of the individuals. Therefore the complexity is on the order of O(gnm)).
APPLICATIONS:
1. Genetic algorithms are adaptive methods which may be used to solve search and
optimization problems
2. It is also applied in other fields such as economics, multimodal optimization, aircraft design,
and DNA analysis.
3. Vehicle routing problem
4. Air flight scheduling problem
"""