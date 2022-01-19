# Import necessary packages
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# pd dataframe formatting
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

fineBeam = pd.read_csv('fine_beam.csv', header=1, nrows=7)

#Check
fineBeam

x = fineBeam['current (A)']
y = fineBeam['voltage (V)']

# Squaring x values (i.e. current/i)
x_sq = x**2

print(x_sq)

plt.rcParams['figure.figsize'] = [12, 8]
plt.scatter(x_sq, y)

########### Plot with line of best fit (importing linregress to do this) #############

from scipy.stats import linregress

m, c, r, p, stderr = linregress(x_sq, y)

print(f'Gradient is {m:.2f} +/- {stderr:.2f}, Intercept: {c:.2f}')
print(f'Correction coefficient: {r:.3f}')

# This line is plotted on the data points:
startLine_x = x_sq.min() -0.1
endLine_x = x_sq.max() +0.1
xlin = np.linspace(startLine_x, endLine_x, 50)
ylin = m*xlin+c

plt.scatter(x_sq, y)
plt.plot(xlin, ylin, 'g')

########### Plot with curve_fit (importing curve_fit to do this) #############

# curve_fit provides more data on m, c, and covariance. It can fit straight lines, despite its name.

from scipy.optimize import curve_fit

def StrtLineModel(x, m, c):
    y_lin = m*x+c
    return (y_lin)

popt, pcov = curve_fit(StrtLineModel, x_sq, y)

print(popt)  # gives m and c values
print(pcov)  # gives covariance, square errors in m, c

perr = np.sqrt(np.diag(pcov))  # error values in m and c

m_fit = popt[0]
c_fit = popt[1]
m_err = perr[0]
c_err = perr[1]

print('------------------------------------')
print(f'm = {m_fit:.2f} +/- {m_err:.2f}')
print(f'c = {c_fit:.2f} +/- {c_err:.2f}')
print('------------------------------------')

# Plotting data

plt.scatter(x_sq, y)
plt.plot(x_sq, SrtLineModel(x_sq, m_fit, c_fit), 'g')



# Now plotting x- and y- errors. Although the errors in x (current) are much larger:
y_err = fineBeam['v_err (V)']
x_err = fineBeam['curr_err (A)']

x_err_percent = []

count = 0
for element in x_err:
    x_err_percent.append(element/fineBeam['current (A)'][count])
    count += 1
    
print('The x_err as a percentage of x')   
print(x_err_percent)
print('\n')

# For error propagation, since i^2, then the error in i is multiplied by 2 (since n=2):
i_sq_err = 2*np.array(x_err_percent)

print('Propagating error to account for i^2:')
print(i_sq_err)
print('\n')

i_sq_abs = []
count_ = 0
for element in i_sq_err:
    i_sq_abs.append(element*x_sq[count_])
    count_ += 1
    
print('Printing the absolute value of errors for i^2:')
print(i_sq_abs)
print('\n')
    

plt.errorbar(x_sq, y, xerr=i_sq_abs, yerr = y_err, capsize = 2, fmt='o')
