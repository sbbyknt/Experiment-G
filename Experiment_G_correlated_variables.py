import numpy as np
import uncertainties

data = {
    #all of these values are in SI units
    #of form "variableName": (value, uncertainty)
    "a": (0.75, 0.001),
    "b": (0.01914, 0.00001),
    "T_P": (6.77, 0.006933),
    "T_B": (7.8045, 0.032421),
    "I": (0.9222014617, 0), #I[-1] will need to be assigned
    "g": (9.830302078, 0), #we want to find g[-1]
    "M_P": (2.0864, 0.0001),
    "M_B": (2.1195, 0.0001),
    "h": (0.6375, 0.02236),
    "T": (1.66867, 4.18699E-4)
}
