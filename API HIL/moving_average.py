import json
import numpy as np


def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]

    return ret[n - 1:] / n

#Read the profile file
with open('profiles.json') as json_file:
    profiles = json.load(json_file)

irradiance = profiles['irradiance']
print(irradiance)

new_irradiance = moving_average(irradiance,n=5)
print(new_irradiance)






