import random

N = 10_000_000
hit_count = 0
r = 1

for _ in range(N):
    # losujemy pkt z zakresu [-r, r]
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    z = random.uniform(-r, r)

