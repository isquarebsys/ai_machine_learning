# Import what you need
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Set the data
data = pd.DataFrame({
    'length': [94, 74, 147, 58, 86, 94, 63, 86, 69, 72, 128, 85, 82, 86, 88, 72, 74, 61, 90, 89, 68, 76, 114, 90, 78],
    'weight': [130, 51, 640, 28, 80, 110, 33, 90, 36, 38, 366, 484, 80, 83, 70, 61, 54, 44, 106, 84, 39, 42, 197, 102,
               57]
})

# Get the linear models. this uses np.polyfit and results in two coefficients
# These are essentially a multiple and a bias
linear_model = np.polyfit(data.length, data.weight, 1)

# calculate the y values based on the co-efficients from the model
r_x, r_y = zip(*((i, i * linear_model[0] + linear_model[1]) for i in data.length))

# Put in to a data frame, to keep is all nice
linear_model_plot = pd.DataFrame({'length': r_x,'weight': r_y})

# Plot the data
fig, axes = plt.subplots(nrows=1, ncols=2)

# Plot the original data and model
data.plot(kind='scatter', color='Red', x='length', y='weight', ax=axes[0], title='Data as Such')
linear_model_plot.plot(kind='line', color='Green', x='length', y='weight', ax=axes[0],title='Linear Regressed')

plt.show()
