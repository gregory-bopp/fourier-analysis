# Manual convolution with FFT
def fft_convolve(f1, f2, mode = "full"):  
    """Convolve two signals using FFT

    Args:
        f1 (np.array): 1-d array. Signal 1
        f2 (np.array): 1-d array. Signal 2
        mode (str, optional): _description_. Defaults to "full".

    Returns:
        array: 1-d array containing the convolution between f1 and f2
    """
    import numpy as np

    _modedict = {'same': 1, 'full': 2}
    try:
        _ = _modedict[mode]
    except KeyError as e:
        raise ValueError("Acceptable mode flags are "
                         " 'same' or 'full'.") from e

    # Compute the size of the full output signal
    full_size = len(f1) + len(f2) - 1
    
    # Compute the next power of 2 geq output size
    fft_size = 2 ** int(np.ceil(np.log2(full_size)))
    
    # FFT of each signal
    fft_f1 = np.fft.fft(f1, fft_size)
    fft_f2 = np.fft.fft(f2, fft_size)
    
    # Take Element-wise multiplication in the frequency domain and inverse FFT
    convolved = np.fft.ifft(fft_f1 * fft_f2)
    convolved = convolved[:full_size]

    if mode == "same":
        output_size = max(len(f1), len(f2))
        trunc = (full_size - output_size)//2
        convolved = convolved[trunc:-trunc]
        # Truncate if output should be odd
        if output_size%2==0:
            convolved=convolved[:-1]

    # else mode == "full"
    
    return np.real(convolved)
