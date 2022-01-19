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


