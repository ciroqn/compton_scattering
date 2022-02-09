# Plotting graphs through angles 30 -150 with 10 deg. increments

%matplotlib inline
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_notebook, show

# These two lines enable formatted printing of Pandas DataFrames
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

################################### CALIBRATION DATA AND PLOT (K_ALPHA AND K_BETA)#####################################

calibration = pd.read_csv('calibration-35kv.csv')

calibration.head()

x = calibration['Channel']
y = calibration['Counts']

plt.rcParams['figure.figsize'] = [12,8]
plt.scatter(x, y)
