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
