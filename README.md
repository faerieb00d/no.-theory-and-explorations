# Number Theory Explorations

A small, dependency-free Python library and playground for classic number
theory: primes, GCD/LCM, modular arithmetic, Diophantine equations,
continued fractions, and perfect/aliquot numbers.

Built for readability — the code is meant to be read alongside the math,
not just imported as a black box.

## Features

| Module | What it covers |
|---|---|
| `numtheory.primes` | Primality testing, Sieve of Eratosthenes, prime factorization, n-th prime |
| `numtheory.gcd_lcm` | Euclidean algorithm, LCM, extended Euclidean algorithm (Bezout coefficients) |
| `numtheory.modular` | Fast modular exponentiation, modular inverse, Chinese Remainder Theorem |
| `numtheory.diophantine` | Solving linear Diophantine equations `ax + by = c` |
| `numtheory.continued_fractions` | Convert rationals to/from continued fraction form |
| `numtheory.perfect_numbers` | Divisor sums, perfect number classification, aliquot sequences |

## Project structure

```
number-theory-explorations/
├── numtheory/                  # the library
│   ├── __init__.py
│   ├── primes.py
│   ├── gcd_lcm.py
│   ├── modular.py
│   ├── diophantine.py
│   ├── continued_fractions.py
│   └── perfect_numbers.py
├── examples/
│   └── explore.py              # runnable tour of every module
├── tests/
│   ├── test_primes.py
│   └── test_modular.py
├── README.md
├── requirements.txt
└── LICENSE
```

## Getting started

No external dependencies are required — everything uses the Python
standard library.

```bash
git clone https://github.com/<your-username>/number-theory-explorations.git
cd number-theory-explorations

# Run the guided tour
python examples/explore.py

# Run the tests
python -m pytest tests/
# or, without pytest installed:
python tests/test_primes.py
python tests/test_modular.py
```

## Usage examples

```python
from numtheory import is_prime, sieve_of_eratosthenes, prime_factors

is_prime(97)                    # True
sieve_of_eratosthenes(50)       # [2, 3, 5, 7, 11, ..., 47]
prime_factors(360)              # {2: 3, 3: 2, 5: 1}
```

```python
from numtheory import mod_pow, mod_inverse, chinese_remainder_theorem

mod_pow(3, 200, 50)             # fast modular exponentiation
mod_inverse(3, 11)              # 4, since (3 * 4) % 11 == 1
chinese_remainder_theorem([2, 3, 2], [3, 5, 7])   # 23
```

```python
from numtheory import solve_linear_diophantine

# Solve 6x + 10y = 4
x0, y0, dx, dy, g = solve_linear_diophantine(6, 10, 4)
```

## Roadmap ideas

Good next explorations to add as the project grows:

- [ ] Miller–Rabin probabilistic primality test for large numbers
- [ ] Quadratic residues and the Legendre/Jacobi symbol
- [ ] Pell's equation solver
- [ ] Euler's totient function and multiplicative functions
- [ ] Visualizations (e.g. Ulam spiral, aliquot sequence graphs)

## License

MIT — see [LICENSE](LICENSE).
