// #include <stdio.h>
// void meow(void);
// int main(void)
// {

//     for (int i = 0; i < 3; i++)
//     {
//         meow();
//     };
// }
// void meow(void){
//     printf("meow\n");
// };


#include <stdio.h>
void meow(int count);
int main(void)
{
    meow(5);
}
void meow(int count){
    for (int i = 0; i < count; i++)
    {
    printf("meow\n");
    };
};
