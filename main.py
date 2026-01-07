import random

N = 10_000_000
hit_count = 0
r = 1

for _ in range(N):
    # losujemy pkt z zakresu [-r, r]
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    z = random.uniform(-r, r)

    if (x**2 + y**2) <= 1 and (x**2 + z**2) <= 1:
        hit_count += 1

steinmetz_volume = (hit_count / N) * 8 * r**3
print("Objętość bryły Steinmetza wynosi:", steinmetz_volume)