
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def dft_partials(x, y):
    """
    Get the discrete Fourier transform of the series x + iy.
    Args
    ----
        x: (numpy vector) time series of x-coordinates
        y: (numpy vector) time series of y-coordinates

    Return
    ------
        S: (n x n) numpy  matrix. Each column m gives 
                  coeff**exp(exp(2 * np.pi * 1j * m * k / n) / n
           where different frequency terms are in rows. 
           Columns correspond to indicies of points of the 
           original series (e.g. time).
    """

    
    n = x.size
    a = x + 1j * y
    # Calcuate FFT
    A = np.fft.fft(a, n)
    ## Compute inverse fourier transform by hand
    k = np.linspace(0, n - 1, num = n)
    S = np.zeros((n, n)) + 1j
    for m in range(0, n):
        S[:, m] = A * np.exp(2 * np.pi * 1j * m * k / n) / n
    return S


def animate_dft(x, y):
    """
    Animate the fourier representation of the (x,y) series
    Args
    ----
        S: S matrix from dft_partials
        x: x component of series to plot
        y: y component of series to plot
    Return
    ------
        anim_path: file path of output mp4 of animation
    """
    def animate_frame(num, Q, S, line, x, y):
        """
        Args
        ----
        num: frame number
        Q: quiver plot object
        S: S matrix from dft_partials
        line: line plot object
        x: x component of series to plot
        y: y component of series to plot
        """

        # Set quivers
        U, V, X, Y = s2uvxy(S, num)
        Q.set_UVC(U, V)
        Q.set_offsets(np.transpose(np.vstack((X, Y))))
        # Set line
        line.set_data(x[0:num], y[0:num])
        return Q, line

    def s2uvxy(S, num):
        U = S[:, num].real
        V = S[:, num].imag
        X = np.cumsum(U)
        Y = np.cumsum(V)
        X = np.append(0, X)
        Y = np.append(0, Y)
        X = X[:-1]
        Y = Y[:-1]
        return U, V, X, Y

    n = np.size(x)
    # Get partial sums of dft 
    S = dft_partials(x, y)

    # Start of figures
    fig, ax = plt.subplots(1, 1)
    # Add line
    abs_lim = np.max(np.abs(np.cumsum(S, 0)))
    # abs_lim = np.max(np.abs([x,y]))
    plt.xlim(-abs_lim, abs_lim)
    plt.ylim(-abs_lim, abs_lim)

    # ax.axis('equal')
    line, = ax.plot([], [], lw=2)

    U, V, X, Y = s2uvxy(S, 0)
    # Add quivers
    Q = ax.quiver(X, Y, U, V, angles='xy', units='xy', scale_units='xy', scale=1)

    anim = animation.FuncAnimation(fig,
                                animate_frame,
                                fargs=(Q, S, line, x, y),
                                interval=50,   # ms between frames
                                frames=n,
                                blit=True)
    fig.tight_layout()
    return anim
    

