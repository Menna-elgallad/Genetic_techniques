import numpy as np
import random


def fitness(l):
    ch = int(l,2)
    desired = 961.1
    error = desired - (ch**2)
    f = 1 / abs(error)
    if f>9:
        print ( "best chrmomsome reached = " , l)
        return
    return f


def evaluation(listt):
    fitness_l=[]
    for i in range(len(listt)):
       f =  fitness(listt[i])
       fitness_l.append(f)
    return fitness_l   

def selection(li , indicies):
    select=[]
    indix = indicies[:2]
    for x in indix:
        select.append(li[x])
    return select    

def uniform(list1 , list2 , u):
    off1 = []
    off2=[]
    for i in range(len(list1)):
        if u[i]==1 :
            off1.append(list1[i])
            off2.append(list2[i])
        else:
            off1.append(list2[i])
            off2.append(list1[i])
    return off1 , off2

def mutation(l):
    child = l
    sub = l[2:]
    k = random.uniform(0,1)
    if k < 0.2:
        sub.reverse()
        child = l[:2]+sub
    return child    

initial = []
chromosome = np.random.randint(0,32,4)
for x in chromosome:
    initial.append(format(x , "05b"))
print (chromosome)
print(initial)
generation_p = initial

for i in range ( 10):

    ff = evaluation(generation_p)
    print ( ff)

    indices = np.argsort(ff)[::-1]
    selected_parnets = selection(generation_p , indices) 
    print(selected_parnets)
    parent1 = selected_parnets[0]
    parent2 = selected_parnets[1]

    u = np.random.randint(0,2,5)
    print(u)

    off1 , off2 = uniform(parent1 , parent2 , u)
    print ( off1 , off2)

    child = mutation(off1)
    child2 = mutation(off2)

    generation = ["".join(child)]  + ["".join(child2)] +["".join(parent1)] +["".join(parent2)]
    generation_p = generation 
    print (generation)