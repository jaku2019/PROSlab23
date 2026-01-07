#include <stdio.h>
#include <stdlib.h>

double random_double(double min, double max){
    int random_int = rand();
    // normalizacja do [0,1]
    double normalized = (double)random_int / (double)RAND_MAX;

    //skalowanie do min max i przesuniecie do zakresu
    double result = normalized * (max-min) + min;
    return result;
}

double random_point_in_cube(double min, double max){
    double x = random_double(min, max);
    double y = random_double(min, max);
    double z = random_double(min, max);

    return x, y, z;

}

int check_point_condition(double x, double y, double z){
    if ((x * x + y * y) <= 1.0 && (x * x + z * z) <= 1.0){
        return 1;
    }
    else{
        return 0;
    }
}

void main(){
    double x, y, z;

    double min = -2;
    double max = 2;

    x, y, z = random_point_in_cube(min, max);
    printf("Random point in cube: (%f, %f, %f)\n", x, y, z);
}