from math import *


def fi(x):
    return 1.0 / sqrt(2 * pi) * exp(-0.5*x**2)
    
    
def normpdf(x, mu=1.0, sigma=0.5):
    arg = (x - mu) / sigma
    return fi(arg) / sigma 



if __name__ == '__main__':
    from display import table
    from mathx import linspace
    table(normpdf, \
    	  linspace(-3, 4, 30))
