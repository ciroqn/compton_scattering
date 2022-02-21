# Spectrum for 150 degrees and best fit w/ error bars

%matplotlib inline
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_notebook, show

# These two lines enable formatted printing of Pandas DataFrames
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"


# FIT K ALPHA TO 150 DEG. RESULT

x = onefifty['Channel']
y = onefifty['Counts']

#print(x.loc[300:340])

# define a Gaussian model
def GaussModel(x, a, x0, sigma):
    y_gauss = a*np.exp(-(x-x0)**2/(2*sigma**2))
    return y_gauss

# Specify starting parameters
p0 = [820, 320, 4]
# Specify lower and upper bounds. Each is a list of the three values
p_lower = [800, 310, 1]
p_upper = [840, 330, 7]

popt, pcov = curve_fit(GaussModel, x, y, p0, bounds = (p_lower, p_upper)) # <-- change this to p0 to fit 
                                                                               # peak A
# extract values from popt into named variables
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
print('The bin energy of K_alpha at 50 deg. is:')
print(f'{binEnergy(17.4, 19.6, 320, 339, 378):.3g} keV')
print('***************************************************')

#p1.scatter(x,y, legend = "Data")

# Find and plot error bars
xs = onefifty['Channel']
yerrs = []
for N in onefifty['Counts']:
    yerrs.append(np.sqrt(N))
    
ys = onefifty['Counts']

# ploterror bars
p1 = figure(title='Intensity of Photon Energies at 150 deg.', x_axis_label="Channel", y_axis_label="Counts", width=800, height=400)

p1.circle(xs, ys, color='gray', size=5, line_alpha=0, legend="Data")


# create the coordinates for the errorbars
err_xs = []
err_ys = []

# Optional: restricts error bars to these points
x1 = onefifty['Channel'].iloc[300:340]
y1 = onefifty['Counts'].iloc[300:340]
yerrs1 = yerrs[300:340]

for x, y, yerr in zip(x1, y1, yerrs1):
    err_xs.append((x, x))
    err_ys.append((y - yerr, y + yerr))

# plot them
p1.multi_line(err_xs, err_ys, color='red', legend='Error bars')

p1.line(xs, GaussModel(xs, a_fit, x0_fit, sigma_fit), 
        color = "green", 
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
