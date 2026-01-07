import ctypes

lib_name = './libsteinmetz.so' 
lib = ctypes.CDLL(lib_name)

# co ta funckja przyjmuje
lib.steinmetz_volume.argtypes = [ctypes.c_int, ctypes.c_double]
# co ta funkcja zwraca
lib.steinmetz_volume.restype = ctypes.c_double

N = 10_000_000
r = 1.0

steinmetz_volume_c = lib.steinmetz_volume(N, r)
print("Objętość bryły Steinmetza (C) wynosi:", steinmetz_volume_c)