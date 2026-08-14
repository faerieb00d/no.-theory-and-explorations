"""
diophantine.py
--------------
Solving linear Diophantine equations of the form: a*x + b*y = c
"""

from __future__ import annotations
from typing import Optional, Tuple

from .gcd_lcm import extended_gcd


def solve_linear_diophantine(a: int, b: int, c: int) -> Optional[Tuple[int, int, int, int, int]]:
    """
    Find one integer solution (x0, y0) to a*x + b*y = c.

    A solution exists if and only if gcd(a, b) divides c.

    Returns a tuple (x0, y0, dx, dy, g) where:
      - (x0, y0) is one particular solution
      - all solutions are given by x = x0 + k*dx, y = y0 - k*dy for integer k
      - g = gcd(a, b)
    Returns None if no solution exists.

    Example: solve_linear_diophantine(6, 10, 4)
      -> one solution to 6x + 10y = 4, plus the step size to walk to more.
    """
    g, x, y = extended_gcd(a, b)

    if c % g != 0:
        return None  # gcd(a, b) must divide c for a solution to exist

    scale = c // g
    x0, y0 = x * scale, y * scale

    # Step sizes for generating the full solution family
    dx = b // g
    dy = a // g

    return x0, y0, dx, dy, g
