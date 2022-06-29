#include <stdio.h>

int main (void){
    int a,b;
    scanf("%d",&a);
    scanf("%d",&b);

    for(int j = 1; j<=1000; j++){
        if((int)(j*0.08) == a && (int)(j*0.1) == b){
         printf("%d\n",j);
         return 0;     
        }
    }
    printf("-1\n");
    return 0;
}
