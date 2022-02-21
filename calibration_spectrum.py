%matplotlib inline
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_notebook, show

# These two lines enable formatted printing of Pandas DataFrames
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

from scipy.optimize import curve_fit

output_notebook()

# ------------------------------ Adding Gaussian best fit to K_{alpha} peak ------------------------------

from bokeh.models import Arrow, Label, NormalHead, OpenHead

calibration = pd.read_csv('calibration-35kv.csv')

x = calibration['Channel']
y = calibration['Counts']

# define a Gaussian model
def GaussModel(x, a, x0, sigma):
    y_gauss = a*np.exp(-(x-x0)**2/(2*sigma**2))
    return y_gauss

# Specify parameters that approximately match alpha peak
p0 = [1600, 338, 9.5]
# Specify lower and upper bounds. Each is a list of the three values
p_lower = [1500, 330, 1]
p_upper = [1700, 350, 10]

# Below is for attempting to fit to beta peak, but for now, it's left out
#p01 = [410, 380, 1]
# TODO: Modify the program to prompt the user to specify values
# upper_a = input('Specify a value for upper limit: ')
#p01_lower = [400, 375, 1]
#p01_upper = [420, 385, 7]


# Using curve_fit and Gaussian model defined, with x's, y's and the bounds to give best possible fit
popt, pcov = curve_fit(GaussModel, x, y, p0, bounds = (p_lower, p_upper)) # <-- change this to p0 to fit 
                                                                               # peak A

# popt gives info on counts, central channeel and sigma
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

# This section is for errorbars (probably easier to use matplotlib here...
xs = calibration['Channel']
yerrs = []
# Error in counts is the sq. root of the counts, N:
for N in calibration['Counts']:
    yerrs.append(np.sqrt(N))
    
ys = calibration['Counts']

# plot the points
p1 = figure(title='Intensity of Photon Energies', x_axis_label="Channel", y_axis_label="Counts", width=800, height=400)

p1.circle(xs, ys, color='gray', size=5, line_alpha=0, legend="Data")


# create the coordinates for the errorbars
err_xs = []
err_ys = []

x1 = calibration['Channel']
y1 = calibration['Counts']
yerrs1 = yerrs

# Extracting y-err bars
for x, y, yerr in zip(x1, y1, yerrs1):
    err_xs.append((x, x))
    err_ys.append((y - yerr, y + yerr))

# plot errorbars
p1.multi_line(err_xs, err_ys, color='blue', legend='Error bars')


# Now to plot spectrum
p1.scatter(xs,ys, legend = "Data", color='gray')

p1.line(xs, GaussModel(xs, a_fit, x0_fit, sigma_fit), 
        color = "red", 
        line_dash = "solid", 
        legend = "Optimised curve")
# Mark centreline
p1.line((x0_fit, x0_fit),(0, a_fit*1.10),
        color = "orangered", 
        line_dash = "dotted", 
        legend = "Centreline")

p1.add_layout(Arrow(end=OpenHead(line_color="black", line_width=1),
                   x_start=450, y_start=1650, x_end=339, y_end=1500))

p1.add_layout(Label(x=450, y=1640, text='Kₐ'))

p1.legend.location = "top_left"
p1.legend.click_policy = "hide"
show(p1)

# ------------------------------- Plotting Gaussian best fit for K_{beta} peak -------------------------------

# Process much the same as above:

# Starting parameters for beta peak
p01 = [410, 380, 1]
# Define upper and lower bounds
p01_lower = [400, 375, 1]
p01_upper = [420, 385, 7]

popt, pcov = curve_fit(GaussModel, x, y, p01, bounds = (p01_lower, p01_upper)) # <-- change this to p0 to fit 
                                                                               # peak A
# Extract values from popt into named variables
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

# Again plotting error bars
xs = calibration['Channel']
yerrs = []
for N in calibration['Counts']:
    yerrs.append(np.sqrt(N))
    
ys = calibration['Counts']

# plot the points
p1 = figure(title='Intensity of Photon Energies', x_axis_label="Channel", y_axis_label="Counts", width=800, height=400)

p1.circle(xs, ys, color='gray', size=5, line_alpha=0, legend="Data")


# create the coordinates for the errorbars
err_xs = []
err_ys = []

x1 = calibration['Channel']
y1 = calibration['Counts']
yerrs1 = yerrs

for x, y, yerr in zip(x1, y1, yerrs1):
    err_xs.append((x, x))
    err_ys.append((y - yerr, y + yerr))

# plot bars
p1.multi_line(err_xs, err_ys, color='blue', legend='Error bars')

# and plot data
p1.scatter(xs,ys, legend = "Data", color='gray')

p1.line(xs, GaussModel(xs, a_fit, x0_fit, sigma_fit), 
        color = "red", 
        line_dash = "solid", 
        legend = "Optimised curve")
# Mark centreline
p1.line((x0_fit, x0_fit),(0, a_fit*1.10),
        color = "orangered", 
        line_dash = "dotted", 
        legend = "Centreline")

p1.add_layout(Arrow(end=OpenHead(line_color="black", line_width=1),
                   x_start=450, y_start=650, x_end=385, y_end=430))

p1.add_layout(Label(x=460, y=650, text='Kᵦ'))

p1.legend.location = "top_left"
p1.legend.click_policy = "hide"
show(p1)
