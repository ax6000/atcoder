#include <iostream>
#include <cmath>
using namespace std;

int main (){
long double  a,b,c;
long double aa,bb,cc;
cin >> a >> b>> c;
aa = sqrtl(a);
bb = sqrtl(b);
cc = sqrtl(c);
if( aa + bb - cc < 0) 
    cout << "Yes" << endl;
else
    cout << "No" << endl;
return 0;
}