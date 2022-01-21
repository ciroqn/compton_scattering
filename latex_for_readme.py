# This is a Python file, despite the title of this document, since Jupyter Notebooks is a good interface in which to run Markdown and LaTeX...

# Fine-beam Tube Experiment to Determine charge-mass ratio of the electron

Electrons travelling through the cathode-anode voltage gain energy proportional to the potential difference between the cathode and anode. The Wehnelt funnel acts as a collimator as the electrons are released from the cathode via thermionic emission:
<br>
<br>


$\large \frac{1}{2} m_{e} v^{2}_{e} = e V $


<br>
<br>
And so, isolating the electron velocity,
<br>
<br>

$\large v^{2}_{e} = \frac{2Ve}{m_{e}}$

<br>
<br>
The magnetic component of the Lorentz force has an effect on these electrons, such that:
<br>
<br>

$\large \lvert F_{m} \rvert = \lvert -e(\vec{v_{e}} \times \vec{B}) \rvert $
<br>
<br>

Given that $\theta = 90$ between the velocity of the electrons and the direction of the magnetic field (acting in the place of the electron trajectories), then the magnetic Lorentz force can be equated to the centripetal force:

<br>
<br>
$\large \lvert F_{m} \rvert = ev_{e}B = \frac{m_{e} v^{2}_{e}} {R_{beam}}$

<br>
<br>
$\large \longrightarrow v^{2}_{e}=B^{2}R^{2}_{beam} (\frac{e}{m_{e}})^{2}$

<br>
<br>
Where $R_{beam}$ is the radius of the circle that the electrons follow in the magnetic field. The velocity of the electrons, $v^{2}_{e}$, can eventually be found by equating the two expressions:
<br>
<br>

$\large V = \frac{1}{2} B^{2} R^{2}_{beam} \frac{e}{m_{e}}$

<br>
<br>
The quantity, $\frac{e}{m_{e}}$ is what will eventually be found by calculating the gradient of the graph plotting the Voltage, V, against $i^{2}$. However, the gradient does contain a number of other values, and $\vec{B}$ cannot be measured directly. It is only known that, in this particular experiment $\lvert \vec{B} \rvert \propto i$.
The const of proportionality between $\lvert \vec{B} \rvert$ and $i$ is $k_{coils}$, where,

<br>
<br>
$ \large k_{coils} = \frac{8\mu_{0}}{5\sqrt{5}}\frac{N}{R_{coils}}$

<br>
<br>
Where $N = 130$ and $R_{coils} = 15.0cm$ and the free space of permeability is $4\pi\times10^{-7} T m A^{-1}$

<br>
<br>
Thus, the formula for the Voltage, V, becomes:

<br>
<br>
$\large V = \frac{1}{2} k^{2}_{coils} i^{2} R^{2}_{beam} \frac{e}{m_{e}}$
<br>
<br>
$ \large \longrightarrow V = (\frac{1}{2} k^{2}_{coils} R^{2}_{beam} \frac{e}{m_{e}}) i^{2}$
<br>
<br>
$ \large \longrightarrow V = (\frac{1}{2} (\frac{8\mu_{0}}{5\sqrt{5}}\frac{N}{R_{coils}})^{2} R^{2}_{beam} \frac{e}{m_{e}}) i^{2}$

<br>
<br>
This means that:
<br>
<br>
$ \large grad. = m = \frac{1}{2} (\frac{8\mu_{0}}{5\sqrt{5}}\frac{N}{R_{coils}})^{2} R^{2}_{beam} \frac{e}{m_{e}}$

But for the voltage vs the radius of the beam squared, we have a slightly different radius:

$ \large grad. = m = \frac{1}{2} (\frac{8\mu_{0}}{5\sqrt{5}}\frac{N}{R_{coils}})^{2} i^{2} \frac{e}{m_{e}}$

The results are:

(a) for $V$ against $i^{2}$ (keeping $R_{beam}$ constant:

$\large \frac{e}{m_{e}} = -2.63 \times 10^{11} \pm 16\% \: C \ kg^{-1}$

(a) for $V$ against $R_{beam}^{2}$ (keeping $i$ constant):

$\large \frac{e}{m_{e}} = -1.92 \times 10^{11} \pm 7\% \: C \ kg^{-1}$
