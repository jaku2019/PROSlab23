import ctypes

lib_name = './libsteinmetz.so' 
lib = ctypes.CDLL(lib_name)

# co ta funckja przyjmuje
lib.steinmetz_volume.argtypes = [ctypes.c_int, ctypes.c_double]
# co ta funkcja zwraca
lib.steinmetz_volume.restype = ctypes.c_double

def steinmetz_volume_c(N, r):
    return lib.steinmetz_volume(N, r)