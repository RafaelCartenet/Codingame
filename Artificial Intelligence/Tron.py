import math
import random
import statistics
import sys

# ------------Paramètres Algorithme Génétique--------------------------------------------------------------------------#

NBTOUR = 5
NBGENOME = 10
NBGEN = 10
MUTRATE = 0.05
CROSSRATE = 0.55

# ------------Fonctions du problème------------------------------------------------------------------------------------#

OUTPUTS = ["RIGHT","UP","LEFT","DOWN"]

T = [[0 for _ in range(30)] for _ in range(20)]

def is_ok(output,lastoutput):
    if (lastoutput==0)&(output==2):return False
    if (lastoutput==2)&(output==0):return False
    if (lastoutput==1)&(output==3):return False
    if (lastoutput==3)&(output==1):return False
    else: return True


def is_in_T(X,Y):
    return (X>=0)&(X<=19)&(Y>=0)&(Y<=29)

def nextXY(X,Y,d):
    if d == 0:
        X += 1
    elif d == 1:
        Y -= 1
    elif d == 2:
        X -=1
    else :
        Y += 1
    return X,Y

def randomGen():
    gen = [random.randint(0,3) for _ in range(NBTOUR)]
    return gen

def fitness(genome):

    fit = 100
    lastOP = out

    print("genome"+str(genome),file=sys.stderr)
    for di in genome:
        print("lastoutput : "+str(lastOP)+" prochain "+str(di),file=sys.stderr)
        if not is_ok(di,lastOP):
            fit = 0
            print("false",file=sys.stderr)
            break
        else:
            lastOP = di
    print(fit,file=sys.stderr)
    return fit

def output(genome):
    return OUTPUTS[genome[0]]

# ------------Fonctions Génétiques-------------------------------------------------------------------------------------#

# Création d'une population initiale aléatoire
def randomPop():
    population = [randomGen() for _ in range(NBGENOME)]
    return population

# Renvoie le meilleur génome d'une population (meilleur fitness)
def bestgenome(population):
    temp = fitnessPop(population)
    return population[temp.index(max(temp))]

# Renvoie la meilleure fintness d'une population donnée
def bestfitness(population):
    temp = fitnessPop(population)
    return max(temp)

# Fonction d'évaluation de l'efficacité d'un génome
def fitnessGA(genome):
    return fitness(genome)

# Calcul de la fitness d'une population
def fitnessPop(population):
    temp = list(map(fitnessGA, population))
    return temp

# Crossover des génomes pour tenter de garder les allèles performants
def crossover(population):
    temp = []
    for k in range(len(population) // 2):
        p1, p2 = list(population[2 * k]), list(population[2 * k + 1])
        if (random.randrange(0, 100) / 100) <= CROSSRATE:
            pas = random.randint(0,NBTOUR)
            temp.append(p1[:pas]+p2[pas:])
            temp.append(p2[:pas]+p1[pas:])
        else :
            temp.append(p1)
            temp.append(p2)
    return temp

# Selection d'une partie de la population en fonction des performances de chaque génome de cette population
# RWS
def selection(population,neg):
    temp = []

    fitness = fitnessPop(population)
    #print(*fitness,sep='\n')
    if neg == True:
        m = min(fitness)
        fitness = [- m + i for i in fitness]
    #print(*fitness,sep='\n')
    sumfit = sum(fitness)
    for _ in range(len(population)):
        G = random.randrange(0, int(sumfit))
        res = 0
        i = 0
        while (res < G):
            res += fitness[i]
            i += 1
        #print(i-1)
        temp.append(population[i-1])

    return temp

# Mutation d'une population (mutation de chaque génome)
def mutatePop(population):
    return [mutate(i) for i in population]

# Mutation d'un genome
def mutate(genome):
    temp = genome
    taillegen = len(genome)
    for i in range(taillegen):
        if (random.randrange(0, 100) / 100) <= MUTRATE:
            j = i
            while j == i:
                j = random.randint(0, taillegen - 1)
            temp[i], temp[j] = temp[j], temp[i]
    return temp

# ------------Main-----------------------------------------------------------------------------------------------------#

out=""

while True:
    # n: total number of players (2 to 4).
    # p: your player number (0 to 3).
    n, p = [int(i) for i in input().split()]
    for i in range(n):
        # x0: starting X coordinate of lightcycle (or -1)
        # y0: starting Y coordinate of lightcycle (or -1)
        # x1: starting X coordinate of lightcycle (can be the same as X0 if you play before this player)
        # y1: starting Y coordinate of lightcycle (can be the same as Y0 if you play before this player)
        x0, y0, x1, y1 = [int(j) for j in input().split()]
        if p == i:
            X, Y = x1, y1

    print(X,file=sys.stderr)
    print(Y,file=sys.stderr)

    pop = randomPop()
    bestfit = fitnessPop(pop)[0]
    bestglobal = bestgenome(pop)

    for i in range(NBGEN):
        #pop = selection(pop, False)
        pop = crossover(pop)
        #pop = mutatePop(pop)
        bestglobal = (bestglobal,bestgenome(pop))[bestfit<fitnessGA(bestgenome(pop))]
        bestfit = fitnessGA(bestglobal)

    print(bestfit,file=sys.stderr)
    out=output(bestglobal)
    print(out)
    out=OUTPUTS.index(out)
