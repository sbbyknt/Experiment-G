import numpy as np
from uncertainties import ufloat

data = {
    #all of these values are in SI units
    #of form "variableName": (value, uncertainty)
    "a": ufloat(0.75, 0.001),
    "b": ufloat(0.01914, 0.00001),
    "T_P": ufloat(6.77, 0.007),
    "T_B": ufloat(7.80, 0.03),
    "M_P": ufloat(2.0864, 0.0001),
    "M_B": ufloat(2.1195, 0.0001),
    "h": ufloat(0.64, 0.02),
    "T": ufloat(1.6687, 4E-4)
}

I = data["M_B"]/12 * (data["a"]**2 + data["b"]**2) * (data["T_P"]/data["T_B"])**2 + data["M_P"] * data["h"]**2
g = 4*np.pi**2 * I / (data["M_P"] * data["h"] * data["T"]**2)
print(g) #g=9.87+/-0.26

precision_in_g = g.std_dev/g.nominal_value
print(f"Precision in g: {precision_in_g}")

if precision_in_g < (1/1000):
    print("Desired level of precision met")
else:
    print("Desired level of precision not met")