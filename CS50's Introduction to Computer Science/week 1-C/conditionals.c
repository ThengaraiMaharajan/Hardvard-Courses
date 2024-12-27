#include <stdio.h>
int main(void){
    int x = 30;
    int y = 30;
    if(x<y)
    {
        printf("%i is smaller than %i", x,y);
    }
    else if (x==y)
    {
        printf("%i is equal to %i", x,y);
    }
    else
    {
        printf("%i is greater than %i", x,y);
    }
}