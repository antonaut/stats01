import math
from functools import reduce

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
