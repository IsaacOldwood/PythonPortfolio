import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Set values
r=0
sigma=0.5
K=100
R=300
t=0.01
#Define funcitons
def d_plus(t,x):
    return (1/ (sigma * np.sqrt(t)) ) * ( np.log(x/K) + (r + ( (sigma**2)/2 ) ) * t )
def d_minus(t,x):
    return (1/ (sigma * np.sqrt(t)) ) * ( np.log(x/K) + (r - ( (sigma**2)/2 ) ) * t )
def f0(t):
    return K * np.exp(-r *t)
def v_exact(t,x):
    return K * np.exp(-r *t) * norm.cdf( (-d_minus(t,x)) - x * norm.cdf((-d_plus(t,x))) )
def fR(t):
    return v_exact(t,R)
def g(x):
    if x<K:
        return K-x
    else:
        return 0
def a(i):
    return 0.5 * delta_t * (r*i - (sigma**2) * (i**2))
def b(i):
    return 1 + delta_t* ( (sigma**2)*(i**2) + r )
def c(i):
    return -0.5 * delta_t * (r*i + (sigma**2)*(i**2) )

#Setup problem
#Setting up the problem
for m in [3,4,9]:
    h=R/(m+1)
    C=1
    delta_t=1/(4**2)
    VN=np.empty(m)
    u=np.empty(m-1)
    d=np.empty(m)
    l=np.empty(m-1)
    little_f=np.empty(m)
    F=np.empty(m)
    VN1=np.empty(m)
    x=np.arange(0,(1+h),h)

    #Creating F
    little_f[0]=-a(1) * f0(t)
    little_f[m-1]=-c(m-1) * fR(t)
    VN[0]=g(x[1])
    VN[m-1]=g(x[m])
    for i in range(1,m-1):
        little_f[i]=0
        VN[i]=g(x[i+1])

    #Creating tridiagonal matrix K
    for i in range(0,m):
        if i != (m-1):
            u[i]=c(i+1)
            l[i]=a(i+2)
        d[i]=b(i+1)



    for t in np.arange(0,(1+delta_t),delta_t):
        F=VN + little_f
        u=np.empty(m-1)
        d=np.empty(m)
        l=np.empty(m-1)
        #Creating tridiagonal matrix K
        for i in range(0,m):
            if i != (m-1):
                u[i]=c(i+1)
                l[i]=a(i+2)
            d[i]=b(i+1)
        
        #Solving the tridiagonal problem
        #Elimination stage
        for i in range(1,(m)):
            d[i] = d[i] - u[i-1] *l[i-1] / d[i-1]
            F[i] = F[i] - F[i-1] *l[i-1] / d[i-1]

        #backsolve stage
        VN1[(m-1)]= F[(m-1)]/d[(m-1)]
        for i in range((m-2),-1,-1):
            VN1[i] = (F[i] - u[i] * VN1[i+1])/d[i]

        #Reset for next iteration
        VN=VN1

    #Insert boundary values
    VN1=np.insert(VN1,0,f0(t))
    VN1=np.insert(VN1,m+1,fR(t))  

    #Print answer
    #print(VN1)
    #Plotting
    x_approx=np.linspace(0,1,num=m+2)
    plt.plot(x_approx,VN1,'o-',label=f'{h}',linewidth=0.9)


#Calculate true values and plot
x_true=np.linspace(0,1)
t_true=0.01
y_true=v_exact(t_true,x_true)

plt.plot(x_true,y_true,'b',label='True')
plt.legend(loc=0)    
plt.title(f't={t}')
plt.xlabel('x')
plt.ylabel('u(x)')
plt.show()