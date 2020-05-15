#All credit to Catherine F. Higham Desmond J. Higham  in   Deep Learning: An Introduction for Applied Mathematicians
import numpy as np
import matplotlib.pyplot as plt
import random

#Activation function
def activate(x,W,b):
    return 1/(1+np.exp((-1)*(W@x+b)))

#Uses backpropogation to train a network. This code is a transcription of the matlab code by Catherine F. Higham Desmond J. Higham
#Data
x1 = np.array([0.1,0.3,0.1,0.6,0.4,0.6,0.5,0.9,0.4,0.7])
x2 = np.array([0.1,0.4,0.5,0.9,0.2,0.3,0.6,0.2,0.4,0.6])
y = np.array([1.,1.,1.,1.,1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.,1.,1.,1.,1.,1.])
y=np.reshape(y,(2,10))

#Initialise weights and biases
np.random.seed(5000)
W2 = 0.5*np.random.rand(2,2)
W3 = 0.5*np.random.rand(3,2)
W4 = 0.5*np.random.rand(2,3)
b2 = 0.5*np.random.rand(2,1)
b3 = 0.5*np.random.rand(3,1)
b4 = 0.5*np.random.rand(2,1)

#Forward and back propogate
eta=0.05 #Learning rate
Niter=int(1e6) #Iterations
savecost=np.empty(Niter)

#Cost fucntion
def cost(W2,W3,W4,b2,b3,b4):
    costvec=np.zeros(10)
    for i in range(0,10):
        x=np.array([[x1[k]],[x2[k]]])
    
        #Forward pass
        a2= activate(x,W2,b2)
        a3= activate(a2,W3,b3)
        a4= activate(a3,W4,b4)
        costvec[i]=(1/10)*np.linalg.norm(np.reshape(y[:,k],(2,1))-a4)

    return np.linalg.norm(costvec)**2

for counter in range(0,Niter):
    k=np.random.randint(10) #Choose a random training point
    x=np.array([[x1[k]],[x2[k]]])

    #Forward pass
    a2= activate(x,W2,b2)
    a3= activate(a2,W3,b3)
    a4= activate(a3,W4,b4)
    #Backward pass
    delta4= a4*(1-a4)*(a4- np.reshape(y[:,k],(2,1)) )
    delta3= a3*(1-a3)*(np.transpose(W4)@delta4)
    delta2= a2*(1-a2)*(np.transpose(W3)@delta3)
    #Gradient step
    W2 = W2 - eta*delta2@np.transpose(x)
    W3 = W3 - eta*delta3@np.transpose(a2)
    W4 = W4 - eta*delta4@np.transpose(a3)
    b2 = b2 - eta*delta2
    b3 = b3 - eta*delta3
    b4 = b4 - eta*delta4
    #Monitor progress
    newcost = cost(W2,W3,W4,b2,b3,b4)
    savecost[counter]=newcost

    if counter % 500 == 0:
        #Display cost every 500 iterations
        print(newcost)

x_plot=range(0,Niter,int(1e4))
#Shows decay of cost
plt.plot(x_plot,savecost[x_plot],'b')    
plt.xlabel('Iterations')
plt.ylabel('Cost')
plt.title('Cost for MATLAB Code')
plt.yscale("log")
plt.show()