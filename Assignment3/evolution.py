import sys
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def FitnessScore(pop):
    fit = np.zeros((pop[:, 1].size, 1))

    for index, solution in enumerate(pop):
        for ia, a in enumerate(solution, start=1):
            for ib, b in enumerate(solution[ia:(len(solution))], start=ia + 1):
                if abs(a - b) == abs(ia - ib):
                    fit[index, 0] = fit[index, 0] + 1

    return fit;

def Crossover(parent1, parent2, size):
    def fillGene(f, p):
        for ia, a in enumerate(p):
            if a not in f:
                if a not in f:
                    for ib, b in enumerate(f):
                        if b == 0:
                            f[ib] = a
                            break
        return f

    fitness1 = np.zeros(len(parent1))
    fitness2 = np.zeros(len(parent2))

    c = random.randint(0, (len(parent1) - size))
    fitness1[c:c + size] = parent1[c:c + size]
    fitness2[c:c + size] = parent2[c:c + size]
    fitness1 = fillGene(fitness1, parent2)
    fitness2 = fillGene(fitness2, parent1)
    offsprings = np.vstack([fitness1, fitness2])
    return offsprings





def best_solution(pop, p_sol):
    sel_pool = np.random.permutation(pop[:, 1].size)[0:int(round(pop[:,1].size * p_sol))]
    #print( sel_pool)
    bestsolution = pop[sel_pool[0], :]
    #print('jj',bestsolution)
    for sol in sel_pool[1:len(sel_pool)]:
        if pop[sol, len(bestsolution) - 1] < bestsolution[len(bestsolution) - 1]:
            bestsolution = pop[sol, :]
    return bestsolution






def swapMutation(child, numberOfSwaps):
    for i in range(numberOfSwaps):
        swapGenesPairs = np.random.choice(len(child), 2, replace=False)
        a = child[swapGenesPairs[0]]
        b = child[swapGenesPairs[1]]
        child[swapGenesPairs[0]] = b
        child[swapGenesPairs[1]] = a

    return child



def plotCheckBoard(sol):
     def checkerboard(shape):
          return np.indices(shape).sum(axis=0) % 2

     sol = sol - 1
     size = len(sol)
     color = 0.5
     board = checkerboard((size, size)).astype('float64')
     for i in range(size):
          board[i, int(sol[i])] = color

     fig, ax = plt.subplots()
     ax.imshow(board, cmap=plt.cm.CMRmap, interpolation='nearest')
     plt.show()

npop = 15 # Number of solutions


size = 8 # size of board and queens
new_size= 2 # variables changed during order crossover
generation = 70 # Number of generations
p_sol = 2# Probability of best_solution
p_m = 1 # Probability of Mutation
numberOfSwaps = 2 # Number of swaps during mutation

# Fitness score calculation
pop = np.zeros((npop, size))
for i in range(npop):
    pop[i, :] = np.random.permutation(size) + 1

fit = FitnessScore(pop) #initial fitness
pop = np.hstack((pop, fit))
print("No ", " Initial Population", " ", " Fitness Score")
for i in range(npop):
    print(i, " ", pop[i, 0:8], " ", pop[i, 8:9])

print("Sorted by Fitness Score (Ascending Order)")
sorted_list = sorted(pop, key=lambda item: (item[8], item[7]))
print(*sorted_list, sep="\n")
meanFit = np.zeros(generation)






# Main
for gen in range(generation):
    parents = [best_solution(pop, p_sol), best_solution(pop,p_sol)]
    print("Parents: ")
    print(parents)

    offsprings = Crossover(parents[0][0:size], parents[1][0:size], new_size)
    print("Children: ")
    print(offsprings)

    for child in range(len(offsprings)):
        r_m = round(random.random(), 2)
        if r_m <= p_m:
            offsprings[child] = swapMutation(offsprings[child],numberOfSwaps)
    fitOff = FitnessScore(offsprings)

    offsprings = np.hstack((offsprings, fitOff))
    pop = np.vstack([pop, offsprings])
    pop = pop[pop[:, size].argsort()][0:npop, :]

    print("Crossover with Fitness: ")
    print(pop)
    print("Generation ", gen + 1, " Done")
    if (pop[8:9] == '0'):
        break
    else:
        continue
bestsolution = pop[np.argmin(pop[:, size]), :] #best solution
print(bestsolution[0:size])
print(f"Best Solution have: {bestsolution[size]} Conflict(s)")
plotCheckBoard(bestsolution[0:size])
























