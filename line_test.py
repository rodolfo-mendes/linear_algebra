from line import Line
from vector import Vector

def test_equals_lines_are_parallel():
    l1 = Line(Vector([2, 3]), 0)
    assert l1.is_parallel(l1)

def test_orthogonal_lines_are_not_paralle():
    l1 = Line(Vector([1, 0]), 0)
    l2 = Line(Vector([0, 1]), 0)
    assert not l1.is_parallel(l2)

def test_parallel_lines():
    l1 = Line(Vector([2.5, 3.5]), 0)
    l2 = Line(Vector([25, 35]), 27)
    assert l1.is_parallel(l2)
    
def test_equals_lines_are_equal():
    l1 = Line(Vector([2, 3]), 0)
    assert l1.is_equal(l1)

def test_orthogonal_lines_are_not_equal():
    l1 = Line(Vector([1, 0]), 0)
    l2 = Line(Vector([0, 1]), 0)
    assert not l1.is_equal(l2)

def test_parallel_lines_are_not_equal():
    l1 = Line(Vector([2.5, 3.5]), 0)
    l2 = Line(Vector([25, 35]), 27)
    assert not l1.is_equal(l2)
