#!/usr/bin/env python3

"""
This script simulates the diffusion process of O2 and CO2 in an alveoli and the creation of ATP correlating to the process
"""

# Credits
__author__ = ' L. T. Stein & J. Stoker '
__version__ = 1.00
__date__ = 20 - 1 - 2022

# Imports
from pypovray import pypovray, pdb, SETTINGS
from vapory import Scene, Pigment, Camera, LightSource, Sphere, Cylinder, Isosurface, ContainedBy, Box, POVRayElement, Text, Background
from bloodvessel import bloodvessel
from cel import cel



def variables():
    """ The molecules; O2, CO2, H2O and C6H12O6 are imported as pdb files and are put as global objects """
    global OXYGEN, CARBONDIOX, CARBONDIOX2, WATER, GLUCOSE, ATP
    # Pdb molecules
    OXYGEN = pdb.PDBMolecule('{}/pdb/o2.pdb'.format(SETTINGS.AppLocation), center=True)
    CARBONDIOX = pdb.PDBMolecule('{}/pdb/co2.pdb'.format(SETTINGS.AppLocation), center=False, offset=[7, 25, 0])
    CARBONDIOX2 = pdb.PDBMolecule('{}/pdb/co2.pdb'.format(SETTINGS.AppLocation), center=False, offset=[-15, 1, 0])
    WATER = pdb.PDBMolecule('{}/pdb/water.pdb'.format(SETTINGS.AppLocation), center=False, offset=[-13.5, 1, 0])
    GLUCOSE = pdb.PDBMolecule('{}/pdb/d_glucose.pdb'.format(SETTINGS.AppLocation), center=False, offset=[-15, 1, 0])



class Function(POVRayElement):
    # Class required to run iso functions
    """ Function()"""


def respiration(step):
    """ Sub_functions consist of objects taking steps. 
    These functions/ objects are later assigned to the frames of the diffusion animation """
    # Checker
    cell = False
    # Alveoli
    cylinder = Cylinder([0, 3.5, 0], [0, 20, 0], 0.5, Pigment('color', [0, 0, 1]))
    alveoli = Sphere([0, 2, 0], 5, Pigment('color', [0, 0, 1], 'filter', 0.7))
    # Scenery objects
    light = LightSource([0, 2, -10], 1.0)
    camera = Camera('location', [0, 0, -25], 'look_at', [0, 0, 0])
    environment = Background('color', [0.02,0.02,0.02])
    
    
    def f0_40():
        """ A red bloodcell moves into the scene through a blood vessel and stops next to an alveoli """
        # Red bloodcell
        bloodcell_in = Cylinder([8, 25 - (step * 0.625), 0], [8, 25 - (step * 0.625), 0.1], 2,Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate',
        [8, 25 - (step * 0.625), 0], Pigment('color', [1, 0, 0]))
        if step > 39:
            bloodcell_in = Cylinder([8, 0, 0], [8, 0, 0.1], 2, Pigment('color', [1, 0, 0]))
            bloodcell_out = Isosurface(
            Function('f_torus(x, y, z, 1.6,  0.4)'),
            ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [8, 0, 0], Pigment('color', [1, 0, 0]))
        return bloodcell_in, bloodcell_out

    def f40_50():
        """ CO2 goes out of a red bloodcell and moves into an alveoli,
         O2 diffuses through the the alveoli's tissue into a redblood cell """
        OXYGEN.move_to([0, -0.6 *(step - 39), 0])
        CARBONDIOX.move_to([8 - (0.8 * (step - 39)), 0, 0])

    def f50_60():
        """ The red bloodcell moves next to alvioli through a blood vessel """
        # Red bloodcell
        bloodcell_in = Cylinder([8, 0 - (0.6 * (step - 49)), 0], [8, 0 - (0.6 * (step - 49)), 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [8, 0 - (0.6 * (step - 49)), 0], Pigment('color', [1, 0, 0]))
        return bloodcell_in, bloodcell_out

    def f60_70():
        """ The red bloodcell goes under the alveoli """
        # Red bloodcell  
        bloodcell_in = Cylinder([8 - (0.8 *(step - 59)) , -6, 0], [8 - (0.8 *(step - 59)) , -6, 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [8 - (0.8 *(step - 59)) ,-6 , 0], Pigment('color', [1, 0, 0]))
        return bloodcell_in, bloodcell_out
        
    def f70_80():
        """ O2 diffuses through the alveoli and goes into the red bloodcell. Inside the bloodcell O2 binds with hemoglobine """
        # Red bloodcell
        bloodcell_in = Cylinder([0, -6, 0], [0, -6, 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [0,-6 , 0], Pigment('color', [1, 0, 0]))
        # O2
        OXYGEN.move_to([0, -6, 0 + (0.5 * (step - 69))])
        return bloodcell_in, bloodcell_out
        
    def f80_100():
        """ The red bloodcell moves along with the camera towards a cell """ 
        # Camera
        camera = Camera('location', [0 - (1.5 * (step - 79)), 0, -25], 'look_at', [0 - (1.5 * (step - 79)), 0, 0])
        # Red bloodcell
        bloodcell_in = Cylinder([0 - (1.5 * (step - 79)), -6, 0], [0 - (1.5 * (step - 79)), -6, 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [0 - (1.5 * (step - 79)), -6, 0], Pigment('color', [1, 0, 0]))
        # O2
        OXYGEN.move_to([0 - (1.5 * (step - 79)), -6, 5])
        return camera, bloodcell_in, bloodcell_out
    
    def f100_120():
        """ The camera and red bloodcell stop at the cell, O2 unbinds and enters the cell """
        # Camera
        camera = Camera('location', [-30, 0, -25], 'look_at', [-30, 0, 0])
        # Red bloodcell
        bloodcell_in = Cylinder([-30, -6, 0], [-30, -6, 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [-30, -6, 0], Pigment('color', [1, 0, 0]))
        # O2
        OXYGEN.move_to([-30, -6 , 5 - (0.25 * (step - 99))])
        return camera, bloodcell_in, bloodcell_out
        
    def f120_140():
        """ The camera and red bloodcell stop at the cell, O2 unbinds and goes futher into the cell """
        # Camera
        camera =  Camera('location', [-30, 0, -25], 'look_at', [-30, 0, 0])
        # Red bloodcell
        bloodcell_in = Cylinder([-30, -6, 0], [-30, -6, 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [-30, -6, 0], Pigment('color', [1, 0, 0]))
        # O2
        OXYGEN.move_to([-30, -6 + (0.45 * (step - 119)) ,0])
        return camera, bloodcell_in, bloodcell_out
        
    def f140_160():
        """ ATP is formed after O2 reacts with glucose"""
        # Camera
        camera = Camera('location', [-30, 0, -25], 'look_at', [-30, 0, 0])
        # Red bloodcell
        bloodcell_in = Cylinder([-30, -6, 0], [-30, -6, 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [-30, -6, 0], Pigment('color', [1, 0, 0]))
        # ATP + textlabel showing 'ATP'
        ATP = Cylinder([-32, 1, 0], [-32, 1, 0.1], 1.5, Pigment('color', [1, 0.65, 0]))
        text = Text('ttf', '"timrom.ttf"', '"{}"'.format(str('ATP')), 1, [0.1, 0, 0],'translate', [-33, 0.5, -1])
        return camera, bloodcell_in, bloodcell_out, ATP, text

    def f160_170():
        """ CO2 is formed after O2 reacted with glucose and moves towards the red bloodcell. ATP stays in the cell """
        # Camera
        camera = Camera('location', [-30, 0, -25], 'look_at', [-30, 0, 0])
        # Red bloodcell
        bloodcell_in = Cylinder([-30, -6, 0], [-30, -6, 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [-30, -6, 0], Pigment('color', [1, 0, 0]))
        # CO2
        CARBONDIOX2.move_to([-30, 1 - (0.7 * (step - 159)), 0])
        # ATP + textlabel showing 'ATP'
        ATP = Cylinder([-32, 1, 0], [-32, 1, 0.1], 1.5, Pigment('color', [1, 0.65, 0]))
        text = Text('ttf', '"timrom.ttf"', '"{}"'.format(str('ATP')), 1, [0.1, 0, 0],'translate', [-33, 0.5, -1])
        return camera, bloodcell_in, bloodcell_out, ATP, text

    def f170_180():
        """ A small portion of CO2 binds to hemoglobine in the red bloodcell and the majority of CO2 dissolves in the blood plasma """
        # Camera
        camera = Camera('location', [-30, 0, -25], 'look_at', [-30, 0, 0])
        # Red bloodcell
        bloodcell_in = Cylinder([-30, -6, 0], [-30, -6, 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [-30, -6, 0], Pigment('color', [1, 0, 0]))
        # ATP + textlabel showing 'ATP'
        ATP = Cylinder([-32, 1, 0], [-32, 1, 0.1], 1.5, Pigment('color', [1, 0.65, 0]))
        text = Text('ttf', '"timrom.ttf"', '"{}"'.format(str('ATP')), 1, [0.1, 0, 0],'translate', [-33, 0.5, -1])
        # CO2
        CARBONDIOX2.move_to([-30, -6 - (0.05 * (step - 169)), 0 + (0.25 * (step - 169))])
        return camera, bloodcell_in, bloodcell_out, ATP, text
        
    def f180_185():
        """ The red bloodcell and the binded CO2 start moving away from the cell. The camera moves along with them """
        # Camera
        camera = Camera('location', [-30 - (2 * (step - 179)), 0, -25], 'look_at', [-30 - (2 * (step - 179)), 0, 0])
        # Red bloodcell
        bloodcell_in = Cylinder([-30 - (2 * (step - 179)), -6, 0], [-30 - (2 * (step - 179)), -6, 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [-30 - (2 * (step - 179)), -6, 0], Pigment('color', [1, 0, 0]))
        # ATP + textlabel showing 'ATP'
        ATP = Cylinder([-32, 1, 0], [-32, 1, 0.1], 1.5, Pigment('color', [1, 0.65, 0]))
        text = Text('ttf', '"timrom.ttf"', '"{}"'.format(str('ATP')), 1, [0.1, 0, 0],'translate', [-33, 0.5, -1])
        # CO2
        CARBONDIOX2.move_to([-30 - (2 * (step - 179)), -6.5, 2.5])
        return camera, bloodcell_in, bloodcell_out, ATP, text
        
    def f185_200():
        """ The red bloodcell and the binded CO2 turn through bended parts of the blood vessel """
        # Camera
        camera = Camera('location', [-40, 0 + (2.03333333333333 * (step - 184)), -25], 'look_at', [-40, 0 + (2.03333333333333 * (step - 184)), 0])
        bloodcell_in = Cylinder([-40, -6.5 + (2.03333333333333 * (step - 184)), 0], [-40, -6.5 + (2.03333333333333 * (step - 184)), 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [-40, -6.5 + (2.03333333333333 * (step - 184)), 0], Pigment('color', [1, 0, 0]))
        ATP = Cylinder([-32, 1, 0], [-32, 1, 0.1], 1.5, Pigment('color', [1, 0.65, 0]))
        text = Text('ttf', '"timrom.ttf"', '"{}"'.format(str('ATP')), 1, [0.1, 0, 0],'translate', [-33, 0.5, -1])
        CARBONDIOX2.move_to([-40, -6.5 + (2.03333333333333 * (step - 184)), 2.5])
        return camera, bloodcell_in, bloodcell_out, ATP, text
        
    def f200_220():
        """ The red bloodcell and the binded CO2 keep moving along the blood vessel """
        # Camera
        camera = Camera('location', [-40 + (2.4 * (step - 199)), 30.5, -25], 'look_at', [-40 + (2.4 * (step - 199)), 30.5, 0])
        # Red bloodcell
        bloodcell_in = Cylinder([-40 + (2.4 * (step - 199)), 24, 0], [-40 + (2.4 * (step - 199)), 24, 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [-40 + (2.4 * (step - 199)), 24, 0], Pigment('color', [1, 0, 0]))
        # ATP + textlabel showing 'ATP'
        ATP = Cylinder([-32, 1, 0], [-32, 1, 0.1], 1.5, Pigment('color', [1, 0.65, 0]))
        text = Text('ttf', '"timrom.ttf"', '"{}"'.format(str('ATP')), 1, [0.1, 0, 0],'translate', [-33, 0.5, -1])
        # CO2
        CARBONDIOX2.move_to([-40 + (2.4 * (step - 199)), 24 , 2.5])
        return camera, bloodcell_in, bloodcell_out, ATP, text
    
    def f220_240():
        """ The red bloodcell and the binded CO2 move towards and arrive at an alveoli """
        # Camera
        camera = Camera('location', [8, 30.5 - (1.2 * (step - 219)), -25], 'look_at', [8, 30.5 - (1.2 * (step - 219)), 0])
        # Red bloodcell
        bloodcell_in = Cylinder([8, 24 - (1.2 * (step - 219)), 0], [8, 24 - (1.2 * (step - 219)), 0.1], 2, Pigment('color', [1, 0, 0]))
        bloodcell_out = Isosurface(
        Function('f_torus(x, y, z, 1.6,  0.4)'),
        ContainedBy(Box(-3, 3)), 'rotate', [90, 0, 0], 'translate', [8, 24 - (1.2 * (step - 219)), 0], Pigment('color', [1, 0, 0]))
        # ATP + textlabel showing 'ATP'
        ATP = Cylinder([-32, 1, 0], [-32, 1, 0.1], 1.5, Pigment('color', [1, 0.65, 0]))
        text = Text('ttf', '"timrom.ttf"', '"{}"'.format(str('ATP')), 1, [0.1, 0, 0],'translate', [-33, 0.5, -1])
        # CO2
        CARBONDIOX2.move_to([8, 24 - (1.2 * (step - 219)), 2.5])
        return camera, bloodcell_in, bloodcell_out, ATP, text
    
    # Assign variables to function 
    bloodcell_in, bloodcell_out = f0_40()

    # For each 'if' statement; if the step is greater than x(frames)_begin 
    # and if the step is smaller than x(frames)_end,
    # functions along with their contents are assigned to those step periods
    # according to the frames in the animation
    if step > 39:
        if step < 50:
            f40_50()

    if step > 50:
        if step < 60:
            bloodcell_in, bloodcell_out = f50_60()

    if step > 59:
        if step < 70:
            bloodcell_in, bloodcell_out = f60_70()
            
    if step > 69:         #nice
        if step < 80:
            bloodcell_in, bloodcell_out = f70_80()
            
    if step > 79:  
        if step < 100:
            camera, bloodcell_in, bloodcell_out = f80_100()     
    
    if step > 99:
        if step < 120:
            camera, bloodcell_in, bloodcell_out = f100_120()  
          
    if step > 119:
        if step < 140:
            camera, bloodcell_in, bloodcell_out = f120_140()
    
    if step > 139:
        if step < 160:
          camera, bloodcell_in, bloodcell_out, ATP, text = f140_160()
          cell = True

    if step > 159:
        if step < 170:
            camera, bloodcell_in, bloodcell_out, ATP, text = f160_170()
            cell = True

    if step > 169:
        if step < 180:
            camera, bloodcell_in, bloodcell_out, ATP, text = f170_180()
            cell = True
            
    if step > 179:
        if step < 185:
            camera, bloodcell_in, bloodcell_out, ATP, text = f180_185()
            cell = True
    
    if step > 184:
        if step < 200:
            camera, bloodcell_in, bloodcell_out, ATP, text = f185_200()
            cell = True
            
    if step > 199:
        if step < 220:
            camera, bloodcell_in, bloodcell_out, ATP, text = f200_220()
            cell = True
          
    if step > 219:
        if step < 240:
            camera, bloodcell_in, bloodcell_out, ATP, text = f220_240()
            cell = True

         
    # If the checker is false, then the scene is displayed without the imported cell object 
    if cell == False:
        # Return all the objects to the scene
        return Scene(camera,
                 objects=[light,environment, alveoli, cylinder, bloodcell_in, bloodcell_out] + OXYGEN.povray_molecule + bloodvessel +
                    CARBONDIOX.povray_molecule + cel + GLUCOSE.povray_molecule,
                 included=['functions.inc'])
                 
    # If the checker is true, then the imported cell object will also be displayed         
    if cell == True:
        return Scene(camera,
                # Return all the objects to the scene
                objects=[light,environment, alveoli, cylinder, bloodcell_in, bloodcell_out, ATP, text] + bloodvessel + cel + WATER.povray_molecule
                + CARBONDIOX2.povray_molecule,
                included=['functions.inc'])


if __name__ == '__main__':
    # Close function variables
    variables()
    # Render scene to mp4
    pypovray.render_scene_to_mp4(respiration)



