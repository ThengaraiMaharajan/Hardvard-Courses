#include <stdio.h>
int main (void){
    int counter = 1;
    while (counter <= 3){
        printf("Hello, World! , %i \n", counter);
        counter++;
    }

    for (int i = 3; i > 0; i--){
        printf("Hello, World! , %i \n", i);
    }
}