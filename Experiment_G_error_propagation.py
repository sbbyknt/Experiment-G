import numpy as np

#well within bit limits here, so do not need to consider numerical error

data = {
    #all of these values are in SI units
    "a": 0.75,
    "D a": 0.001,
    "b": 0.01914,
    "D b": 0.00001,
    "T_P": 6.77,
    "D T_P": 0.006933, 
    "T_B": 7.8045,
    "D T_B": 0.032421, 
    "I": 0.9222014617, 
    "D I": 0, #will need to be assigned by calling below function
    "g": 9.830302078,
    "D g": 0, #what we want to find
    "M_P": 2.0864,
    "D M_P": 0.0001,
    "M_B": 2.1195,
    "D M_B": 0.0001,
    "h": 0.6375,
    "D h": 0.02236, 
    "T": 1.66867,
    "D T": 4.18699E-4
}

def find_delta_I():
    component1 = ((data["T_P"]/data["T_B"])**2 * ((data["a"] ** 2)/12 + (data["b"] ** 2)/12) * data["D M_B"]) ** 2
    component2 = ((data["T_P"]/data["T_B"])**2 * ((2 * data["M_B"] * data["a"])/12) * data["D a"])**2 
    component3 = ((data["T_P"]/data["T_B"])**2 * ((2 * data["M_B"] * data["b"])/12) * data["D b"])**2 
    component4 = (((2 * data["T_P"])/(data["T_B"] ** 2)) * ((data["M_B"] * data["a"] ** 2)/12 + (data["M_B"] * data["b"] ** 2)/12) * data["D T_P"])**2
    component5 = (((-2 * (data["T_P"] ** 2))/(data["T_B"] ** 3)) * ((data["M_B"] * data["a"] ** 2)/12 + (data["M_B"] * data["b"] ** 2)/12) * data["D T_B"])**2
    component6 = (data["h"] ** 2 * data["D M_P"]) ** 2
    component7 = (2 * data["M_P"] * data["h"] * data["D h"])**2

    return np.sqrt(component1+component2+component3+component4+component5+component6+component7)


def find_delta_g():
    component1 = ((4 * np.pi ** 2)/(data["M_P"] * data["h"] * (data["T"] ** 2)) * data["D I"]) ** 2
    component2 = ((-4 * np.pi ** 2 * data["I"])/(data["M_P"] ** 2 * data["h"] * data["T"] ** 2) * data["D M_P"]) ** 2
    component3 = ((-4 * np.pi ** 2 * data["I"])/(data["M_P"] * data["h"] ** 2 * data["T"] ** 2) * data["D h"]) ** 2
    component4 = ((-8 * np.pi ** 2 * data["I"])/(data["M_P"] * data["h"] * data["T"] ** 3) * data["D T"]) ** 2

    return (component1 + component2 + component3 + component4) ** 0.5

data["D I"] = find_delta_I()

print(find_delta_g())