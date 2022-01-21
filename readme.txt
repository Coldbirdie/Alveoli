Authors
Jelmer Stoker en Luka Stein
Date
20-01-2022
Version
1.00


Name
Diffusion in alveoli


Description
This project displays an animation of carbondioxide and oxygen that diffuse through an alveoli in the lungs. 
Afterwards O2 binds to hemoglobine in a red bloodcell. The redblood cell will move to a cell, whereafter O2 will unbind
and enter a cell. In order to create ATP(adenosine triphosphate) a molecule that carries energy, O2 reacts with glucose. 
After the reaction CO2, H2O and ATP are formed, CO2 isn't needed so it leaves the cell. Futhermore the CO2 will dissolve into
blood plasma, but also binds for a small amount to hemoglobine in a red bloodcell.
 Finally the red bloodcell with CO2 inside of it will move towards an alveoli, to conclude the cyclus.

The projects consists of three scripts: the main script(main.py),
a cell object script(cel.py) and a blood vessel object script(bloodvessel.py). 
These objects scripts are imported and used in the main script. Also
there are four pdb files imported, these are molecules such as : water, oxygen, carbondioxide and glucose

The main function called 'respiration' in main.py consist of several sub-functions. In these sub-functions, objects take steps(to move).
Afterwards the steps are assigned to a devision of frame periods, e.g. 40 to 50 is a frame period. Each period gets assigned to
the corresponding sub-function in chronological order


Installation
For this code you need different programs. First of all this code is written in python.
The animation is made in povray, so you also need povray. The translation between python and 
povray is done with pypovray. So first of all you need to download python, 
after you have downloaded python you need to download povray (the program that makes the images).
If you downloaded povray you automatically have pypovray the program, that translates python to povray.

For the download of povray it's also recommended that you have a linux system. 
You could also download it on a windows system, but this is not recommended.
In this project there are newly created pdb files, these are not brought within the default package.
The pdb files are included in the .zip map. First open the pypovray folder, inside the folder there
should be a folder called 'pdb'. Once you've opened this folder, 
drag the .pdb files you've gotten from the .zip map into it. 
Futhermore we've used the following website to acquire a glucose molecule pdb file:
https://ww2.chemistry.gatech.edu/~lw26/structure/small_molecules/index.html

As for the final step, the duration 
length of the video must be adjusted to 12 seconds since that's the length required to run this animation.
Likewise as for the location of the pdb folder, there can be found file named default.ini. Open the file, search
for the title [SCENE] and change the duration to 'duration = 12'.

Requirements:
1: Python 3.9.2
2: POVray 3.7.0
3: Pypovray (git pull 18 November 2021)
recommended:
1: linux system 11


Usage
First go to where the scripts are located, by typing in the linux terminal the following command line:
 - cd folder pypovray
 - e.g. cd project/pypovray
In order to adjust a file, type the following command line:
 - nano script.py
 - e.g. nano main.py
To run the script, type the following command line:
 - python3 script.py
 - e.g. python3.py


Support
If you need help you can mail to:
 - jelmerstoker04V2@gmail.com 
 - luka.stein020@gmail.com 


Authors and acknowledgment
We want to thank R.Wedema and L.Oldhoff for helping us when we got stuck while coding and 
for providing us the essential materials we needed to complete our scripts


