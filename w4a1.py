######################################################################
# This week's reading:
# --------------------
# - Review sections 1 – 4.6 of the Python Tutorial.
# - 4.7.6. Documentation Strings
#   https://docs.python.org/3/tutorial/controlflow.html#documentation-strings
# - Symbol Tables
#   https://eli.thegreenplace.net/2010/09/18/python-internals-symbol-tables-part-1
#
# This week's assignment is based on the quadratic formula. References:
# - https://www.khanacademy.org/math/algebra/quadratics/solving-quadratics-using-the-quadratic-formula/a/discriminant-review
# - https://en.wikipedia.org/wiki/Quadratic_formula
#
# Implement `sign` and `roots` functions. Fix all the errors.
######################################################################

# Here we reuse `discriminant` function implemented earlier.
# The import statement outputs "You did it! \o/" message. Can this noise be
# suppressed?
from w3a1 import discriminant

from math import sqrt  # `sqrt` is needed for `roots` function


def sign(x):
    """Given numeric argument x, return 1 if x is positive,
    -1 if x is negative, otherwise return 0.

    >>> sign(3.141592653589793)
    1
    >>> sign(-12)
    -1
    >>> sign(0.)
    0
    """
    pass


def roots(a, b, c):
    """Return solutions of the quadratic equation
    ax^2 + bx + c = 0

    >>> roots(2, -3, 1)
    (0.5, 1.0)

    >>> x1, x2 = roots(6, 10, -1)
    >>> round(x1, 6), round(x2, 6)
    (-1.761294, 0.094627)

    >>> roots(3, 24, 48)
    (-4.0,)

    >>> roots(1, 2, 3) is None
    True

    >>> roots(0, 1, -5)
    Traceback (most recent call last):
    AssertionError
    """
    assert a != 0


if __name__ == '__main__':
    import doctest
    doctest.testmod()
