
import random
import numpy as np

parent1 = '1001101000'
parent2 = '1001011001'



def onepoint (list1 , list2,k):
    off_s1 = np.append(list1[:k] , list2[k:])
    off_s2 = np.append(list2[:k] ,list1[k:])
    return off_s1 , off_s2

off1 , off2 = onepoint(parent1 , parent2, 5)
print ("single point crossover",off1 , off2 )

def twopoint (list1 , list2 , p1,p2):
    substring1 = list1[p1:p2]
    substring2 = list2[p1:p2]
    off_s1 = list1[:p1] +substring2+ list1[p2:]
    off_s2 = list2[:p1] +substring1+ list2[p2:]
    return off_s1 , off_s2 

off1 , off2 = twopoint(parent1 , parent2, 3 , 7)
print ("two point crossover" ,off1 , off2 )

def multipoint (a , b ,x ):
    for i in x :
        off1 , off2 = onepoint(a , b,i)
        a = off1 
        b= off2
    return off1 , off2

x = [2,5]
off1 , off2 = multipoint ( parent1 , parent2 ,x )    
print("multipoint crossover" , off1 , off2)    

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


u = np.random.randint(0,2,10) 
off1 , off2 = uniform(parent1 , parent2 , u)  
print("uniform crossover" , off1 , off2)

def order(list1 , list2 , p1 , p2):
    off1 = []
    off2=[]
    sub1 = list1[p1:p2]
    sub2 = list2[p1:p2]
    for x in list2:
        if x not in sub1:
            off1.append(x)
    for x in list1 : 
        if x not in sub2:
            off2.append(x)
    off1[p1:p1] = sub1
    off2[p1:p1]  =sub2      
    return off1 , off2

p1 = [1,4,2,7,8,10,9,3,5,6]
p2 = [10,7,9,6,4,3,1,2,5,8]
off1 , off2 = order(p1 , p2 , 3 , 6)
print ("order crossover" ,  off1 , off2)      

def pmx (l1 , l2 , p1 , p2):
    sub1 = l1[p1:p2]
    sub2 = l2[p1:p2]
    off1 = []
    off2 = []
    dict={}
    for i in range(len(sub1)):
        dict[sub1[i]] = sub2[i]
        dict[sub2[i]] = sub1[i]
    for x in l1 :
        if x in dict:
            off1.append(dict[x])
        else :
            off1.append(x)
    for x in l2 :
        if x in dict:
            off2.append(dict[x])
        else :
            off2.append(x)          
    return off1 , off2        

p1 = [1,4,2,7,8,10,9,3,5,6]
p2 = [10,7,9,6,4,3,1,2,5,8]
off1 , off2 = pmx(p1 , p2 , 3 , 6)
print ("pmx cross over" ,  off1 , off2)     


def shuffle_cross(l1,l2,k):
    random.shuffle(l1)
    random.shuffle(l2)
    off1 = np.append(l1[:k] , l2[k:])
    off2 = np.append(l2[:k] , l1[k:])
    return off1 , off2

off1 , off2 = shuffle_cross(parent1 , parent2, 3 )
print ("shuffle cross over" ,  off1 , off2)     
