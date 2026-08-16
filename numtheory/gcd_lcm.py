"""
gcd_lcm.py
Euclidean algorithm (which also gives Bezout coefficients).
"""

from __future__ import annotations
from typing import Tuple


def gcd(a: int, b: int) -> int:
    
    #Euclidean algorithm for the greatest common divisor. gcd(a, b) = gcd(b, a mod b), with gcd(a, 0) = a.
  
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Least common multiple, derived from gcd via:
        lcm(a, b) = |a * b| / gcd(a, b)
    """
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean algorithm.
    Returns (g, x, y) such that:  a*x + b*y = g = gcd(a, b)
    """
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # old_r is gcd(a, b); old_s, old_t are the Bezout coefficients
    return old_r, old_s, old_t
