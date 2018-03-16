from math import *


def fi(x):
    return 1.0 / sqrt(2 * pi) * exp(-x**2)
    
    
def normpdf(x, mu=1.0, sigma=0.5):
    pass


if __name__ == '__main__':
    from display import table
    table(fi, xrange(-5, 5))
