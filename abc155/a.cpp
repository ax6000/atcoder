#include <iostream>
using namespace std;

int main (){
    int a,b,c,flg;
    cin >> a >> b >> c;
    flg = 0;
    if(a == b && b != c)
        flg = 1;
    else if(b == c && b != a)
        flg = 1;
    else if(c == a && a != b)
        flg = 1;
    if(flg)
    cout << "Yes" << endl;
    else
    cout << "No" << endl;
    return 0;

}