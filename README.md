# Pyhton code to obtain Strain-Stress curve and properties 

This project started with the necessity to automate the process of plotting Strain-Stress curves and obtaining the properties of the material tested on the universal testing machine, more specifically metallic materials.

## Index
- [Introduction](#introduction)
- [Use](#use)

## Introduction
This project is an application that, firstly, reads the text file obtained from the universal testing machine (example of the text file that 
the code was based on at the index) extracting the data, using Pandas, and other necessary elements (area and gauge lenght), using RegEx. The output will be the 
UTS (Ultimate Tensile Strength), Elongation, Young's modulus, the Yield Stress and the Strain-Stress curve, plotted using Matplotlib.

The Young's modulus is obtained using the 'linregress' function of scipy.stats. Therefore, using the previously calculated Young's modulus, the 
Yield Stress is obtained with the conventional yield stress calculation (strain of 0,2%).

## Use

To use this project, there are a few things to be noticed before using the code to have a smooth experience.

1) 
