import random

# kod zamkniety w funkcji z okreslonym typami
def steinmetz_mypyc_function(N: int, r: float) -> float:
    
    hit_count: int = 0
    x: float
    y: float
    z: float

    for _ in range(N):
        # losujemy pkt z zakresu [-r, r]
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        z = random.uniform(-r, r)

        if (x**2 + y**2) <= 1 and (x**2 + z**2) <= 1:
            hit_count += 1
    return (hit_count / N) * 8 * r**3