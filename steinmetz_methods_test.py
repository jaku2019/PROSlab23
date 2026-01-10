import random
import ctypes
from steinmetz_mypyc import steinmetz_mypyc_function
from steinmetz_ctype import steinmetz_volume_c
from numba import jit
import matplotlib.pyplot as plt
import time
import numpy as np

# liczenie czasu wykonania
def time_it(fun):
    def wrapper(*args, **kwargs):
        stime = time.perf_counter()
        # result = fun(*args, **kwargs) moznaby zracac tez wynik, ale tu potrzebny jest tylko czas
        etime = time.perf_counter()
        mtime = etime - stime
        # print("Czas wykonania", mtime)
        return (mtime)
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

# Python z Numba bez pomiaru (dla 'rozgrzewki' JIT)
@jit(nopython=True)
def steinmetz_numba_warmup(N, r):
    hit_count = 0
    for _ in range(N):
        # losujemy pkt z zakresu [-r, r]
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        z = random.uniform(-r, r)

        if (x**2 + y**2) <= 1 and (x**2 + z**2) <= 1:
            hit_count += 1
    return (hit_count / N) * 8 * r**3

# Python z Numba z pomiarem
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

# Python z ctypes
@time_it
def steinmetz_c_lib(N, r):
    return steinmetz_volume_c(N, r)

# Python z mypyc
@time_it
def steinmetz_mypyc(N, r):
    import steinmetz_mypyc
    return steinmetz_mypyc.steinmetz_mypyc_function(N, r)

# Czesc testowa
N_values = [5_000_000, 6_000_000, 7_000_000]
r = 1.0  # Ustalone r

# Listy na czasy wykonania t_c
times_python = []
times_numba = []
times_ctypes = []
times_mypyc = []

# rozgrzewka jit numby
steinmetz_numba_warmup(1_000_000, r)

# petla pomiarowa
for N in N_values:
    print(f"Liczę dla N = {N}")

    # czysty Python
    t_py = steinmetz_pure_python(N, r)
    times_python.append(t_py)

    # numba
    t_nb = steinmetz_numba(N, r)
    times_numba.append(t_nb)

    # ctypes
    t_ct = steinmetz_c_lib(N, r)
    times_ctypes.append(t_ct)

    # mypyc
    t_mp = steinmetz_mypyc(N, r)
    times_mypyc.append(t_mp)

# liczenie wsp przyspieszenia p
# konwersja do numpy zeby wygodniej liczyc element po elemencie
times_python = np.array(times_python)
times_numba = np.array(times_numba)
times_ctypes = np.array(times_ctypes)
times_mypyc = np.array(times_mypyc)

p_numba = times_python / times_numba
p_ctypes = times_python / times_ctypes
p_mypyc = times_python / times_mypyc

