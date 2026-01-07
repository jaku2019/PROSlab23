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

int check_point_condition(double x, double y, double z){
    if ((x * x + y * y) <= 1 && (x * x + z * z) <= 1){
        return 1;
    } else {
        return 0;
    }
}

void main(){
    int N = 1000000;    // liczba prob
    double x, y, z;     // wspolrzedne punktu
    double hit_count = 0;  // Licznik trafien
    double r = 1.0;     // promien walcow
    double steinmetz_volume; // objetosc Steinmetza
    
    // zakres 2r
    double min = -r;
    double max = r;
    for (int i = 0; i < N; i++){

        // losowanie 3 pktow
        x = random_double(min, max);
        y = random_double(min, max);
        z = random_double(min, max);

        // Jesli funkcja zwrocila 1, zwiekszamy licznik
        if (check_point_condition(x, y, z) == 1) {
            hit_count++;
        }
    }
    
    // obliczanie objetosci Steinmetza
    steinmetz_volume = 8 * r * r * r * hit_count / N;
    printf("Obj Steinmetza: %f\n", steinmetz_volume);
}