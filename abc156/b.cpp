#include <iostream>
using namespace std;

int main (){
int n,k;
int cnt = 1;

cin >> n >> k ; 
while(k <= n){
    n /= k;
    cnt ++;
}

cout << cnt << endl;

return 0;
}