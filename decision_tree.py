import math
from functools import reduce

used = set()


def unused(attr):
    return attr in used


def entropy(attr):
    """TODO FIX THIS"""
    return math.sqrt(attr)


def id3(S, attributes):
    ent = map(entropy, unused(attributes))
    smallest = reduce(lambda x, y: x < y, ent)
    pass
