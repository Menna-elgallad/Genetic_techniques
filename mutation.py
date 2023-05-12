import numpy as np
import random
#reverse
def reversedmutation(l , pos):
    child = l
    sub = l[pos:]
    p = random.uniform(0,1)
    if p < 0.3 :
        sub.reverse()
        child = l[:pos]+sub
    return child        

A=[1,2,3,4,5,6,7,8]           
print(reversedmutation(A,4))

#flip
def flipmutation(x):
    child =x
    for i in range (len(child)):
        k=np.random.uniform(0,1)
        if k<0.5:
            if child[i]==1:
                child[i]=0
            else:
                child[i]=1
    print(x)

child=[0,1,0,1,0,1]
print(flipmutation(child))

#random mutation
def randmutation(x):
    child=x
    i=random.randint(0,len( child))
    print("i" , i)
    child[i]= child[i]/2
    return child

x=[1,2,3,4,5,6]
print(randmutation(x))

def interchanging(l1 ):
    child = l1
    pos1 = random.randint(0,len(l1)-1)
    pos2 = random.randint(0,len(l1)-1)
    child[pos1] , child[pos2] = child[pos2] , child[pos1]
    return child    

x=[1,2,3,4,5,6]
print(interchanging(x))

