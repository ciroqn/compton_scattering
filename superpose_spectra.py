# superposing spectra from calibration and target angles (30-150, 10++) to see the shift of photon energies more clearly after scattering

%matplotlib inline
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_notebook, show

# These two lines enable formatted printing of Pandas DataFrames
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# Read all csv files

calib = pd.read_csv('calibration-35kv.csv')
thirty = pd.read_csv('30.csv')
fifty = pd.read_csv('50.csv')
seventy = pd.read_csv('70.csv')
ninety = pd.read_csv('90.csv')
oneten = pd.read_csv('110 - 35kv.csv')
onethirty = pd.read_csv('130.csv')
onefifty = pd.read_csv('150.csv')

#Check
calib.head()

output_notebook()

#Plot all spectra
plt.rcParams['figure.figsize'] = [16, 8]
plt.rcParams['font.size'] = 18
plt.plot(calib['Channel'], calib['Counts'], label="Calibration")
plt.plot(thirty['Channel'], thirty['Counts'], label="$30^{0}$")
plt.plot(fifty['Channel'], fifty['Counts'], label="$50^{0}$")
plt.plot(seventy['Channel'], seventy['Counts'], label="$70^{0}$")
plt.plot(ninety['Channel'], ninety['Counts'], label="$90^{0}$")
plt.plot(oneten['Channel'], oneten['Counts'], label="$110^{0}$")                        
plt.plot(onethirty['Channel'], onethirty['Counts'], label="$130^{0}$")                                                                    
plt.plot(onefifty['Channel'], onefifty['Counts'], label="$150^{0}$")
#plt.title('Deflected Photon Energies')
plt.ylabel('Counts')
plt.xlabel('Channel')
plt.legend()
#plt.savefig('compare_plots.png')
plt.show()
