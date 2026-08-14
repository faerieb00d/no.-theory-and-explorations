"""
modular.py
----------
Modular exponentiation, modular inverse, and the Chinese Remainder Theorem.
"""

from __future__ import annotations
from typing import List, Optional

from .gcd_lcm import extended_gcd


def mod_pow(base: int, exponent: int, modulus: int) -> int:
    """
    Fast modular exponentiation via binary exponentiation (square-and-multiply).

    Computes (base ** exponent) % modulus in O(log exponent) multiplications
    instead of the naive O(exponent).
    """
    if modulus == 1:
        return 0
    if exponent < 0:
        raise ValueError("Use mod_inverse for negative exponents")

    result = 1
    base %= modulus

    while exponent > 0:
        if exponent & 1:  # exponent is odd
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus

    return result


def mod_inverse(a: int, m: int) -> int:
    """
    Modular multiplicative inverse of a mod m, i.e. the x such that
    (a * x) % m == 1.

    Exists only when gcd(a, m) == 1. Computed via the extended Euclidean
    algorithm rather than Fermat's little theorem, so it also works for
    non-prime m (as long as a and m are coprime).
    """
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No inverse exists: gcd({a}, {m}) = {g}, not 1")
    return x % m


def chinese_remainder_theorem(remainders: List[int], moduli: List[int]) -> Optional[int]:
    """
    Solve the system:
        x = remainders[0] (mod moduli[0])
        x = remainders[1] (mod moduli[1])
        ...

    Returns the unique solution x in [0, lcm(moduli)), or None if the
    system is unsolvable (moduli need not be pairwise coprime; this
    handles the general case via pairwise merging).
    """
    if len(remainders) != len(moduli):
        raise ValueError("remainders and moduli must have the same length")

    x, m = remainders[0] % moduli[0], moduli[0]

    for r, n in zip(remainders[1:], moduli[1:]):
        g, p, q = extended_gcd(m, n)
        if (r - x) % g != 0:
            return None  # no solution: congruences are inconsistent

        lcm_mn = m // g * n
        # Combine the two congruences into one mod lcm(m, n)
        x = (x + m * ((r - x) // g % (n // g)) * p) % lcm_mn
        m = lcm_mn

    return x % m
