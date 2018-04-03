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
    labels = {
    	'outlook': 
    	    {'sunny':1, 
          'overcast':2, 
          'rainy':4},
    'temperature': 
        {'hot': 1,
         'mild': 2,
         'cool': 4},
    'humidity': 
        {'high': 1,
         'normal': 2}, 
    'windy': 
        {'true': 1, 
         'false': 0},
    'play': 
        {'yes': 1, 
         'no': 0}}

    n = namedtuple('n',
        	    """outlook,
        	    temperature,
        	    humidity,
        	    windy,
        	    play""")
  
    S = set([
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
    	  n(4, 2, 1, 1, 0)])
    return (S, labels)


def key_from_value(d,
                   val, 
                   default=None):
    for k in d:
        if d.get(k) == val:
            return k
    return default


def print_test_set(hdr='wf99',\
	   dset=test_set_wf99):
    s, labels = dset()
    print('test dataset - ' + hdr)
    print('-------------------')
    for row in s:
        res = '('
        for f in row._fields:
            res += \
              	key_from_value(   \
              		labels.get(f),   \
              	 getattr(row, f))
            res += ', '
        res = res[:-2]
        res += ')'
        print(res)    


if __name__ == '__main__':
    print_test_set()