#initial population 

import numpy as np

def fitness(parent):
    
    data = [4,-2,7,5,11,1]
    desired = 44.1
    output = 0
    for i in range(len(parent)):
        output += parent[i]*data[i]
    error = desired  -output
    f = 1 / abs(error)   
    return f  


def evaluating ( l1):
    fitness_f =[]
    for i in range (len (l1)):
        fit = fitness(l1[i])
        fitness_f.append(fit)
        if fit>=1:
            print ("best parent found with fitness = " , fit)
            print(l1[i])
            break
    return fitness_f    


def select(list):
    sub = indicies[:3]
    selected = []
    for x in sub :
        selected.append(list[x])
    return selected


def crossover (list1 , list2,k):
    off_s1 = np.append(list1[:k] , list2[k:])
    off_s2 = np.append(list2[:k] ,list1[k:])
    return off_s1 , off_s2

def randmutation(x):
    child=x
    i=np.random.randint(0,len( child))
    child[i]= child[i]/2
    return child



initial = []
for i in range(6) :

    chromosome = np.random.uniform(-10,10,6)
    initial.append(chromosome) 

generationpop = initial


for i in range ( 10):
    fitness_f = evaluating(generationpop)

    indicies = np.argsort(fitness_f)[::-1]

    selected = select(generationpop)    


    parent1 = selected[0]
    parent2 = selected[1]
    parent3 = selected[2]

    off1,off2 = crossover(parent1,parent2 , 3)
    off3 , off4 = crossover ( parent2 , parent3 , 3)
    print ( off1 , off2 , off3 , off4)


    child1 = randmutation(off1)
    child2 = randmutation(off2)
    child3 = randmutation(off3)
    child4 = randmutation(off4)

    new_generation = [child1]+[child2]+[child3]+[child4]+[parent1]+[parent2]
    generationpop = new_generation
    print ( "new _gene," , new_generation)