import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from fourier import fft_convolve

# Hat function
def hat(n1,n2,n3):
    n = n1 + n2 + n3
    return np.concatenate([np.zeros(n1), np.ones(n2), np.zeros(n3)])  

# Plotting function
def plot_row(*args, extent=None, cmap='virids'):
    fig, axes = plt.subplots(1, len(args), figsize=(6*len(args), 5))
    for ax, arg in zip(axes, args):
        a = ax.plot(arg[0])
        ax.set_xlabel("$x$")
        ax.set_ylabel("$y$")
        ax.set_title(arg[1])
    fig.tight_layout()


if __name__ == "__main__":

    # Define signals to convolve
    s1 = hat(10,10,10)
    s2 = hat(10,10,10)
    
    # Mode to use for convolution (domain of output)
    mode = "same"

    # Perform manual convolution with FFT
    s3 = fft_convolve(s1, s2, mode)
    # Numpy non-FFT convolution
    s4 = np.convolve(s1,s2, mode)
    # Scipy FFT-based convolution
    s5 = signal.fftconvolve(s1,s2,mode)

    # Check differences between standard implementations
    print("manual - numpy: {}".format(np.max(np.abs(s3 - s4))))
    print("manual - scipy: {}".format(np.max(np.abs(s3 - s5))))

    # Plot the Original Signals and Convolution   
    plot_row((s1, 'Signal 1'),
             (s2, 'Signal 2'),
             (s3, 'Manual fft_convolve'),
             (s4, 'numpy.convolve'),
             (s5, 'scipy.signal.fftconvolve'))
    
    plt.show()
