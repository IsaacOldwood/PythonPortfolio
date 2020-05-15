import numpy as np
import matplotlib.pyplot as plt
import random

#Create data
x=np.array([0.,0.5,1.])
y_exact=np.array([0.,1.,1.])

#Intiliase W and b
W=0.5
b=0.5

#Set other constants
N=3
eta=0.75
MaxIter=64

#Initialise approximation
F=W * x + b

#Functions
def cost():
    return (1/N) * np.sum( 0.5* (y_exact - F)**2 )
#Partial derivates of cost
def cost_W(k):
    return (1/N) * np.sum( x[k]*(W*x[k]- y_exact[k] +b) )
def cost_b(k):
    return (1/N) * np.sum( W*x[k] - y_exact[k] + b )

#Cost_vec
cost_vec=np.empty(MaxIter)
j=np.arange(0,MaxIter,1)

#Peform stochastic gradient descent
for i in range(0,MaxIter):
    #Pick random index
    k=random.randint(0, (N-1))
    #Forward pass
    F=W*x+b
    #Alter weights and biases
    W= W - eta * cost_W(k)
    b= b - eta * cost_b(k)
    #Calculate newcost
    newcost=cost()
    cost_vec[i]=newcost

    #print(newcost)

plt.plot(j,cost_vec)
plt.title('Cost')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.show()

print(F)
print(W)
print(b)