#!/usr/bin/env python3
"""Independent A332101 certificate using rational logarithm/Taylor exponential.

This program uses no repository code.  It proves the requisite power-ratio
inequalities by bounding -n*log(1-u) with four rational series terms and a
geometric remainder, then bounding exp(-x/128) by alternating Taylor sums.
Squaring seven times gives exp(-x); all arithmetic is integer/rational.
It separately tests small n with exact Python integers and binary search.
"""

import argparse
from fractions import Fraction
from time import perf_counter

INDEX = 777451915729368
THRESHOLD = 1121626023352384
GRID = 10**90
HALVINGS = 7  # exp(-a) = exp(-a/128)**128
TERMS = 70     # 69-term odd lower, 70-term even upper for 0<=x<=1


def ceil_ratio(a, b):
    return (a + b - 1) // b


def fixed_floor(q):
    return q.numerator * GRID // q.denominator


def fixed_ceil(q):
    return ceil_ratio(q.numerator * GRID, q.denominator)


def taylor_bracket(x):
    """For x=x_int/GRID in [0,1], return enclosing grid endpoints of exp(-x)."""
    assert 0 <= x <= GRID
    low_term = high_term = GRID
    low_odd = high_even = GRID
    for j in range(1, TERMS + 1):
        low_term = low_term * x // (GRID * j)
        high_term = ceil_ratio(high_term * x, GRID * j)
        if j & 1:
            low_odd -= high_term
            high_even -= low_term
        else:
            high_even += high_term
            if j < TERMS:  # odd-degree partial sum, through degree 69
                low_odd += low_term
    assert 0 < low_odd <= high_even <= GRID
    return low_odd, high_even


def ratio_power_bounds(h, d):
    """Certified GRID bounds for (1-h/d)**INDEX using log and exp series."""
    assert 1 <= h < d
    u = Fraction(h, d)
    # -INDEX*log(1-u) = INDEX*sum_{j>=1} u**j/j.
    # For j>=5, 1/j <= 1/5, hence residual <= INDEX*u**5/(5*(1-u)).
    log_low = INDEX * sum((u**j / j for j in range(1, 5)), Fraction(0))
    log_high = log_low + INDEX * u**5 / (5 * (1-u))
    xlo = fixed_floor(log_low / (1 << HALVINGS))
    xhi = fixed_ceil(log_high / (1 << HALVINGS))
    lower, _ = taylor_bracket(xhi)  # larger argument => smaller exp
    _, upper = taylor_bracket(xlo)
    for _ in range(HALVINGS):
        lower = lower * lower // GRID
        upper = ceil_ratio(upper * upper, GRID)
    assert 0 <= lower <= upper <= GRID
    return lower, upper


def large_witness():
    k = THRESHOLD
    up_prev = ratio_power_bounds(1, k)[1]
    lo_curr = ratio_power_bounds(1, k + 1)[0]
    assert 2 * up_prev < GRID < 2 * lo_curr
    print('LARGE n=%d k=%d N=%d grid=10^90' % (INDEX, k, k+1))
    print('2*((k-1)/k)^n - 1 upper numerator:', 2 * up_prev - GRID)
    print('2*(k/(k+1))^n - 1 lower numerator:', 2 * lo_curr - GRID)
    lower_sum = 0
    for h in range(1, 121):
        lower_sum += ratio_power_bounds(h, k+1)[0]
    print('sum h=1..120 ((N-h)/N)^n - 1 lower numerator:', lower_sum - GRID)
    assert lower_sum > GRID
    print('PASS witness: A078607(n)=%d A332101(n)=%d' % (k,k+1))


def small_scan(limit):
    """Exact-integer comparisons, accelerating a sum with a provable tail bound.

    For b>q, terms 1..b-q-1 are at most (b-q-1)**n each.
    When that simple estimate is inconclusive we double q, eventually
    summing every term. Thus every classification is exact.
    """
    anomalies = []
    worst_q = 0
    refinement_count = 0

    def reaches(n, b):
        nonlocal worst_q, refinement_count
        target = pow(b, n)
        q = min(128, b-1)
        while True:
            tail_start = b-q
            partial = sum(pow(j, n) for j in range(tail_start, b))
            prior = tail_start - 1
            upper = partial + prior * pow(prior, n) if prior else partial
            worst_q = max(worst_q, q)
            if partial >= target:
                return True
            if upper < target:
                return False
            refinement_count += 1
            assert q < b-1
            q = min(2*q, b-1)

    for n in range(limit + 1):
        if n == 0:
            c, b = 1, 2
        else:
            # Doubling then binary search locates the least positive C(n).
            def good(m):
                return 2 * pow(m, n) > pow(m + 1, n)
            lo, hi = 0, 1
            while not good(hi):
                lo, hi = hi, hi*2
            while hi-lo > 1:
                mid = (hi+lo)//2
                if good(mid):
                    hi = mid
                else:
                    lo = mid
            c = hi
            # Since E(b+1)-E(b)>=0 before C, B>=C+1.
            b = c+1
            while not reaches(n, b):
                b += 1
        if b != c+2:
            anomalies.append((n,b,c))
    print('SMALL exact n=0..%d; B(n) != C(n)+2: %s' % (limit, anomalies))
    print('SMALL maximum explicitly summed terms per comparison:',worst_q)
    print('SMALL inconclusive initial bounds needing refinement:',refinement_count)
    assert anomalies == [(0,2,1),(1,3,2)]
    print('PASS small-range exact check')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=2000)
    args = parser.parse_args()
    t = perf_counter()
    large_witness()
    print('LARGE runtime seconds: %.6f' % (perf_counter()-t))
    small_scan(args.max_n)
    print('TOTAL runtime seconds: %.6f' % (perf_counter()-t))


if __name__ == '__main__':
    main()
