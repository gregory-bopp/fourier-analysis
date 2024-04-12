import numpy as np
import matplotlib.pyplot as plt
from fourier.spectral_derivative import spectral_derivative_1d

# Define function
def f(x):
    return np.exp(-x**2)

# Define domain and buffer
n_buffer = 1000
N = 10000 + n_buffer * 2
L = 10
xt = np.linspace(-L/2, L/2, N, endpoint=False)
Ft = f(xt)

# Calculate k=3 spectral derivatives of f(x)
dFdxt = spectral_derivative_1d(Ft, L)

# Remove buffer for plotting
x = xt[(n_buffer):-(n_buffer)]
F = Ft[(n_buffer):-(n_buffer)]
dFdx = dFdxt[(n_buffer):-(n_buffer)]

# Plot result
plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(x,F)
plt.subplot(1,2,2)
plt.plot(x,dFdx)
plt.show()


