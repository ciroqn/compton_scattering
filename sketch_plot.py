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
