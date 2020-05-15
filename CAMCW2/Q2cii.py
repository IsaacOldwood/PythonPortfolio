import numpy as np
import matplotlib.pyplot as plt

#Set values
t=0
a=np.pi**(-2)
g0=0
g1=1
error_vec=[]
h_vec=[]
delta_t_vec=[]
#Edit for given function
def f():
    return 0
def u0(x):
    return np.sin(2*np.pi*x)+(x)
#Setting up the problem
for m in [3,7,15,31,63]:
    h=1/(m+1)
    delta_t=2*(h**2)
    UN=np.empty(m)
    lam=(a*delta_t)/(h**2)
    u=(lam*(-1)) *np.ones(m-1)
    d=(1+lam*(2))*np.ones(m)
    l=(lam*(-1)) *np.ones(m-1)
    little_f=np.empty(m)
    F=np.empty(m)
    UN1=np.empty(m)
    x=np.arange(0,(1+h),h)

    #Creating F
    little_f[0]=delta_t*f() + lam* (g0)
    little_f[m-1]=delta_t*f() + lam* (g1)
    UN[0]=u0(x[1])
    UN[m-1]=u0(x[m])
    for i in range(1,m-1):
        little_f[i]=delta_t*f()
        UN[i]=u0(x[i+1])



    for t in np.arange(0,(1+delta_t),delta_t):
        F=UN + little_f
        u=(lam*(-1)) *np.ones(m-1)
        d=(1+lam*(2))*np.ones(m)
        l=(lam*(-1)) *np.ones(m-1)
        #print(t)
        #Solving the tridiagonal problem
        #Elimination stage
        for i in range(1,(m)):
            d[i] = d[i] - u[i-1] *l[i-1] / d[i-1]
            F[i] = F[i] - F[i-1] *l[i-1] / d[i-1]

        #backsolve stage
        UN1[(m-1)]= F[(m-1)]/d[(m-1)]
        for i in range((m-2),-1,-1):
            UN1[i] = (F[i] - u[i] * UN1[i+1])/d[i]

        #Reset for next iteration
        UN=UN1

    #Insert boundary values
    UN1=np.insert(UN1,0,g0)
    UN1=np.insert(UN1,m+1,g1)
    #Calculate true values and plot
    x_true=np.linspace(0,1,num=m+2)
    t_true=1
    y_true=np.exp(-4*t_true) * np.sin(2*np.pi*x_true) + (x_true)

    #Calculate and save error
    error= np.max( np.abs( y_true - UN1 ) )
    error_vec.append(error)
    h_vec.append(h)
    delta_t_vec.append(delta_t)

#Print answer
#print(UN1)
#Plotting
x_approx=np.linspace(0,1,num=m+2)

plt.plot(h_vec,error_vec,'bo')    
plt.xlabel('h')
plt.ylabel('Error')
plt.yscale("log")
plt.xscale("log")
plt.show()

print(h_vec)
print(delta_t_vec)
print(error_vec)

for i in range(0,len(error_vec)):
    print(error_vec[i-1]/error_vec[i])