# The following plot gives 1/E_{out} vs 1-cos(theta) from experimental data AND a predicted straight line produced by inputting same energies into 
# the Compton formula.

%matplotlib inline
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from bokeh.plotting import figure, output_notebook, show

# These two lines enable formatted printing of Pandas DataFrames
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# Importing relevant csv and deleting all the cols and rows with 'NA' (should have been vetted before, but...)
data = pd.read_csv('errors_compton.csv')
df = data.dropna(how='all')
df_final = df.dropna(axis=1)
df_final

# Extract data from cols
e_out = df_final['scattered energy (keV)']
angle = df_final['angle (deg.)']

# Convert to radians
angle_rad = angle * np.pi/180

#Abosolute error (this needs to be changed. DON'T INLCUDE E1 in calculation for error)
y_err = df_final['(n-n1)/(n2-n1) % error']

## Dividing the fractional error by 100:
absol = y_err/100

# Check data looks correct
print('The absolute error:')
print(absol)

# Convert energy to joules 
energy_joules = e_out*1000*1.6*10**-19
# Check data looks correct
print('Energy in keV:')
print(e_out)
print('Energy in joules:')
print(energy_joules)

# These will be plotted against one another
inverse_Eout = 1/energy_joules
x_axis = 1 - np.cos(angle_rad)
#y_err_inv = 1/ y_err

#print(df_final.columns.tolist()) ----> Initially had trouble selecting 'n', but printing this showed that it was 'n '

binNum = df_final['n ']

# This is the quantity that has an error in it. This function finds the quantity to be tweaked for each n - it does not find the error
def findingError(n):
    calculation = abs(n-339)*(((19.6*1000*1.6*10**-19)-(17.4*1000*1.6*10**-19))/(378-339))
    return calculation

# Fidning corresponding quantity for each n
stage1_errors =[]
for bin in binNum:
    stage1_errors.append(findingError(bin))
    
# Convert to array:
stage1_errs_arr = np.array(stage1_errors)

# What is the error in the above values for each bin, n?
stage1_errs_absol = stage1_errs_arr*absol

# finding fractional error (or percentage error) i.e. error/E_out
fractional_errs = stage1_errs_absol/energy_joules


# Now that we have a fraction, we multiply the inverse Eout with this fractional error
final_errs = fractional_errs*inverse_Eout

# These print statements check data looks acceptable
print('Look here:',final_errs)


print('The energy errors without E1')
print(stage1_errs_arr_absol)
print('Inv Errors are:')
print(stage2_errors)
print('Inverse energies are:')
print(inverse_Eout)

#y_err_final_j = inv_eout_j*absol

# Now to find predicted data points and line etc.
theoretical = []

def theoreticalCompt(angle):
    angle_radians = angle*(np.pi/180)
    electronRest = (9.1*10**-31)*(3*10**8)**2
    trig = 1-np.cos(angle_radians)
    return (17.4*1000*1.6*10**-19) / (1 + ((17.4*1000*1.6*10**-19)/(electronRest))*trig)

for angle in df_final['angle (deg.)']:
    theoretical.append(theoreticalCompt(angle))
    
theoretical_arr = np.array(theoretical)

# Calculating theoretical energies in keV

theoretical_ = []

for angle in df_final['angle (deg.)']:
    theoretical_.append(theoreticalCompt(angle))
    
theoretical_arr = np.array(theoretical_)

theoretical_kev = (theoretical_arr/1000)/(1.6*10**-19)

print('Here are the theoretical E_out energies:')
print(theoretical_kev)

inv_theory = 1/theoretical_arr

print(inv_theory)

# ------------------------------ Now to plot extracted data ------------------------------

from scipy.stats import linregress

# This single line does the linear regression fit
m, c, r, p, stderr = linregress(x_axis, inverse_Eout)

# This is for thereotical line:
mt, ct, rt, pt, stderrt = linregress(x_axis, inv_theory)

print(f'Gradient: {m:.2f} +/- {stderr:.2f}, Intercept: {c:.2f}')
print(f'Correlation coefficient: {r:.3f}')

print(f'Gradient: {mt:.2f} +/- {stderrt:.2f}, Intercept: {ct:.2f}')
print(f'Correlation coefficient: {rt:.3f}')

# Plot the line on to the data:
xstart = x_axis.min() - 0.25                 # calculate start and end x values
xend   = x_axis.max() + 0.25                 # for plotting the fitted line 
xlin   = np.linspace(xstart, xend, 50) # create array of x values for the line
ylin   = m*xlin+c                      # generate the y values for the straight line

# For theoretical line:
ylin_t   = mt*xlin+ct  

plt.plot(xlin, ylin, color = 'blue', label= 'Best fit')    # plot the fitted line 
plt.plot(xlin, ylin_t, color = 'red', label= 'Theoretical line')

plt.rcParams['figure.figsize'] = [12, 8]
plt.rcParams['font.size'] = 18
plt.scatter(x_axis, inverse_Eout, ls='None', label="Data points")
plt.scatter(x_axis, inv_theory, color='red', label='Theoretical data points')
plt.title('Deflected Photon Energies')
plt.ylabel(r'$\frac{1}{E_{out}}$ / $ \times 10^{14}$ $J^{-1}$ ')
plt.xlabel(r'$1-cos(\theta)$')
plt.legend()
plt.errorbar(x_axis, inverse_Eout, yerr=final_errs, ls='None', ecolor='black', capsize=5)
#plt.savefig('photonenergy.png')
