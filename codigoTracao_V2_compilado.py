# Importing all the libraries that will be used
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import re
import os
from os import listdir
from os.path import isfile, join

# Function responsible for reading a csv/txt file, given by the universal testing machine (may vary from machine to machine)
def getData(data):
    df = pd.read_csv(data, skiprows=9, skipfooter=37, delimiter='\t', engine='python')
    df.drop(columns=['index'], inplace=True)
    return df

# Function responsible for acquiring the area and the initial lenght (l0) of the tested material within the csv/txt file
def readParameters(data):
    with open(data) as f:
        arq = f.read()
    
    a = re.search(r'Area:\t(.+)', arq)
    gl = re.search(r'GaugeLength:\t(.+)', arq)
    area = float(a[1])
    l0 = float(gl[1])
    return area, l0

# Function responsible for plotting the Stress-Strain curve
def StrainStressCurve(x_axis,y_axis):
    fig, ax = plt.subplots()

    ax.plot(x_axis, y_axis, color='b')

    ax.set_xlabel('$\epsilon$ (mm/mm)')
    ax.set_ylabel('$\sigma$ (MPa)')
    ax.set_title('Strain-Stress Curve')
    ax.set_xlim([0, max(x_axis)+0.005])
    ax.set_ylim([0, max(y_axis)+100])
    ax.grid()

    plt.show()

# Function responsible for giving the basic properties that can be extrated from the Stress-Strain curve
# LTR, yield stress, Young's modulus, elongation and the Stress-Strain curve
def runMetalsAnalysis(area,l0,df):
    # Stress and Strain calculations
    df['Stress'] = df['Load(kN)']*1000/area #MPa
    df['Strain'] = df['Defor(mm)']/l0 # mm/mm
    
    # Plotting Stress-Strain curve
    StrainStressCurve(df['Strain'],df['Stress'])
    
    # UTS and elongation
    UTS = np.max(df['Stress'])
    elong = df['Strain'].iloc[df.index[df['Stress']==UTS]].tolist()[0]
    print('The UTS is {0} MPa'.format(round(UTS)))
    print('The elongation is {0}%'.format(elong*100))
    
    # Modulus of elasticity (Young's modulus) -- under review for optimization (automatization on the selection of the interval for making the regression)
    # defining the interval for making the regression (for calculating the Young's modulus)
    LowerLimit = 0 # Lower limit defined as zero, because, theoretically, the initial part of the curve is within the elastic region
    UpperLimit = float(input('Inform the upper limit, in MPa: ')) # For now, the upper limit of the elastic region is informed manually, roughly by looking to the Stress-Strain curve
    
    elastic_LowerLimit = df.index[df['Stress']>LowerLimit].tolist()
    elastic_UpperLimit = df.index[df['Stress']>UpperLimit].tolist()
    elastic_region = df.loc[elastic_LowerLimit[0]:elastic_UpperLimit[0]] # established the elastic region interval

    output_regression = linregress(elastic_region['Strain'], elastic_region['Stress']) # doing the regression
    E = output_regression[0] # The first item of the returned list is the Young's modulus
    #print(output_regression)
    print('The elastic modulus is {0} GPa'.format(round(E/1000)))
    
    # Yield Stress calculation
    stress_offset = E*(df['Strain']-0.002) # Conventional yield stress calculation (strain of 0,2%)

    f = df['Stress']
    g = stress_offset # Conventional yield strenght

    yieldStress_index = np.argwhere(np.diff(np.sign(f - g)))[0][0] # gets the index of intesection between the stress offset and the Stress values of the testing (gets the first index of intersection)
    # np.sign(f-g) -> will make the difference between f and g, then will assign -1 (to negative values), 0 (when the difference equals zero) and 1 (when the number is positive)
    # np.diff(np.sign(f-g)) -> will make the subtraction of np.sign(f-g)[i+1] with np.sign(f-g)[i], np.sign(f-g) will return an array
    # np.argwhere(np.diff(np.sign(f-g))) -> will find the indexes that are non zero 
    # because of np.sign, the points are -1, 0 or 1, when the convetional yield stress touches the stress-strain curve, np.diff will return an array full of zeros and the numbers will be the point of intersection
    # then, np.argwhere will find the indexes that are non zero
    yieldStress = df['Stress'][yieldStress_index] # getting the yield stress value
    
    print('The yield stress is {0} MPa'.format(round(yieldStress)))

    return 

# Here runs it all, it will read the text/csv file from a paste called "data"
# Inside this paste, it will open another paste (or pastes) and then read the text file and return the properties with the Stress-Strain curve
# This part of the code funtions like this: will run until every single file inside every single paste inside the data paste is read and processed
rootdir = r'C:\Users\gfa19\Desktop\Arquivos_Para_Python\codigoTracao_V2\data' # Here is the path that leads to my 'data' paste (personalize it to attend to your local paste)

for diretorio in os.listdir(rootdir):
    d = os.path.join(rootdir, diretorio)
    if os.path.isdir(d):
        print(d)
        path = d
        files = [f for f in listdir(path) if isfile(join(path, f))]
        print(files)
        for arquivo in files:
            print('\narquivo: {0}\n'.format(arquivo))
            dfx = getData(path+'\\'+arquivo) 
            area,l0 = readParameters(path+'\\'+arquivo)
            runMetalsAnalysis(area,l0,dfx)
            print()