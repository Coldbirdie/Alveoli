# Imports
from vapory import Pigment, Cylinder, Torus, Isosurface, ContainedBy, Box, POVRayElement

class Function(POVRayElement):
    # Class required to run iso functions
    """ Function()"""

def bloodvessels():
    """ 4 blood vessels are created. Two are vertical and two are horizontal.
     There are also 4 curved parts to connect the blood vessels """
    cylinders = {
        # Blood vessels straight
        'cylinder1_v' : Cylinder([8, 21, 0], [8, -2, 0], 3, Pigment('color', [1, 0, 0], 'filter', 0.7)),
        'cylinder2_h' : Cylinder([4 , -6, 0], [-36, -6, 0], 3, Pigment('color', [1, 0, 0], 'filter', 0.7)),
        'cylinder3_v' : Cylinder([-40, 20, 0], [-40, -2, 0], 3, Pigment('color', [1, 0, 0], 'filter', 0.7)),
        'cylinder4_h' : Cylinder([4 , 24, 0], [-36, 24, 0], 3, Pigment('color', [1, 0, 0], 'filter', 0.7)),
        
        # Blood vessels curved
        'isosurface1_b' : Isosurface(Function('f_torus(x, y, z, 4.0,  3.0)'),
                       ContainedBy(Box([0, -10, 0], [10, 10, 10])), 'rotate', [90, 0, 0], 'translate', [4, -2, 0], Pigment('color', [1, 0, 0], 'filter', 0.7)),
                       
        'isosurface2_b' : Isosurface(Function('f_torus(x, y, z, 4.0,  3.0)'),
                       ContainedBy(Box([-10, -10, 0], [0, 10, 10])), 'rotate', [90, 0, 0], 'translate', [-36, -2, 0], Pigment('color', [1, 0, 0], 'filter', 0.7)),
        
        'isosurface3_b' : Isosurface(Function('f_torus(x, y, z, 4.0,  3.0)'),
                       ContainedBy(Box([-10, -10, -10], [0, 10, 0])), 'rotate', [90, 0, 0], 'translate', [-36, 20, 0], Pigment('color', [1, 0, 0], 'filter', 0.7)),
                       
        'isosurface4_b' : Isosurface(Function('f_torus(x, y, z, 4.0,  3.0)'),
                       ContainedBy(Box([0, -10, 0], [10, 10, -10])), 'rotate', [90, 0, 0], 'translate', [4, 20, 0], Pigment('color', [1, 0, 0], 'filter', 0.7)),
        }

    # Take values Cylinder_1_2_3_4.. and Isosurface_1_2_3_4.. from dictionary 'cylinders'. The values are assigned to list 'coordinates' 
    coordinates = list(cylinders.values())
    return coordinates


# Close function
bloodvessel = bloodvessels()


