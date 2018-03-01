from vector import Vector

v = Vector([3.039, 1.879])
b = Vector([0.825, 2.036])
print(
    'v_p = {0}, is_parallel={1}'.format(
        v.parallel_to(b),
        v.parallel_to(b).is_parallel(b)
    )
)
print

v = Vector([-9.88, -3.264, -8.159])
b = Vector([-2.155, -9.353, -9.473])
print(
    'v_o = {0}, is_orthogonal={1}'.format(
        v.orthogonal_to(b),
        v.orthogonal_to(b).is_orthogonal_to(b)
    )
)
print

v = Vector([3.009, -6.172, 3.692, -2.51])
b = Vector([6.404, -9.144, 2.759, 8.718])
print(v.parallel_to(b))
print(v.orthogonal_to(b))
