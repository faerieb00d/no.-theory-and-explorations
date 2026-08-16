
#perfect_numbers.py

from __future__ import annotations
from typing import List


def divisor_sum(n: int, proper: bool = True) -> int:
    """
    If proper=True (default), sums divisors excluding n itself
    (this is the "aliquot sum"). If proper=False, includes n.
    """
    if n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 0 if proper else 1

    total = 1  # 1 always divides n (for n > 1)
    d = 2
    while d * d <= n:
        if n % d == 0:
            total += d
            partner = n // d
            if partner != d:
                total += partner
        d += 1

    if not proper:
        total += n

    return total


def is_perfect(n: int) -> bool:
    """
    A number is "perfect" if it equals the sum of its proper divisors.
    Example: 28 = 1 + 2 + 4 + 7 + 14.
    """
    return n > 1 and divisor_sum(n, proper=True) == n


def classify(n: int) -> str:
    """Classify n as 'perfect', 'abundant', or 'deficient'."""
    s = divisor_sum(n, proper=True)
    if s == n:
        return "perfect"
    return "abundant" if s > n else "deficient"


def aliquot_sequence(n: int, max_steps: int = 20) -> List[int]:
    """
    Generate the aliquot sequence starting at n: repeatedly replace the
    current number with the sum of its proper divisors.

    Stops early if it reaches 0 sequence terminates 
    or a perfect
    number- fixed point, or after max_steps iterations. Many aliquot
    sequences are unsolved problems in number theory (
    """
    sequence = [n]
    current = n

    for _ in range(max_steps):
        current = divisor_sum(current, proper=True)
        sequence.append(current)
        if current == 0 or current == sequence[-2]:
            break

    return sequence
