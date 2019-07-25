import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# These are just sample numbers, the actual data needs to be inputted once found 
x = np.random.normal(size=1000)
y = x * 3 + np.random.normal(size=1000)

# Calculate the point density
xy = np.vstack([x,y])
z = gaussian_kde(xy)(xy)

fig, ax = plt.subplots()
ax.scatter(x, y, c=z, s=100, edgecolor='')
plt.show()
