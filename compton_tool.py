# This file refers to the Compton scattering tool and using two different datasets: the first has a longer count period (6 minutes) which decreses the certainty 
# in the counts made by the detector. The second dataset involves counting to 30 seconds for each energy, and this of course increased the uncertainity in the 
# total number of counts. The energies for each "experiment" were were varied from 18.6keV to 17.4keV (with 0.1keV decrements). The angular resolution was 1 deg.
# and the energy window was 0.2 keV. If either of these were too small, the photon count would be very low. If they were high, then, the width of the k_alpha
# peaks would be large and therefore not very precise.

%matplotlib inline
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_notebook, show

# These two lines enable formatted printing of Pandas DataFrames
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# Read 1st dataset
dataset_one = pd.read_csv('compt_scattering_tool.csv', header=1)

dataset_one.head()

plt.rcParams['figure.figsize'] = [12, 8]

# Quick plot to see if data points look reasonable:
dataset_one.plot('energy (keV)', 'counts', kind="scatter", title="Data from 1st Compton Scattering Tool Experiment")

######################## Plotting 1st Dataset using Bokeh and Matplotlib #######################

from scipy.optimize import curve_fit

output_notebook()

# define a Gaussian model, since the data points require such a model
def GaussModel(x, a, x0, sigma):
    y_gauss = a*np.exp(-(x-x0)**2/(2*sigma**2))
    return y_gauss

x = dataset_one['energy (keV)']
y = dataset_one['counts']

# Finding initial guess for parameters a, x0 and sigma (a=amplitude, x0=peak datapoint, sigma=measure half peak x values)
p0 = [260, 17.8, 0.2]

# Getting best-fit data and errors:
popt, pcov = curve_fit(GaussModel, x, y, p0)

print(popt)
print(pcov)

a_fit = popt[0]
x0_fit = popt[1]
sigma = popt[2]

# Now to determine errors on fit parameters. We do this by finding the sqrt of the diagonal of pcov matrix:
perr = np.sqrt(np.diag(pcov))

print('\n')
print('The fit parameters with errors ----------------')
print(f'The amplitude A: {a_fit:.3g} +- {perr[0]:.3g}')
print(f'The central peak, x0: {x0_fit:.3g} +- {perr[1]:.3g}')
print(f'The standard deviation, sigma: {sigma:.3g} +- {perr[2]:.3g}')
print('-----------------------------------------------')

# This is plotting in Bokeh
p1 = figure(title="Data for Compton Scattering with Six-minute recording sessions",
           x_axis_label = 'Energy / keV',
           y_axis_label = 'Count')

p1.scatter(x, y, legend='Data')

p1.line(x, GaussModel(x, a_fit, x0_fit, sigma),
       color = 'green',
       line_dash="dashed",
       legend="Optimised Curve")

p1.legend.location = "top_left"
show(p1)

# This is plotting in Matplotlib - This is better because it is a lot easier than Bokeh to plot error bars:
y_err = dataset_one['counts_err']
plt.errorbar(x, y, yerr = y_err, capsize = 2, fmt = 'o')
plt.plot(x, GaussModel(x, a_fit, x0_fit, sigma), color='blue', linestyle='dotted')
plt.xlabel('Energy (keV)')
plt.ylabel('Counts')
plt.title('Data for Compton Scattering with six-minute recording sessions')
plt.show()

