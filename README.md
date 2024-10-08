# Pyhton code to obtain Strain-Stress curve and properties 

This project started with the necessity to automate the process of plotting Strain-Stress curves and obtaining the properties of the material tested 
on the universal testing machine, specifically metallic materials.

## Index
- [Introduction](#introduction)
- [Usage](#usage)
- [Examples-of-output](#examples-of-output)
- [Contribution](#contribution)
- [License](#license)
- [Contact](#contact)

## Introduction
This project is an application that reads the text file obtained from the universal testing machine ([example of the text file](ExampleTextFile_1020steel_annealed_700_2h.txt)) extracting the data, using Pandas, and other necessary elements (area and gauge length), using RegEx. The output will be the 
UTS (Ultimate Tensile Strength), True UTS, Elongation, elastic and plastic elongation, Young's modulus (or elastic modulus), Yield Stress, the Engineering Strain-Stress curve and True Stress-Strain curve (plotted using MatPlotLib), and Toughness 

The Young's modulus is obtained using the 'linregress' function of scipy.stats. Therefore, using the previously calculated Young's modulus, the 
Yield Stress is obtained with the conventional yield stress calculation (strain of 0,2%).

To calculate the values for plotting the True Strain-Stress curve and to obtain the True UTS it was used the following formulas:

$$\sigma_t = \sigma_e \cdot (1 + \epsilon_e)\$$

$$\epsilon_t = \log(1+\epsilon_e)\$$

Where:

$\sigma_e\$ = Engineering Stress, $\sigma_t\$ = True Stress, $\epsilon_e\$ = Engineering Strain, $\epsilon_t\$ = True Strain.

To calculate the toughness of the material, it was used numerical methods for integration to obtain the area under the curve. It was necessary to choose the most appropriate method for the Strain-Stress curve, considering the irregularities that can be present in the graph, which was the Trapezoidal Rule. This method calculates the area of a trapezoid between a point and the previous point, which is better for grasping sudden changes in the curve.

## Usage

To use this project, there are a few things to clarify before using it and having a smooth experience.

1) The text file that the code was based on is the output from the Universal Testing Machine from my University, UTFPR-Londrina, therefore, be
   careful with the format of the text file that the code will read. The functions 'getData' and 'readParameters' may be altered depending on
   the text file being used.
2) The function 'runMetalsAnalysis' receives the DataFrame (referred to as df) with the columns Load (in kilonewtons, kN), Deformation (in
   millimeters, mm), Stroke (in millimeters, mm) and Time (in seconds, s) (Observation: the index column is dropped in the 'getData' function).
   However, only the Load and Deformation columns matter to the function, so be careful with the measurement units of the code and your text
   file.
3) The paste that the code will read the text files is referred to as 'data' (recommended name). The code will open the 'data' paste, then it will open
   each paste inside of it to read the text files. In conclusion, the text files have to be inside of a paste, that has to be placed inside the 'data' paste
   to the code to function. This way you can group your text files, separating them into categories (different pastes inside the paste 'data').
4) Related to the previous item, you must copy the path of your 'data' paste (from your computer) and paste it at the variable
   'rootdir' in the code, so the code can access your text files.
5) When running the code, the code will plot the Strain-Stress curve and return the UTS and elongation. After this, a prompt will appear asking
   you to give the upper limit of the elastic region, which can be informed roughly by looking at the plotted curve (answer in MPa). For now, it's
   done manually this step. With the upper limit informed, the output will give you the Young's modulus and the Yield Stress.

## Examples-of-output

![Exemplo_output_codigoTracao](ExampleOfOutput_1.png)
![Exemplo_output_codigoTracao2](ExampleOfOutput_2.png)

## Contribution

Contributions are welcome! Please follow these steps to contribute:

1. Fork the project.
2. Create a branch for your feature or bug fix:
    ```sh
    git checkout -b my-feature
    ```
3. Commit your changes:
    ```sh
    git commit -m "Add a new feature"
    ```
4. Push to the branch:
    ```sh
    git push origin my-feature
    ```
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [License](License) file for more details.

## Contact

Gabriel Favareto De Almeida - [LinkedIn](https://www.linkedin.com/in/gabriel-de-almeida-181701234/) - gabicubber@gmail.com
