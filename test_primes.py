import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from numtheory.primes import is_prime, sieve_of_eratosthenes, prime_factors, next_prime, nth_prime


def test_is_prime_basic():
    assert not is_prime(0)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(97)
    assert not is_prime(100)


def test_sieve_matches_is_prime():
    limit = 200
    sieve_result = sieve_of_eratosthenes(limit)
    brute_force = [n for n in range(2, limit + 1) if is_prime(n)]
    assert sieve_result == brute_force


def test_prime_factors():
    assert prime_factors(360) == {2: 3, 3: 2, 5: 1}
    assert prime_factors(17) == {17: 1}
    assert prime_factors(1) == {}


def test_next_prime():
    assert next_prime(10) == 11
    assert next_prime(13) == 17


def test_nth_prime():
    assert nth_prime(1) == 2
    assert nth_prime(6) == 13
    assert nth_prime(100) == 541


if __name__ == "__main__":
    test_is_prime_basic()
    test_sieve_matches_is_prime()
    test_prime_factors()
    test_next_prime()
    test_nth_prime()
    print("All prime tests passed.")
