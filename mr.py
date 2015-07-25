import pylab as p
import numpy as np

#Setup parameters
alpha = 1;  theta = 0.064 
sigma = 0.27; R0 = 3
time = 1
n_path = 1000; n_partition= 1000

#Create Brownian paths
dt = time / n_partition
t = p.linspace(0,time,n_partition+1)[:-1];
dB = p.randn(n_path,n_partition+1) * p.sqrt(dt); dB[:,0] = 0;
B = dB.cumsum(axis=1);

# Generating Variable R
R = p.zeros_like(B)

R[:,0] = R0
for col in range(n_partition):
    R[:,col+1] = R[:,col] + (theta-R[:,col])*dt + sigma*R[:,col]*dB[:,col+1]


#Plotting only 5 realizations of R
R_plot = R[0:5:,:-1]
p.plot(t,R_plot.transpose())
label = 'Time , t' ; p.xlabel(label)          
label = '$R_t$' ; p.ylabel(label)
para1 = '\n with $\\alpha$ = 1' 
para2 = ', $\\theta$ = 0.064'
para3 = ', and $\sigma$ = 0.027 \n'
p.title('5 runs of Mean reversal process for ' + label + para1 + para2 + para3)
p.show();

#Calculate the expectation value of R(1) based on the simulation
E_R1= np.mean(p.array(R[:,-1]))
print('E(R1) = ' + str(E_R1))

#calculation for P[R(1)> 2]
mask = R[:,-1] > 2
P_R1 = sum(mask)/n_path
print('P(R1 > 2) = ' + str(P_R1))