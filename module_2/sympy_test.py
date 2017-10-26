from sympy import *
import math
import numpy as np
import matplotlib
import pandas

init_printing()

# %%
np.arccos(-1)

# %%
sqrt(2)
cos(0)

# %%
acos(-1)
acos(Rational(1 / 2))

from fractions import Fraction

acos(Fraction(1, 2))

print(math.pi)
# %%
sqrt(18)

# %%
math.sqrt(18)

# %%
alpha, beta, gamma = symbols('alpha, beta, gamma')

log(alpha**beta) + gamma

# %%
x, y = symbols('x, y')

y + sin(x)**y

# %%
mu, sigma = symbols('mu, sigma')

mu + sigma

exp((-(x - mu)**2)/sigma)


def squares(n, accumulator=3):
    if n == 1:
        return n + accumulator
    return squares(n - 1, accumulator + 2)
