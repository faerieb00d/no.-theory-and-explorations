"""
primes.py
---------
Primality testing, prime generation, and prime factorization.
"""

from __future__ import annotations
from typing import List, Dict


def is_prime(n: int) -> bool:
    """
    Trial-division primality test with 6k +/- 1 optimization.

    Every prime > 3 is of the form 6k - 1 or 6k + 1, so after
    checking 2 and 3 we only need to test candidates of that form.

    Time complexity: O(sqrt(n))
    """
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def sieve_of_eratosthenes(limit: int) -> List[int]:
    """
    Return all primes <= limit using the Sieve of Eratosthenes.

    Time complexity: O(n log log n)
    Space complexity: O(n)
    """
    if limit < 2:
        return []

    is_composite = [False] * (limit + 1)
    primes = []

    for number in range(2, limit + 1):
        if not is_composite[number]:
            primes.append(number)
            # Mark all multiples of `number` starting at number*number
            for multiple in range(number * number, limit + 1, number):
                is_composite[multiple] = True

    return primes


def prime_factors(n: int) -> Dict[int, int]:
    """
    Return the prime factorization of n as {prime: exponent}.

    Example: prime_factors(360) -> {2: 3, 3: 2, 5: 1}   (360 = 2^3 * 3^2 * 5)
    """
    if n < 1:
        raise ValueError("prime_factors is defined for positive integers only")

    factors: Dict[int, int] = {}
    remaining = n

    divisor = 2
    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factors[divisor] = factors.get(divisor, 0) + 1
            remaining //= divisor
        divisor += 1 if divisor == 2 else 2  # after 2, only test odd numbers

    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1

    return factors


def next_prime(n: int) -> int:
    """Return the smallest prime strictly greater than n."""
    candidate = n + 1
    while not is_prime(candidate):
        candidate += 1
    return candidate


def nth_prime(n: int) -> int:
    """
    Return the n-th prime number (1-indexed), i.e. nth_prime(1) == 2.

    Uses a growing sieve so it stays reasonably fast for moderate n.
    """
    if n < 1:
        raise ValueError("n must be >= 1")

    # Rough upper bound on the n-th prime for a sieve limit (valid for n >= 6)
    import math

    if n < 6:
        limit = 15
    else:
        limit = int(n * (math.log(n) + math.log(math.log(n)))) + 10

    primes = sieve_of_eratosthenes(limit)
    while len(primes) < n:
        limit *= 2
        primes = sieve_of_eratosthenes(limit)

    return primes[n - 1]
