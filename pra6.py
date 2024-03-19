# Convert 2D np Array to 1d np array.
import numpy as np
twoD= np.array([[1,2,3],[9,8,7]])

to_oneD=twoD.reshape(-1)
print(to_oneD)
print(to_oneD.ndim)