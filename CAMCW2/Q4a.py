import numpy as np
import matplotlib.pyplot as plt

#Create data
x=np.array([0.,0.5,1.])
y_exact=np.array([0.,1.,0.])

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
def cost_W():
    return (1/N) * np.sum( x*(W*x- y_exact +b) )
def cost_b():
    return (1/N) * np.sum( W*x - y_exact + b )

#Cost_vec
cost_vec=np.empty(MaxIter)
j=np.arange(0,MaxIter,1)

#Peform gradient descent
for i in range(0,MaxIter):
    #Forward pass
    F=W*x+b
    #Calculate partial derivates
    delta=W * (F-y_exact)
    #Alter weights and biases
    W= W - eta * cost_W()
    b= b - eta * cost_b()
    #Calculate newcost
    newcost=cost()
    cost_vec[i]=newcost

    #print(newcost)

plt.plot(j,cost_vec)
plt.title('Cost')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.show()