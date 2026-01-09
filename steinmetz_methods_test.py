import random
import ctypes
from numba import jit
import matplotlib.pyplot as plt
import time

def time_it(fun):
    def wrapper(*args, **kwargs):
        stime = time.perf_counter()
        v = fun(*args, **kwargs)
        etime = time.perf_counter()
        mtime = etime - stime
        print("Czas wykonania", mtime)
        return (v, mtime)
    return wrapper


# Python czysty
@time_it
def steinmetz_pure_python(N, r):
    
    hit_count = 0
    for _ in range(N):
        # losujemy pkt z zakresu [-r, r]
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        z = random.uniform(-r, r)

        if (x**2 + y**2) <= 1 and (x**2 + z**2) <= 1:
            hit_count += 1
    return (hit_count / N) * 8 * r**3

# Python z Numba
@time_it
@jit(nopython=True)
def steinmetz_numba(N, r):
    
    hit_count = 0
    for _ in range(N):
        # losujemy pkt z zakresu [-r, r]
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        z = random.uniform(-r, r)

        if (x**2 + y**2) <= 1 and (x**2 + z**2) <= 1:
            hit_count += 1
    return (hit_count / N) * 8 * r**3
# Python z ctypes (C)
def steinmetz_c_lib():
    lib_path = './libsteinmetz.so'

# Python z mypyc
def steinmetz_mypyc():
    import steinmetz_mypyc
    return steinmetz_mypyc.steinmetz_mypyc_function

steinmetz_pure_python(1_000_000, 1)
steinmetz_numba(1_000_000, 1)
steinmetz_numba(1_000_000, 1)