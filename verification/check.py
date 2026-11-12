"""Integer interval certificate, independently written by OpenAI Codex, 2026-11-13."""
n = 777451915729368
k = 1121626023352384
scale = 10**70

def enclosure(p, q):
    # Bounds for (p/q)^n on the grid of multiples of 1/scale.
    low, high = p * scale // q, -(-p * scale // q)
    a, b = scale, scale
    exponent = n
    while exponent:
        if exponent % 2:
            a = a * low // scale
            b = -(-b * high // scale)
        low = low * low // scale
        high = -(-high * high // scale)
        exponent //= 2
    return a, b

previous_upper = enclosure(k - 1, k)[1]
current_lower = enclosure(k, k + 1)[0]
sum_lower = sum(enclosure(k + 1 - h, k + 1)[0] for h in range(1, 121))
for name, margin in [('previous upper', 2 * previous_upper - scale),
                     ('current lower', 2 * current_lower - scale),
                     ('sum lower', sum_lower - scale)]:
    print(name + ' margin (scale 10^70):', margin)
assert 2 * previous_upper < scale < 2 * current_lower
assert sum_lower > scale
print('PASS: A078607(n) =', k, '; A332101(n) =', k + 1)
