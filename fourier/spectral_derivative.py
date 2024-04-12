import numpy as np

def spectral_derivative_1d(f, L):
    """Calculate the spectral derivative of a 1-dimensional function, f, 
    that is defined over domain (-L/2, L/2).

    Args:
        f (np.ndarray): 1-dimensional array of real or complex valued numbers of function 
        at input locations evenly spaced between (-L/2,L/2)
        L (np.double): interval width of input domain (-L/2, L/2)

    Returns:
        np.ndarray: 1-dimensional array of same length as f. Spectral derivative of f(x) w.r.t. x
    """    

    # Calculate size in x and y dimensions
    N = len(f)

    # Take the Fourier transform
    f_hat = np.fft.fft(f)

    # Define the wave numbers
    omega = np.fft.fftfreq(N, L/N)
    
    # Calculate the spectral derivative
    dfhat_dx = 1j * omega * f_hat

    # Take the inverse Fourier transform
    return np.fft.ifft(dfhat_dx).real

def spectral_derivative_2d(f, Lx, Ly):
    """Calculate the spectral derivative of a 2-dimensional function, f, 
    that is defined over domain (-L/2, L/2).

    Args:
        f (np.ndarray): 1-dimensional array of real or complex valued numbers of function 
        at input locations evenly spaced between (-L/2,L/2)
        L (np.double): interval width of input domain (-L/2, L/2)

    Returns:
        Tuple: spectral gradient of f: df/dx, df/dy
            np.ndarray: df/dx, 2-dimensional array of same shape as f
            np.ndarray: df/dy, 2-dimensional array of same shape as f
    """    

    # Calculate size in x and y dimensions
    Nx,Ny = f.shape

    # Take the Fourier transform
    f_hat = np.fft.fft2(f)

    # Define the wave numbers
    kx = np.fft.fftfreq(Nx, Lx/Nx)
    ky = np.fft.fftfreq(Ny, Ly/Ny)
    KX, KY = np.meshgrid(kx, ky)


    # Calculate the spectral derivative
    df_hat_dx = 1j * KX * f_hat
    df_hat_dy = 1j * KY * f_hat

    # Take the inverse Fourier transform
    df_dx = np.fft.ifft2(df_hat_dx).real
    df_dy = np.fft.ifft2(df_hat_dy).real

    return df_dx.real, df_dy.real
    

