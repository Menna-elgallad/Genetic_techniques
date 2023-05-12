import random 
import numpy as np 
import sys


def fitness ( l):
    desired_output = 25.1
    x = int(l[0])
    y = int(l[1])
    add =x+y
    if add!=7:
        return 1/sys.maxsize
    else : 
        output = (x**2)+(y**2)
        return 1/(abs(desired_output-output))

def evaluation(l):
    fitness_l=[]
    for i in range(len(l)):
        fit = fitness(l[i])
        fitness_l.append(fit)
        if fit>=1:
            print ( "best cromosome reached = " , l[i])
            print ("fitness = ," , fit)
            return 
    return fitness_l

def crossover(l1,l2):
    off1 = [[l1[0]] +[l2[1]]]
    off2 = [[l1[1]]+[l2[0]]]
    return off1,off2

def mutation(l):
    child = l
    k = random.uniform(0,1)
    if k < 0.3 :
        i = np.random.randint(0,len(child))
        child[0][i] = child[0][i] / 2
    return child

def selection(l , indx):
    selected_parent=[]
    ind = indx[:3]
    for x in ind:
        selected_parent.append(l[x])
    return selected_parent


inital = []
for i in range(5):
    chromosome = np.random.uniform(0,20,2)
    inital.append(chromosome)
g_pop = inital
print("initial pop = " , inital)

for i in range(50):
    ff = evaluation (g_pop)
    print(ff)
    indx = np.argsort(ff)[::-1]
    print(indx)

    selectionP = selection(g_pop , indx)
    print("selected parnts =", selectionP)

    p1 = selectionP[0]
    p2 = selectionP[1]
    p3 = selectionP[2]

    off1 , off2 = crossover(p1 , p2)
    off3 , off4 = crossover(p2 , p3)
    print("offsprings done by crossover",off1 , off2 , off3 , off4)


    child1 = mutation(off1)
    child2 = mutation(off2)
    child3 = mutation(off3)
    child4 = mutation(off4)
    print("children after mutation" , child1 , child2 , child3 , child4 )

    new_generation = child1+child2+child3+child4+[p1]
    g_pop= new_generation
    print ( "new _gene," , new_generation)