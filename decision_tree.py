import math
from functools import reduce
from collections import namedtuple


used = set()



def unused(attributes):
    return set(attributes) - used


def build_entropy(ds):
    ds = ds
    S, labels = ds
    
    def entropy(attr):
        def p(z):
            T = select(attr, ds, z)
            return float(len(T)) \
                    / float(len(S))

        inner = lambda z: -p(z) * \
                math.log(p(z), 2)
        return sum(map(inner, \
            labels.get(attr).values()))

    return entropy


def id3(ds):
    S, labels = ds
    attributes = labels.keys()
    entropy = build_entropy(ds)  
    def smallest():
        ent = [ (a, entropy(a)) \
            for a in unused(attributes)]
        print(ent)
        return reduce(lambda x, y: \
                      x if x[1] < y[1] else y, ent)
    print(smallest())

def select(what, from_set, where):
    S, _ = select_ds(what,
    	                  from_set,
    	                  where)
    return S

def select_ds(what, from_set, where):
    S, labels = from_set
    res = []
    for row in S:
        if getattr(row, what) == where:
            res.append(row)
    return (set(res), labels)


# test data

def test_set_wf99():
    labels = {
    	'outlook': 
    	    {'sunny': 1, 
          'overcast': 2, 
          'rainy': 4},
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


def print_dset(hdr='wf99',\
	   dset=test_set_wf99()):
    s, labels = dset
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


def test_entropy():
    ds = test_set_wf99()
    entropy = build_entropy(ds)
    print(entropy('windy'))
    
def test_select():
    print_dset()
    print('')
    print_dset(hdr='selw',
    	          dset=select_ds('windy', 
    	             test_set_wf99(),
                  0))


if __name__ == '__main__':
    id3(test_set_wf99())