# -*- coding: utf-8
import math
from functools import reduce
from collections import namedtuple

"""
The target attribute is always furthest
to the right and accessed like:
    row[-1]
    
It should always be binary,
meaning only 0 or 1 are allowed values.
"""



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


class Node:
    def __init__(self, 
    	    parent,
    	    label,
    	    attr,
      	  children):
        self.label = label
        self.attribute = attr
        self.parent = parent
        self.children = children
    
    def __repr__(self):
        return '(' + \
        	self.attribute + ': ' + \
        	str(self.label) + ')'


def id3(ds):
    """
ID3 (Examples, 
	    Target_Attribute, 
	    Attributes) 
Create a root node for the tree 
If all examples are positive, 
  Return the single-node tree Root, 
  with label = +. 
If all examples are negative, 
  Return the single-node tree Root, 
  with label = -. 
If number of predicting attributes
  is empty
  Return the single node tree Root,
    with label = most common value 
    of the target attribute in the 
    examples. 
Otherwise 
  Begin A <- The Attribute that
  best classifies examples.
  Decision Tree attribute for Root = A. 

For each possible value, vi, of A, 
Add a new tree branch below Root,
 corresponding to the test A = vi. 
 
Let Examples(vi) be the subset 
of examples that have the value vi 
for A 

If Examples(vi) is empty 
Then below this new branch 
  add a leaf node with 
  label = most common target value 
  in the examples 
Else below this new branch add 
  the subtree 
  ID3 (Examples(vi), 
  	  Target_Attribute, 
  	  Attributes – {A}) 
End 
Return Root    
    """
    S, labels = ds
    attributes = labels.keys()
    entropy = build_entropy(ds)  
    def smallest(unused):
        ent = [ (a, entropy(a)) \
            for a in unused ]            
        return reduce(lambda x, y: \
                      x if x[1] < y[1] else y, ent)

    return id3helper(
        None,
        ds,
        smallest,
        set([attributes[0]]))
        

def id3helper(
    parent, 
	   ds,
	   smallest,
	   used):
    S, labels = ds
    attributes = labels.keys()
    nplus = 0
    nminus = 0


    for row in S:
        if row[-1] == 1:
            nplus += 1
        else:
            nminus += 1

    plus = Node(parent, 
                1,
                attributes[-1], 
                None)
    minus = Node(parent,
    	            0,
    	            attributes[-1],
    	            None)
    most_common = minus
    
    if nplus > nminus:
        most_common = plus

    if nplus == len(S):
        return plus
    if nminus == len(S):
        return minus
    if len(used) == len(attributes):
        return most_common

    unused = set(attributes) - used
    A = smallest(unused)[0]
    children = {}
    current = Node(parent, None, A, children)

    for val in labels.get(A).values():
        T = select(A, ds, val)
        if len(T) == 0:
            children[val] = most_common
        else:
            children[val] = \
        	      id3helper(current,
        	      	  (T, labels),
        	  	      smallest,
        	      	  used.union(set([A])))
    return current


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
def print_dtree(dt, depth=0):
    print(dt)
    if not dt.children:
        return
    for k in dt.children.keys():
        print '  '*depth + str(k) + ':',
        print_dtree(dt.children[k], depth + 1)

if __name__ == '__main__':
    dtree = id3(test_set_wf99())
    print_dtree(dtree)