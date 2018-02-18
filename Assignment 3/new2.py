import numpy as np
import random as rd
from heapq import nlargest

#Question 1
def arrayfunc(n):
 a = []
 for i in range(n):
    a.append([])
    for j in range(n):
        a[i].append(i+j)
 print(a)
 return
arrayfunc(2)

#Question 2
ll= list(range(0,20))
list_Odd_Numbers = list(filter(lambda varX: varX % 2 == 1,ll))
np_odd=np.array(list_Odd_Numbers)
lo= np.reshape(np_odd, (2,5))
le= np.log(lo)
print(le)

#Question 3
def newarrfunc(n):
 a = np.random.random_integers(10, size=(n,n))
 print(a)
 np_ll=np.array(np.mean(a, axis=1))
 lo= np.reshape(np_ll, (n,1))
 print(lo)
 print(a-lo)
 return
newarrfunc(2)

#Question 4
def newarrfunc1(n,value):
 A = np.random.random_integers(10, size=(n,n))
 print(A)
 X = np.abs(A-value)
 idx = np.where(X == X.min())
 print(A[idx[0], idx[1]])
 return
newarrfunc1(3,3)

#Question 5
def newarray(n):
 np_l1=np.array(np.random.randint(10, size=n))
 np_l2=np.array(np.random.randint(10, size=n))
 print(np.array_equal(np_l1,np_l2))
 return
newarray(4)

#Question 6
def narray(k,n):
 np_array=np.array(np.random.randint(10, size=n))
 print(np_array)
 print(nlargest(k,np_array))
 return
narray(3,10)