"""
explore.py
----------
A runnable tour through the numtheory package. Run this directly:

    python examples/explore.py
"""

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from numtheory import (
    is_prime,
    sieve_of_eratosthenes,
    prime_factors,
    nth_prime,
    gcd,
    lcm,
    extended_gcd,
    mod_pow,
    mod_inverse,
    chinese_remainder_theorem,
    solve_linear_diophantine,
    to_continued_fraction,
    from_continued_fraction,
    is_perfect,
    aliquot_sequence,
)


def section(title: str) -> None:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


def main() -> None:
    section("Primes")
    print(f"Is 97 prime? {is_prime(97)}")
    print(f"Primes up to 50: {sieve_of_eratosthenes(50)}")
    print(f"Prime factorization of 360: {prime_factors(360)}")
    print(f"The 100th prime is: {nth_prime(100)}")

    section("GCD / LCM")
    print(f"gcd(48, 18) = {gcd(48, 18)}")
    print(f"lcm(4, 6) = {lcm(4, 6)}")
    g, x, y = extended_gcd(240, 46)
    print(f"extended_gcd(240, 46) = gcd {g}, with 240*({x}) + 46*({y}) = {g}")

    section("Modular arithmetic")
    print(f"3^200 mod 50 = {mod_pow(3, 200, 50)}")
    print(f"Inverse of 3 mod 11 = {mod_inverse(3, 11)}")
    crt_result = chinese_remainder_theorem([2, 3, 2], [3, 5, 7])
    print(f"CRT: x = 2 (mod 3), x = 3 (mod 5), x = 2 (mod 7)  ->  x = {crt_result}")

    section("Diophantine equations")
    solution = solve_linear_diophantine(6, 10, 4)
    x0, y0, dx, dy, g = solution
    print(f"One solution to 6x + 10y = 4: x = {x0}, y = {y0}")
    print(f"Next solution: x = {x0 + dx}, y = {y0 - dy}")

    section("Continued fractions")
    cf = to_continued_fraction(415, 93)
    print(f"415/93 as a continued fraction: {cf}")
    back = from_continued_fraction(cf)
    print(f"Converted back: {back} (should equal 415/93)")

    section("Perfect numbers & aliquot sequences")
    for n in [6, 28, 12, 496]:
        print(f"{n} is perfect? {is_perfect(n)}")
    print(f"Aliquot sequence starting at 12: {aliquot_sequence(12)}")
    print(f"Aliquot sequence starting at 220: {aliquot_sequence(220, max_steps=5)}")


if __name__ == "__main__":
    main()
