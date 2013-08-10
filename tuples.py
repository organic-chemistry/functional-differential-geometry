#!/usr/bin/env python3


class Tuple:
    def __init__(self, *components):
        self._components = components
    
    def __getitem__(self, index):
        return self._components[index]


class UpTuple(Tuple):
    def __repr__(self):
        return "up({})".format(", ".join(str(c) for c in self._components))


class DownTuple(Tuple):
    def __repr__(self):
        return "down({})".format(", ".join(str(c) for c in self._components))


up = UpTuple
down = DownTuple


def ref(tup, *indices):
    if indices:
        return ref(tup[indices[0]], *indices[1:])
    else:
        return tup


def component(*indices):
    def _(tup):
        return ref(tup, *indices)
    return _


if __name__ == "__main__":
    v = up("v^0", "v^1", "v^2")
    p = down("p_0", "p_1", "p_2")
    s = up("t", up("x", "y"), down("p_x", "p_y"))
    assert ref(up("a", "b", "c"), 1) == "b"
    assert ref(up(up("a", "b"), up("c", "d")), 0, 1) == "b"
    assert component(0, 1)(up(up("a", "b"), up("c", "d"))) == "b"
    assert repr(up(1, 2)) == "up(1, 2)"
    assert repr(down(1, 2)) == "down(1, 2)"
