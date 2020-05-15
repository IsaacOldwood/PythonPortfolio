import numpy as np
import matplotlib.pyplot as plt

#Create data
x=np.array([0.,0.5,1.])
y_exact=np.array([0.,1.,1.])

#Intiliase W and b
W=0.5
b=0.5

#Set other constants
N=3
eta=0.75
MaxIter=16

#Initialise approximation
F=W * x + b

#Functions
def cost():
    return (1/N) * np.sum( 0.5* (y_exact - F)**2 )
#Partial derivates of cost
def cost_W():
    return (1/N) * np.sum( x*(W*x- y_exact +b) )
def cost_b():
    return (1/N) * np.sum( (W*x - y_exact + b) )

#Cost_vec
cost_vec=np.empty(MaxIter)
j=np.arange(0,MaxIter,1)
w_vec=np.empty(MaxIter)
b_vec=np.empty(MaxIter)

#Peform gradient descent
for i in range(0,MaxIter):
    newcost=cost()
    cost_vec[i]=newcost
    w_vec[i]=W
    b_vec[i]=b
    #Forward pass
    F=W*x+b
    #Alter weights and biases
    W= W - eta * cost_W()
    b= b - eta * cost_b()
    #Calculate newcost
    

    #print(newcost)

plt.plot(j,cost_vec)
plt.title('Cost')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.show()

#for i in range(0,MaxIter):
#    print(f"""{w_vec[i]} & {b_vec[i]} & {cost_vec[i]} \\""")