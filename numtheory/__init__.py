"""
A small, dependency-free Python package for exploring classic number theory:
primes, GCD/LCM, modular arithmetic, Diophantine equations, continued
fractions, and figurate/perfect numbers.

"""

from .primes import (
    is_prime,
    sieve_of_eratosthenes,
    prime_factors,
    next_prime,
    nth_prime,
)
from .gcd_lcm import gcd, lcm, extended_gcd
from .modular import mod_pow, mod_inverse, chinese_remainder_theorem
from .diophantine import solve_linear_diophantine
from .continued_fractions import to_continued_fraction, from_continued_fraction
from .perfect_numbers import is_perfect, divisor_sum, aliquot_sequence

__version__ = "0.1.0"

__all__ = [
    "is_prime",
    "sieve_of_eratosthenes",
    "prime_factors",
    "next_prime",
    "nth_prime",
    "gcd",
    "lcm",
    "extended_gcd",
    "mod_pow",
    "mod_inverse",
    "chinese_remainder_theorem",
    "solve_linear_diophantine",
    "to_continued_fraction",
    "from_continued_fraction",
    "is_perfect",
    "divisor_sum",
    "aliquot_sequence",
]
