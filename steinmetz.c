#include <stdio.h>
#include <stdlib.h>

double random_double(double min, double max) {
    int random_int = rand();
    // normalizacja do [0,1]
    double normalized = (double)random_int / (double)RAND_MAX;

    //skalowanie do min max i przesuniecie do zakresu
    double result = normalized * (max-min) + min;
    return result;
}

