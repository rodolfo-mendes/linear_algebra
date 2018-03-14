from plane import Plane
from vector import Vector

p1 = Plane(Vector([-0.412, 3.806, 0.728]), -3.46)
p2 = Plane(Vector([1.03, -9.515, -1.82]), 8.65)
print(
    'Equal = {0}, Parallel but Unequal: {1}, Not Parallel: {2}'.format(
    p1 == p2,
    (p1 != p2 and p1.is_parallel(p2)),
    not p1.is_parallel(p2))
)
print('')

p1 = Plane(Vector([2.611, 5.528, 0.283]), 4.6)
p2 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)
print(
    'Equal = {0}, Parallel but Unequal: {1}, Not Parallel: {2}'.format(
    p1 == p2,
    (p1 != p2 and p1.is_parallel(p2)),
    not p1.is_parallel(p2))
)
print('')

p1 = Plane(Vector([-7.926, 8.625, -7.217]), -7.952)
p2 = Plane(Vector([-2.642, 2.875, -2.404]), -2.443)
print(
    'Equal = {0}, Parallel but Unequal: {1}, Not Parallel: {2}'.format(
    p1 == p2,
    (p1 != p2 and p1.is_parallel(p2)),
    not p1.is_parallel(p2))
)
print('')