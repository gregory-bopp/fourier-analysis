import numpy as np
import fourier as fr

# Lissajous Curve parameters
# See: https://en.wikipedia.org/wiki/Lissajous_curve
# The appearance is highly sensitive to the ratio a/b

sec = 10        # Duration of animation in seconds
n = 500         # Number of points to use
A = 3           # x amplitude
B = 3           # y amplitude
a = 1           # x frequency
b = 3           # y frequency
delta = np.pi/2

# Generate input series
theta = np.linspace(1/n, 2*np.pi, num=n)
x = A * np.sin(a*theta + delta)
y = B * np.sin(b*theta)

# Animate the result
anim = fr.animate_dft(x, y)
anim.save(anim_path='fig/lissajous.gif', fps=n/sec)

