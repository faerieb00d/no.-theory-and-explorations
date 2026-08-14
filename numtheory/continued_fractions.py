"""
continued_fractions.py
-----------------------
Convert rationals to/from their continued fraction representation.

A continued fraction [a0; a1, a2, ..., an] represents:
    a0 + 1 / (a1 + 1 / (a2 + 1 / (... + 1/an)))
"""

from __future__ import annotations
from typing import List
from fractions import Fraction


def to_continued_fraction(numerator: int, denominator: int) -> List[int]:
    """
    Convert a rational number numerator/denominator into its continued
    fraction representation [a0, a1, ..., an], using the Euclidean algorithm.
    """
    if denominator == 0:
        raise ValueError("denominator cannot be zero")

    terms: List[int] = []
    n, d = numerator, denominator

    while d != 0:
        q = n // d
        terms.append(q)
        n, d = d, n - q * d

    return terms


def from_continued_fraction(terms: List[int]) -> Fraction:
    """
    Reconstruct the exact rational value of a continued fraction
    [a0, a1, ..., an], working from the back (bottom of the fraction) up.
    """
    if not terms:
        raise ValueError("terms must be non-empty")

    result = Fraction(terms[-1])
    for term in reversed(terms[:-1]):
        result = term + Fraction(1, 1) / result

    return result
