from vapory import Pigment, Sphere

def cel():
    """ A yellow cell is created and put into a variable """
    cel = {
    'sphere' : Sphere([-30, 3, 0], 6, Pigment('color', [1, 1, 0], 'filter', 0.7))
        }
    # Take value Sphere.. from dictionary 'cel'. The value is assigned to list 'cel'    
    cel = list(cel.values())
    return cel


# Close function
cel = cel()

