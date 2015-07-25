import pylab as p
import numpy as np

#Setup parameters
mu=0.1; sigma=0.26;S0=39
n_path=1000; n=n_partitions=1000;
period=3;

#theoritical expectation and variance
T_E = S0 * p.exp(mu*period)
T_Var = (S0**2)*(np.exp(2*mu*period))*(np.exp(sigma*sigma*period)-1)
print('Theoritical Expectiation and Variance')
print('E[S(3)] = ' + str(T_E))
print('Var[S(3)]= ' + str(T_Var))

#Create Brownian paths
t=p.linspace(0,period,n+1);
dB=p.randn(n_path,n+1)/p.sqrt(n/period);dB[:,0]=0;
B=dB.cumsum(axis=1);

#Calcualte stock prices
nu=mu-sigma*sigma/2.0
S=p.zeros_like(B);S[:,0]=S0
S[:,1:]=S0*p.exp(nu*t[1:]+sigma*B[:,1:])

#Plotting only 5 realizations of the GBM
S_plot=S[0:5]
label = 'Time , $t$' ; p.xlabel(label)
label = 'Stock prices, $S$' ; p.ylabel(label)
title = '\n with $\mu$ = ' + str(mu) +'and $\sigma$ = ' + str(sigma) + '\n'
p.title('5 runs of GBM' + title )
p.plot(t,S_plot.transpose());
p.show();

#Calculate the expectation value of S(3) based on the simulation
S_T3=np.array(S[:,-1])
E_S_T3=np.mean(S_T3)
print('\nE(S3) = ' + str(E_S_T3))

#Calculate the variance of S(3)
Var_S_T3=np.var(S_T3)
print('Var(S3) = ' + str(Var_S_T3))

#Calculate P[S(3)> 39]
count=S_T3>39
P_S3_MT39=(sum(count)/len(S_T3))
print('P(S3 > 39) = '+str(P_S3_MT39))

#Calculate E[S(3) | S(3) > 39]                 
S3_MT39 = S_T3 * count               
E_S3_MT39 = sum(S3_MT39) / sum(count)
print('E[S3 | S3 > 39] = ' + str(E_S3_MT39))