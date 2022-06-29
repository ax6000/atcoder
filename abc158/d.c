#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void revStr(char* str){
	int size = strlen(str);
	int i,j;
	char tmp = {0};
	
	for(i = 0, j = size - 1; i < size / 2; i++, j--){
		tmp = str[i];
		str[i] = str[j];
		str[j] =tmp;
	}
	return;	
}

int main (void){
char *s,*tmp;
s = malloc(300001);
int q;
int first,mode;
char *c;
c = malloc(2);

scanf("%s",s);
scanf("%d",&q);
for(int i = 0; i < q; i++){
    scanf("%d", &first);
    if(first == 1)
      revStr(s); 
    else
    {
        scanf("%d",&mode);
        free(c);
        c = malloc(2);
        scanf("%s",c);
        if(mode == 1){
            strcat(c,s);
            strcpy(s,c);
        }
        else{
            strcat(s,c);
        }
    }
}
printf("%s\n",s);
return 0;
}