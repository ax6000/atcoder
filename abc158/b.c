#include <stdio.h>

int main (void){
unsigned long long int  a,b,n;
scanf("%llu",&n);
scanf("%llu",&a);
scanf("%llu",&b);

if(a == 0)
    printf("0\n");
else if(n%(a+b) < a)
    printf("%llu\n",n/(a+b)*a+n%(a+b));
else 
     printf("%llu\n",n/(a+b)*a+a);
return 0;
}