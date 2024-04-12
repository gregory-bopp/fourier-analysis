import numpy as np
import matplotlib.pyplot as plt
from fourier.spectral_derivative import spectral_derivative_2d

# Plotting function
def plot_image_row(*fields, extent=None, cmap='virids'):
    fig, axes = plt.subplots(1, len(fields), figsize=(6*len(fields), 5))
    for ax, field in zip(axes, fields):
        a = ax.imshow(field, extent=extent)
        ax.set_aspect("equal")
        ax.set_xlabel("$x$")
        ax.set_ylabel("$y$")
        fig.colorbar(a, ax=ax, cmap = cmap, location='bottom')

    return fig, axes
# Define function
def f(x,y):
    return np.exp(-(x**2 + y**2)/0.2)

# Define the range for x and y values
N = 200  # Number of points
Lx = 2   # Length of the domain in x-direction
Ly = 2   # Length of the domain in y-direction
x = np.linspace(-Lx/2, Lx/2, N, endpoint=False)
y = np.linspace(-Ly/2, Ly/2, N, endpoint=False)
X, Y = np.meshgrid(x, y)

# Calculate the function values
F = f(X, Y)
dF_dx, dF_dy = spectral_derivative_2d(F, Lx, Ly)

# Plot the image
plot_image_row(F, dF_dx, dF_dy, extent = (-Lx/2, Lx/2, -Ly/2, Ly/2))
plt.show()



