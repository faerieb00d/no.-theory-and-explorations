
#modular.py



from __future__ import annotations
from typing import List, Optional

from .gcd_lcm import extended_gcd


def mod_pow(base: int, exponent: int, modulus: int) -> int:
    """
    Fast modular exponentiation via binary exponentiation (square-and-multiply).
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
  
    
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"No inverse exists: gcd({a}, {m}) = {g}, not 1")
    return x % m


def chinese_remainder_theorem(remainders: List[int], moduli: List[int]) -> Optional[int]:
  
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
