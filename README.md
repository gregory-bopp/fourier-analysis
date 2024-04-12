# Applications of the Fourier Transform

This Python project explores various applications of the Fourier transform, including the spectral derivative and convolutions. The Fourier transform is a standard tool in signal processing, image processing, and many other fields, where signals are decomposed into their frequency components. Often a difficult calculation in a time or space domain can be made simpler in the frequency domain.

## Overview 
This project contains applications and visualizations that make use of Fourier-based methods. The python scripts and jupyter notebooks in the `applications` directory include overviews of the following:

1. **Discrete Fourier Transform Animation**: 
This module animates the discrete Fourier transform (DFT) of a complex sequence as described in this [3 Blue 1 Brown video](https://www.youtube.com/watch?v=r6sGWTCMz2k). 

- `applications/complex_dft/lissajous.py`: animation the DFT of a parametrically defined function: [Lissajous Curve](https://en.wikipedia.org/wiki/Lissajous_curve)

![](assets/lissajous.gif)

2. **Spectral Derivative**: Taking a numerical derivative of a function $f(x)$ can sometimes be more stable when operating in the frequency domain. If $\mathcal{F}(f)(x) \hat{f}(\omega)$, is the Fourier transform of a differentiable function $f(x)$, then $\mathcal{F}(f')(x) = i \omega \hat{f}(\omega)$.

3. **Convolution**: The convolution theorem says that under suitable conditions, convolution of two functions in the time domain is equivalent to pointwise multiplication in the frequency domain. 


## Installation
1. Clone the repository
```bash
git clone https://github.com/gregory-bopp/fourier-transform-python.git
```
2. Install the project dependencies
```bash
pip install -r requirements
```

3. Install project library
```bash
python -m pip install --upgrade setuptools
pip install fourier
```


# License

This project is licensed under the MIT License. See the LICENSE file for details.
