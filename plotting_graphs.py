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

# FINDING K_BETA PEAK, BIN NO., BEST FIT ETC...

def GaussModel(x, a, x0, sigma):
    y_gauss = a*np.exp(-(x-x0)**2/(2*sigma**2))
    return y_gauss

# Specify starting parameters that approximately match Peak A
p0 = [1600, 338, 9.5]
# Specify lower and upper bounds. Each is a list of the three values
p_lower = [1500, 330, 1]
p_upper = [1700, 350, 10]

# TODO: Change the initial values and bounds to match Peak B
p01 = [410, 380, 1]
# TODO: Modify the program to prompt the user to specify values
# upper_a = input('Specify a value for upper limit: ')
p01_lower = [400, 375, 1]
p01_upper = [420, 385, 7]

# The bounds constrain fit to region of Peak A
# The bounds are specified as a tuple with two elements.  
# The first is a list of the lower bounds of the 
# three parameters, and the second a list of the upper bounds
popt, pcov = curve_fit(GaussModel, x, y, p01, bounds = (p01_lower, p01_upper)) # <-- change this to p0 to fit 
                                                                               # peak A

# For readability, extract values from popt into named variables
a_fit     = popt[0]
x0_fit    = popt[1]
sigma_fit = popt[2]


print('fit parameters')
print('***************************************************')
print (f'A     = {a_fit: .3g}')
print (f'x0    = {x0_fit: .3g}')
print (f'sigma = {sigma_fit: .3g}')
print('***************************************************')

# Calculate the errors on the returned parameters
perr = np.sqrt(np.diag(pcov)) # squares of the error values are 
                              # on the covariance matrix diagonal

# For readability, extract values from perr into named variables
a_err     = perr[0]
x0_err    = perr[1]
sigma_err = perr[2]

#print fit parameters and error estimates
print()
print('fit parameters with error estimates')
print('***************************************************')
print(f'A     = {a_fit: .3g} +/- {a_err: .3g}')
print(f'x0    = {x0_fit: .3g} +/- {x0_err: .3g}')
print(f'sigma = {sigma_fit: .3g} +/- {sigma_err: .3g}')
print('***************************************************')

# Plot the data points and the optimised curve
# This time using Bokeh to generate an interactive plot
p1 = figure(title = "Intensity of Photon Energies", 
            x_axis_label = "Channel", 
            y_axis_label = "Count")

p1.scatter(x,y, legend = "Data")

p1.line(x, GaussModel(x, a_fit, x0_fit, sigma_fit), 
        color = "red", 
        line_dash = "solid", 
        legend = "Optimised curve")
# Mark centreline
p1.line((x0_fit, x0_fit),(0, a_fit*1.10),
        color = "orangered", 
        line_dash = "dotted", 
        legend = "Centreline")

p1.legend.location = "top_left"
p1.legend.click_policy = "hide"
show(p1)
