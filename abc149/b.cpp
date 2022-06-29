#include <iostream>
using namespace std;
#include <string>

int main (){
long long a,b,k,ansa,ansb;
 
cin >> a >> b >> k; 

if (k > a){
    ansa = 0;
    k -= a;
    ansb = b-k;
}else
{
    ansa = a-k;
    ansb = b;
}
if(ansb < 0)
    ansb = 0;

cout << ansa <<  " " << ansb << endl;
return 0;
}