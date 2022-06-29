#include <iostream>
using namespace std;
#include <string>

int main (){
int x,flg; 
cin >> x;
if (x == 2){
    cout << 2 << endl;
return 0;
}
while(1){
    flg = 1;
    if(x % 2 == 0){
        x++;
        continue;
    }
       
    for (int i = 3; i < x; i+= 2)
    {
        if(x % i == 0){
            flg = 0;
            break;
        }
    }
    if(flg)
        break;
    x++;
}
cout << x << endl;
return 0;
}