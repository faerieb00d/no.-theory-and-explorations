import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from numtheory.gcd_lcm import gcd, lcm, extended_gcd
from numtheory.modular import mod_pow, mod_inverse, chinese_remainder_theorem
from numtheory.diophantine import solve_linear_diophantine


def test_gcd_lcm():
    assert gcd(48, 18) == 6
    assert lcm(4, 6) == 12
    assert gcd(0, 5) == 5


def test_extended_gcd():
    a, b = 240, 46
    g, x, y = extended_gcd(a, b)
    assert g == gcd(a, b)
    assert a * x + b * y == g


def test_mod_pow():
    assert mod_pow(2, 10, 1000) == 24  # 1024 % 1000
    assert mod_pow(7, 128, 13) == pow(7, 128, 13)  # cross-check vs builtin


def test_mod_inverse():
    inv = mod_inverse(3, 11)
    assert (3 * inv) % 11 == 1


def test_chinese_remainder_theorem():
    # x = 2 mod 3, x = 3 mod 5, x = 2 mod 7  ->  classic CRT example, x = 23
    result = chinese_remainder_theorem([2, 3, 2], [3, 5, 7])
    assert result == 23


def test_solve_linear_diophantine():
    solution = solve_linear_diophantine(6, 10, 4)
    assert solution is not None
    x0, y0, dx, dy, g = solution
    assert 6 * x0 + 10 * y0 == 4

    # No solution case: gcd(4, 6) = 2, does not divide 5
    assert solve_linear_diophantine(4, 6, 5) is None


if __name__ == "__main__":
    test_gcd_lcm()
    test_extended_gcd()
    test_mod_pow()
    test_mod_inverse()
    test_chinese_remainder_theorem()
    test_solve_linear_diophantine()
    print("All modular/diophantine tests passed.")
