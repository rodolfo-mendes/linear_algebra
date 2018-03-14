import pytest

from plane import Plane
from vector import Vector

def test_plane_are_parallel_to_itself():
    p1 = Plane(Vector([10.0, -5.0, 7.5]), 5.0)
    assert p1.is_parallel(p1)

def test_equal_planes_are_parallel():
    p1 = Plane(Vector([10.0, -5.0, 7.5]), 5.0)
    p2 = Plane(Vector([10.0, -5.0, 7.5]), 5.0)
    assert p1.is_parallel(p2)

def test_planes_with_different_constants_are_parallel():
    p1 = Plane(Vector([10.0, -5.0, 7.5]), 5.0)
    p2 = Plane(Vector([10.0, -5.0, 7.5]), -1.0)
    assert p1.is_parallel(p2)

def test_planes_with_multiple_coefficients_are_parallel():
    p1 = Plane(Vector([10.0, -5.0, 7.5]), 5.0)
    p2 = Plane(Vector([20.0, -10.0, 15.0]), -1.0)
    assert p1.is_parallel(p2)

def test_planes_in_different_directions_are_not_parallel():
    p1 = Plane(Vector([2.0, 5.0, 7.0]), 3.0)
    p2 = Plane(Vector([5.0, 2.0, 2.0]), 5.0)
    assert not p1.is_parallel(p2)

def test_plane_is_equal_to_itself():
    p1 = Plane(Vector([10.0, -5.0, 7.5]), 5.0)
    assert p1.is_equivalent(p1)

def test_equal_planes_are_equal():
    p1 = Plane(Vector([10.0, -5.0, 7.5]), 5.0)
    p2 = Plane(Vector([10.0, -5.0, 7.5]), 5.0)
    assert p1.is_equivalent(p2)

def test_parallel_planes_with_different_constants_are_not_equal():
    p1 = Plane(Vector([10.0, -5.0, 7.5]), 5.0)
    p2 = Plane(Vector([10.0, -5.0, 7.5]), -1.0)
    assert not p1.is_equivalent(p2)

def test_planes_in_different_directions_are_different():
    p1 = Plane(Vector([2.0, 5.0, 7.0]), 3.0)
    p2 = Plane(Vector([5.0, 2.0, 2.0]), 5.0)
    assert not p1.is_equivalent(p2)
    