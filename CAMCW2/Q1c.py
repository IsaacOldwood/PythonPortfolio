import numpy as np
import matplotlib.pyplot as plt
#Solution of tridiagonal amtrix from 2.6 Eperson "An Introduction to Numerical Methods and Analysis"
#Of the form Ax=f
#l is lower diagonal, d is diagonal and u is the upper diagonal

#n=4
#l=np.array([np.NaN,1.0,1.0,1.0])
#d=np.array([4.0,4.0,4.0,4.0])
#u=np.array([1.0,1.0,1.0,np.NaN])
#f=np.array([6.0,12.0,18.0,19.0])
#x=np.array([0.0,0.0,0.0,0.0])
#
##Elimination stage
#for i in range(1,(n)):
#    d[i] = d[i] - u[i-1] *l[i] / d[i-1]
#    f[i] = f[i] - f[i-1] *l[i] / d[i-1]
#
##backsolve stage
#x[(n-1)]= f[(n-1)]/d[(n-1)]
#for i in range((n-2),-1,-1):
#    x[i] = (f[i] - u[i] * x[i+1])/d[i]
#
#print(x)

#Calculate true values and plot
x_true=np.linspace(0,1)
y_true=(x_true)-np.sin(np.pi*x_true)

plt.plot(x_true,y_true,'b',label='True')

#Edit for given function
def f(x):
    return (np.pi**2.0)*np.sin(np.pi*x)
#Setting up the problem
alpha=0
beta=1
for m in [3,9,19]:
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
    x_approx=np.linspace(0,1,num=m+2)

    plt.plot(x_approx,U,'o-',label=f'{h}',linewidth=0.9)
plt.legend(loc=0)    
plt.xlabel('x')
plt.ylabel('u(x)')
plt.show()