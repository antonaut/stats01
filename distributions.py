from math import *
from mathx import over

def fi(x):
    return 1.0 / sqrt(2 * pi) * \
           exp(-0.5*x**2)
    
    
def normpdf(x, mu=1.0, sigma=0.5):
    arg = (x - mu) / sigma
    return fi(arg) / sigma 


# discrete

def binomialpdf(k, p, N):
    # TODO
    return over(N, k) * p**k * \
           (1 - p)**(N - k)

if __name__ == '__main__':
    from display import table, h1, h2, h3
    from mathx import linspace
    
    h1('Distributions')
    h2('Continuous')
    h3('Normpdf')
    table(normpdf, \
    	  linspace(-3, 4, 30))
    
    h2('Discrete')
    h3('binomialpdf')
    # table(binomialpdf, xrange(0, 30))