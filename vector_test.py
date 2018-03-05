from vector import Vector

def test_eq():
    assert Vector([0.6, 0.8, 0.9]) == Vector([0.6, 0.8, 0.9])

def test_not_eq():
    assert Vector([0.6, 0.8, 0.9]) != Vector([1.6, 0.8, 0.9])

def test_plus():
    v = Vector([1.5, 2.0, 3.5])
    w = Vector([0.5, 1.0, -0.5])

    assert v.plus(w) == Vector([2.0, 3.0, 3.0])

def test_minus():
    v = Vector([1.5, 2.0, 3.5])
    w = Vector([0.5, 1.0, -0.5])

    assert v.minus(w) == Vector([1.0, 1.0, 4.0])

def test_times_scalar():
    v = Vector([1.5, 2.0, 3.5])

    assert v.times_scalar(3.0) == Vector([4.5, 6.0, 10.5])

def test_magnitude():
    assert Vector([3.0, 4.0]).magnitude() == 5.0

def test_normalized():
    print( Vector([3.0, 4.0]).normalized() )
    assert Vector([3.0, 4.0]).normalized() == Vector(['0.6', '0.8'])

def test_parallel_vector():
    print(Vector([2.5, 3.5]).angle_with(Vector([25, 35]), in_degrees=True))
    assert Vector([2.5, 3.5]).is_parallel(Vector([25, 35]))
