import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#Set values
r=0
sigma=0.5
K=100
R=300
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

#Setup problem