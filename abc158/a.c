#include <stdio.h>

int main (void){
    char s[3];
    scanf("%s",s);
    int i = -1;
    int flg = 0;
    while(++i < 3){
        if(s[i] != s[0])
            flg = 1;
    }
    if(flg)
        printf("Yes\n");
    else 
        printf("No\n");
    return 0;
}