import math
from functools import reduce
from collections import namedtuple


used = set()


def unused(attr):
    return attr in used


def build_entropy(S, attrs):
    S = S
    attrs = attrs

    def entropy(attr):
        def p(z):
            return float(len(attrs[z].nodes())) \
            / float(len(S))

        inner = lambda z: -p(z) * math.log2(p(z))
        return sum(map(inner, attrs[attr].nodes()))

    return entropy


def id3(S, attributes):
    entropy = build_entropy(S, attributes)
    ent = map(entropy, unused(attributes))
    smallest = reduce(lambda x, y: x < y, ent)
    pass


# test data

def test_set_wf99():
    O = {'sunny':1, 
         'overcast':2, 
         'rainy':4}
    T = {'hot': 1,
         'mild': 2,
         'cool': 4}
    H = {'high': 1,
         'normal': 2}   
    W = {'true': 1, 'false': 0}
    P = {'yes': 1, 'no': 0}
    def n(outlook,
          temperature,
          humidity,
          windy,
          play):
        return namedtuple(
        	    outlook=outlook,
        	    temperature=temperature,
        	    humidity=humidity,
        	    windy=windy,
        	    play=play)
  
    S = set(
    	  n(1, 1, 1, 0, 0),
    	  n(1, 1, 1, 1, 0),
    	  n(2, 1, 1, 0, 1),
    	  n(4, 2, 1, 0, 1),
    	  \
    	  n(4, 4, 2, 0, 1),
    	  n(4, 4, 2, 1, 0),
    	  n(2, 4, 2, 1, 1),
    	  n(1, 2, 1, 0, 0),
    	  \
    	  n(1, 4, 2, 0, 1),
    	  n(4, 2, 2, 0, 1),
    	  n(1, 2, 2, 1, 1),
    	  n(2, 2, 1, 1, 1),
    	  \
    	  n(2, 1, 2, 0, 1),
    	  n(4, 2, 1, 1, 0)   	  
    	)
     return (S, (O, T, H, W, P))

def print_test_set():
  pass