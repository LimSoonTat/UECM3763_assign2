from pandas.io.data import DataReader as DR
from datetime import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

#The collection of data starting from 17/7/2010 to 16/7/2015
start = dt(2012, 7, 17)
end = dt(2015, 7, 16)

#Task 2
#Hong Leong Bank Berhad with stock code: 5819.KL is chosen
HongLeong_close= DR("5819.KL", 'yahoo', start, end)['Close']

#define function to calculate moving average
def moving_average(values,average_day):
    weights=np.repeat(1.0,average_day)/average_day
    sma = np.convolve(values,weights,'valid')
    return sma
    
#calculate 5 days moving average
moving_average_5=moving_average(HongLeong_close,5)  

#To plot the moving average
count = len(moving_average_5)
xaxis = np.arange(count)+5
yaxis = moving_average_5
plt.xlabel('Day $n$')
plt.ylabel('Moving Average')
plt.plot(xaxis,yaxis)
plt.title('Plot of 5-day Moving Average')

print(' ')
print('FTSEKLCI component chosen: HONG LEONG BERHAD')
print(' ')
print('The 5-day moving average plot is as following:')
plt.show()

#5819.KL and ^KLSE is the stock code for Hong Leong Bank Berhad and KLSE respectively
combine=['5819.KL','^KLSE']
#To download the closing data of Hong Leong Bank Berhad and KLCI index
closing = DR(combine, 'yahoo', start, end)['Close']
#To find the correlation of Hong Leong Bank Berhad and KLSE
correlation = closing.corr()

print(' ')
print('The correlation of FTSEKLCI and Hong Leong Bank Berhad is as following:')
print(correlation)
print(' ')