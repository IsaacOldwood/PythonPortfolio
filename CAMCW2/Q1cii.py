import numpy as np
import matplotlib.pyplot as plt

#Edit for given function
def f(x):
    return (np.pi**2.0)*np.sin(np.pi*x)
#Setting up the problem
alpha=0
beta=1
error_vec=[]
h_vec=[]
for m in [3,9,19,24,49,99,199]:
    h=1/(m+1)
    u=(1/(h**2))*np.ones(m-1)
    d=(1/(h**2))*(-2.0)*np.ones(m)
    l=(1/(h**2))*np.ones(m-1)
    F=np.empty(m)
    U=np.empty(m)
    x=np.arange(0,(1+h),h)

    #Creating F
    F[0]=f(x[1]) - ( alpha/(h **2) )
    F[m-1]=f(x[m-1]) - ( beta/(h **2) )
    for i in range(1,m-1):
        F[i]=f(x[i+1])


    #Solving the tridiagonal problem
    #Elimination stage
    for i in range(1,(m)):
        d[i] = d[i] - u[i-1] *l[i-1] / d[i-1]
        F[i] = F[i] - F[i-1] *l[i-1] / d[i-1]

    #backsolve stage
    U[(m-1)]= F[(m-1)]/d[(m-1)]
    for i in range((m-2),-1,-1):
        U[i] = (F[i] - u[i] * U[i+1])/d[i]

    #Insert end values
    U=np.insert(U,0,alpha)
    U=np.insert(U,m+1,beta)
    #Print answer
    #print(U)
    #Calculate true values and plot
    x_true=np.linspace(0,1,num=m+2)
    y_true=(x_true)-np.sin(np.pi*x_true)
    
    #Calculate error
    error= np.sqrt(h*np.sum( np.abs(y_true-U)**2 ))
    error_vec.append(error)
    h_vec.append(h)
    
print(h_vec)
print(error_vec)
plt.plot(h_vec,error_vec,'bo')    
plt.xlabel('h')
plt.ylabel('Error')
plt.yscale("log")
plt.xscale("log")
plt.show()

for i in range(0,len(error_vec)):
    print(error_vec[i-1]/error_vec[i])