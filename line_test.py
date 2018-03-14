import pytest

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

def test_infinite_intersection():
    l1 = Line(Vector([2.5, 3.5]), 0)

    with pytest.raises(Exception) as e:
        l1.intersection(l1)

    assert 'infinite intersections' in str(e.value)

def test_no_intersection():
    l1 = Line(Vector([2.5, 3.5]), 0)
    l2 = Line(Vector([25, 35]), 27)

    with pytest.raises(Exception) as e:
        l1.intersection(l2)

    assert 'no intersection' in str(e.value)

def test_single_intersection():
    l1 = Line(Vector([5, 3]), 8)
    l2 = Line(Vector([-5, 7]), 12)
    print(l1.intersection(l2))
    assert l1.intersection(l2) == Vector([0.4, 2])
