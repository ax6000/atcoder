#include <iostream>
#include <string>
using namespace std;

int n;
void ft_combn(int cnt, string s){
    if(cnt == n){
        cout << s << endl;
        return;
    }
    char c = 'a' - 1 ;
    while( ++c <= s[cnt - 1] + 1){
        ft_combn(cnt + 1, s + c);
    }
}


int main (){

cin >> n ;
ft_combn(1,"a");
return 0;
}